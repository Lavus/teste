from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^imovel/(?P<pk>[0-9]+)/$', views.imovel_info, name='imovel_info'),
    url(r'^list_imovel/', views.list_imovel, name='listar_imagens_imovel'),
    url(r'^list_depoimento/', views.list_depoimento, name='listar_imagens_depoimento'),
    url(r'^list_destaque/', views.list_destaque, name='listar_imagens_destaque'),
    url(r'^upload_imovel/', views.upload_imovel, name='upload_imagens_imovel'),
    url(r'^upload_depoimento/', views.upload_depoimento, name='upload_imagens_depoimento'),
    url(r'^upload_destaque/', views.upload_destaque, name='upload_imagens_destaque')
]
