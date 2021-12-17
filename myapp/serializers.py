from django.db.models import fields
from rest_framework import serializers
from myapp.models import AppContent

class AppContentSerializer(serializers.ModelSerializer):
    # contentId = serializers.Field(source='id')
    # contentId=location = serializers.SerializerMethodField(source='id')
    class Meta:
        model=AppContent
        fields=('id','title','content','published_at','created_at','updated_at')