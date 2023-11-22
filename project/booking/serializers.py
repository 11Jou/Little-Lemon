from rest_framework import serializers
from django.contrib.auth.models import User
from decimal import Decimal
from django.utils.text import slugify
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(method_name='get_slug', read_only=True)
    class Meta:
        model = Category
        fields =['id','slug']

    def get_slug(self, category):
        return slugify(category.title)
    

class MenuItemsSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    ) 
    class Meta:
        model = MenuItem
        fields = "__all__"


