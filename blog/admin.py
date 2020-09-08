from django.contrib import admin

from .models import Post, Category

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado', 'publicado')
    list_filter = ('nome', 'criado', 'publicado')
    search_fields = ('nome',)
    date_hierarchy = 'publicado'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)} #Colocar o slug automático pelo titulo
    list_display = ('titulo', 'autor', 'publicado', 'status') #Culunas da tabela
    list_filter = ('status', 'criado', 'publicado', 'autor') #Filtro de pesquisa por status, criado, publicado e autor
    search_fields = ('titulo', 'conteudo',) #Barra de pesquisa por titulo e conteúdo
    date_hierarchy = 'publicado' #Filtro de hierarquia por data
    raw_id_fields = ('autor',) #Colocar mais de um autor na publicação