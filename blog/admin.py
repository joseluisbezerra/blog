from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)} #Colocar o slug automático pelo titulo
    list_display = ('titulo', 'autor', 'publicado', 'status') #Culunas da tabela
    list_filter = ('status', 'criado', 'publicado', 'autor') #Filtro de pesquisa por status, criado, publicado e autor
    search_fields = ('titulo', 'conteudo') #Barra de pesquisa por titulo e conteúdo
    date_hierarchy = 'publicado' #Filtro de hierarquia por data
    raw_id_fields = ('autor',) #Colocar mais de um autor na publicação