from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Category, ProductItem,DataHub

@registry.register_document
class ItemDocument(Document):
    category = fields.NestedField(properties={
        'title': fields.TextField(),
        'code': fields.TextField()
    })
    hub = fields.ObjectField(properties={
        'id': fields.KeywordField(),
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