import django_filters
from django_filters import CharFilter

from .models import *

class ManagementFilter(django_filters.FilterSet):
    titulo = CharFilter(lookup_expr='icontains', label='Título')


    class Meta:
        model = Post
        fields = ['titulo', 'publicado','status', 'categoria']

class HomeFilter(django_filters.FilterSet):
    titulo = CharFilter(lookup_expr='icontains', label='Título')


    class Meta:
        model = Post
        fields = ['titulo', 'categoria']