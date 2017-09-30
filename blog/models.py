from django.db import models
from django.utils import timezone
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField

class Imagem(models.Model):
    album = models.ForeignKey('Imovel', related_name='imagens')
    titulo = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)
    imagem = CloudinaryField('imagem')

    def __unicode__(self):
        try:
            public_id = self.imagem.public_id
        except AttributeError:
            public_id = ''
        return "Imagem <%s:%s>" % (self.titulo, public_id)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Imovel(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    localizacao = models.TextField()
    tamanho = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Destaque(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300)
    published_date = models.DateTimeField(blank=True, null=True)
    imagem = CloudinaryField('imagem')

    def __unicode__(self):
        try:
            public_id = self.imagem.public_id
        except AttributeError:
            public_id = ''
        return "Imagem <%s:%s>" % (self.titulo, public_id)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def cloudnary_up(self):
        cloudinary.uploader.upload("self.imagem.url")

    def __str__(self):
        return self.titulo

class Depoimento(models.Model):
    autor = models.ForeignKey('auth.user')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    imagem = CloudinaryField('imagem')

    def __unicode__(self):
        try:
            public_id = self.imagem.public_id
        except AttributeError:
            public_id = ''
        return "Imagem <%s:%s>" % (self.titulo, public_id)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
