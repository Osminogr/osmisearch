
from elasticsearch_dsl import Q
from django.shortcuts import render
from jmespath import search
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from bs4 import BeautifulSoup

from .documents import ItemDocument
from .models import *
from .serializers import *
import time

class GetDataHubView(APIView):
    def get(self, request, pk = 2):
        queryset = ProductItem.objects.all().filter(hub_id = pk)
        serializer = ProductItem_serializer(
            instance=queryset,
            many = True
        )
        return Response(serializer.data)

class SetDataHubView(APIView):
    def get(self,request):
        DataHub.objects.create(
            email=request.GET['email'],
            hub_link = request.GET['hub_link'],
            phone = request.GET['phone']
        )
        return Response({'s':True})

from progress.bar import PixelBar,FillingCirclesBar

class ShopGenerator(APIView):
    def get(self,request):
        
        updated = []
        hubs = DataHub.objects.all()
        for hub in hubs:
            updated.append(hub.id)
            req = requests.get(hub.hub_link)
            soup = BeautifulSoup(req.content,features='xml')
            
            #Очищаем категории
            start_time = time.time()
            try:
                h_categories = Category.objects.all().filter(hub_id = hub.id)
                h_categories._raw_delete(h_categories.db)
            except:
                pass
            print("--- %s seconds Category del ---" % (time.time() - start_time))
            start_time = time.time()
            try:
                h_items = ProductItem.objects.all().filter(hub_id = hub.id)
                h_items._raw_delete(h_items.db)
            except:
                pass
            print("--- %s seconds Item del ---" % (time.time() - start_time))
            #Пересоздаем категории
            xml_categories = soup.findAll("category")
            c_bar = FillingCirclesBar(
                'Updating Categories in Hub '+ str(hub.id),
                max=len(xml_categories)
                
            )
            for tag in xml_categories:
                Category.objects.create(
                    title = tag.text,
                    code = tag['id'],
                    hub_id=hub.id
                )
                c_bar.next()
            c_bar.finish()

            xml_items = soup.findAll("offer")
            i_bar = FillingCirclesBar(
                'Updating items in Hub '+ str(hub.id),
                max=len(xml_items)
                
            )
            for tag in xml_items:
                ProductItem.objects.create(
                    hub = hub,
                    title=tag.find('name').text,
                    description = tag.find('description').text,
                    currency_code = tag.find('currencyId').text,
                    image_link = tag.find('picture').text,
                    price = tag.find('price').text,
                    link = tag.find('url').text,
                    categories = Category.objects.get(code=tag.find('categoryId').text),
                )
                i_bar.next()
            i_bar.finish()
            
        return Response({'updated': hub.id})

from .translators import basic_transliter
from transliterate import translit
class SearchView(APIView):
    def get(self, request, pk):
        if request.GET['q']:
            hub = DataHub.objects.get(id=pk)
            try:
                translit_text = translit(request.GET['q'],reversed=True)
            except:
                translit_text = request.GET['q']
            q = Q(
                    'bool',
                    must=[

                    ],
                    must_not=[
                    ],
                    should=[
                        Q('fuzzy', title=request.GET['q']),
                        Q('fuzzy', description=request.GET['q']),


                        Q('fuzzy', description=basic_transliter(request.GET['q'])),
                        Q('fuzzy', title=basic_transliter(request.GET['q'])),

                        Q('fuzzy', title=translit_text),
                        Q('fuzzy', description=translit_text),

                        Q('match', category__title=request.GET['q']),
                    ],
        minimum_should_match=0)
            search = ItemDocument.search().extra(size=100).query(q)
            queryset = search.execute()
            serializer = ProductItem_serializer(
                instance=queryset,
                many = True
            )
            return Response(serializer.data)
        else:
            return Response({})