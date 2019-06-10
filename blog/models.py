from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from accounts.models import User


class Post(models.Model):
    title = models.CharField('Título', max_length=200)
    content = RichTextUploadingField('Contenido')

    date_published = models.DateTimeField(
        'Fecha de publicación', auto_now_add=True)
    date_updated = models.DateTimeField('Última actualización', auto_now=True)

    cover_image = models.ImageField(
        'Imagen de portada',
        upload_to='blog/posts/cover_images')

    visible = models.BooleanField('Visible', default=True)

    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE)
    author.verbose_name = 'Autor'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
