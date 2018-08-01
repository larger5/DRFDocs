from rest_framework import serializers
from booktest.models import BookInfo

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookInfo
        # fields = ('btitle','bpub_date')
        fields = '__all__'  # 包含所有属性