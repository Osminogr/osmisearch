from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Category, ProductItem,DataHub

@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = 'category'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Category
         fields = [
             'title',
         ]

@registry.register_document
class ItemDocument(Document):
    categories = fields.NestedField(properties={
        'title': fields.TextField(),
        'code': fields.TextField()
    })
    hub = fields.NestedField(properties={
        'id': fields.IntegerField(),
        'email': fields.TextField(),
        'hub_link':fields.TextField()
    })
    class Index:
        name = 'item'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = ProductItem
         
         fields = [
             'title',
             'description',
             'image_link',
             'link',
             'currency_code',
             'price',
         ]
         related_model = [Category,DataHub]