"""
URL configuration for proj_bd project.
...
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app import views
from app.views import CategoriaView, ProdutoView

urlpatterns = [
    path('admin/', admin.site.urls),
    # define as rotas de URL da nossa aplicacao
    path('', views.home, name='home'),
    # path('instrucoes/', 'instrucoes/instrucoes.html', name='instrucoes'),


    # ===========================================================================
    # Rotas: CATEGORIA
    #   - categorias/              : exibe página de listagem
    #   - categorias/incluir/      : exibe a página de inclusao de registro
    #   - categorias/alterar/<id>/ : exibe a página de alteracao de registro
    #   - categorias/excluir/<id>/ : exibe a página de exclusao de registro
    #   - categorias/salvar/       : insere, altera ou exclui um registro do BD
    #
    path('categorias/', CategoriaView.as_view(), name='categorias'),
    path('categorias/<str:acao>/', CategoriaView.as_view(), name='categorias'),
    path('categorias/<str:acao>/<int:id>/', CategoriaView.as_view(), name='categorias'),

    # ===========================================================================
    # Rotas: PRODUTO
    #   - produtos/              : exibe página de listagem
    #   - produtos/incluir/      : exibe a página de inclusao de registro
    #   - produtos/alterar/<id>/ : exibe a página de alteracao de registro
    #   - produtos/excluir/<id>/ : exibe a página de exclusao de registro
    #   - produtos/salvar/       : insere, altera ou exclui um registro do BD
    #
    path('produtos/', ProdutoView.as_view(), name='produtos'),
    path('produtos/<str:acao>/', ProdutoView.as_view(), name='produtos'),
    path('produtos/<str:acao>/<int:id>/', ProdutoView.as_view(), name='produtos'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)