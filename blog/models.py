from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

def imagem_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (slugify(instance.titulo), ext)
    # file will be uploaded to MEDIA_ROOT/blog/<slug>/<filename>
    return 'blog/{}/{}'.format(slugify(instance.titulo), filename)

class Category(models.Model):
    nome = models.CharField(max_length=100)
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(verbose_name='Título', max_length=250)
    slug = models.SlugField(max_length=250)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    categoria = models.ManyToManyField(Category, related_name='get_posts', verbose_name='Categorias')
    imagem = models.ImageField(upload_to=imagem_directory_path, blank=True, null=True)
    conteudo = RichTextField(verbose_name='Conteúdo')
    publicado = models.DateTimeField(default=timezone.now, verbose_name='Data de publicação')
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='rascunho')

    class Meta:
        ordering = ('-publicado',)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])
    
    def get_absolute_url_edit(self):
        return reverse('post_edit', args=[self.pk])
    
    def get_absolute_url_delete(self):
        return reverse('post_delete', args=[self.pk])

    def __str__(self):
        return self.titulo


@receiver(post_save, sender=Post)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save()