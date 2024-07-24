from django.urls import path
from . import views

urlpatterns  = [
path('', views.home , name = 'home'),
path('home2', views.home2 , name = 'home2'),
path('editar_proj', views.editar_proj , name = 'editar_proj'),
path('salvar', views.salvar , name = 'salvar'),
path('delete', views.delete , name = 'delete'),
path('edit', views.edit , name = 'edit'),
path('alter', views.alter , name = 'alter'),
path('apaga_projeto', views.apaga_projeto , name = 'apaga_projeto'),
path('criar_proj', views.criar_proj , name = 'criar_proj'),
path('duplicar_projeto', views.duplicar_projeto , name = 'duplicar_projeto'),
path('duplicar_dados', views.duplicar_dados , name = 'duplicar_dados'),
path('novo_nome', views.novo_nome , name = 'novo_nome'),

]

