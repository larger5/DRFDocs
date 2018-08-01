import django_filters
from django.db.models import Q
from .models import BookInfo

class BooksFilter(django_filters.rest_framework.FilterSet):

    # Django2.0 为 field_name 而不是 name
    btitle=django_filters.CharFilter(field_name='btitle',lookup_expr='icontains')   # contains 区分大小写

    class Meta:
        model = BookInfo
        fields = ['btitle', 'bpub_date']