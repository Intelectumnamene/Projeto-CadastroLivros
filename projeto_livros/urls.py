"""
URL configuration for projeto_livros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from livros import views
from usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('conta/',usuarios_views.novo_usuario,name='novo_usuario'),
    path('login/',auth_views.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='usuarios/logout.html'),name='logout'),
    path("motivos_para_ler/", views.motivos_para_ler, name="motivos_para_ler"),
    path("", views.livros_lidos, name="livros_lidos"),
    path("contato/", views.pagina_contato, name="contato"),
    path("novo_livro/", views.criar, name="novo_livro"),
    path("novo_livro/<int:id_livros_lidos>", views.editar, name="editar"),
    path("excluir_livro/<int:id_livros_lidos>", views.excluir, name="excluir"),
    path("livro_registrado/", views.livro_registrado, name="livro_registrado"),
    path("/<int:id_livros_lidos>", views.detalhe, name="detalhe"),
]
