from django.contrib import admin

from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado', 'publicado')
    list_filter = ('nome', 'criado', 'publicado')
    search_fields = ('nome',)
    date_hierarchy = 'publicado'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Colocar o slug automático pelo titulo
    prepopulated_fields = {'slug': ('titulo',)}
    list_display = ('titulo', 'autor', 'publicado',
                    'status')  # Culunas da tabela
    # Filtro de pesquisa por status, criado, publicado e autor
    list_filter = ('status', 'criado', 'publicado', 'autor')
    # Barra de pesquisa por titulo e conteúdo
    search_fields = ('titulo', 'conteudo',)
    date_hierarchy = 'publicado'  # Filtro de hierarquia por data
    raw_id_fields = ('autor',)  # Colocar mais de um autor na publicação
