from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CategoriaForm, ProdutoForm
from .services import CategoriaService, ProdutoService


class CategoriaView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CategoriaService()

    def get(self, request, acao=None, id=None):
        if acao is None:
            registros = self.service.listar()
            return render(request, 'categorias_listar.html', context={'registros': registros})

        elif acao == 'incluir':
            form = CategoriaForm()
            return render(request, 'categorias_editar.html', context={'acao': 'Inclusão', 'form': form})

        elif acao in ('alterar', 'excluir'):
            registro = self.service.buscar_por_id(id)
            form = CategoriaForm(initial={'id': registro[0], 'descricao': registro[1]})
            acao_label = 'Alteração' if acao == 'alterar' else 'Exclusão'
            return render(request, 'categorias_editar.html', context={'acao': acao_label, 'form': form})

        elif acao == 'salvar':
            # alguém acessou /categorias/salvar/ via GET por engano
            return HttpResponseRedirect(reverse("categorias"))

    def post(self, request, acao=None, id=None):
        form_data = request.POST
        acao_form = form_data['acao']

        if acao_form == 'Inclusão':
            self.service.incluir(form_data['descricao'])
        elif acao_form == 'Exclusão':
            self.service.excluir(form_data['id'])
        else:
            self.service.alterar(form_data['id'], form_data['descricao'])

        return HttpResponseRedirect('/categorias/')


class ProdutoView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ProdutoService()

    def _choices(self):
        categorias = self.service.listar_categorias()
        return [(c[0], c[1]) for c in categorias]

    def _form_com_dados(self, registro):
        return {
            'id': registro[0],
            'descricao': registro[1],
            'preco_unitario': registro[2],
            'quantidade_estoque': registro[3],
            'categoria_id': registro[4],
        }

    def get(self, request, acao=None, id=None):
        if acao is None:
            registros = self.service.listar()
            return render(request, 'produtos_listar.html', context={'registros': registros})

        elif acao == 'incluir':
            form = ProdutoForm(categoria_choices=self._choices())
            return render(request, 'produtos_editar.html', context={'acao': 'Inclusão', 'form': form})

        elif acao in ('alterar', 'excluir'):
            registro = self.service.buscar_por_id(id)
            form = ProdutoForm(categoria_choices=self._choices(), initial=self._form_com_dados(registro))
            acao_label = 'Alteração' if acao == 'alterar' else 'Exclusão'
            return render(request, 'produtos_editar.html', context={'acao': acao_label, 'form': form})

        elif acao == 'salvar':
            # alguém acessou /produtos/salvar/ via GET por engano
            return HttpResponseRedirect(reverse("produtos"))

    def post(self, request, acao=None, id=None):
        form_data = request.POST
        acao_form = form_data['acao']

        if acao_form == 'Inclusão':
            self.service.incluir(
                form_data['descricao'],
                form_data['preco_unitario'],
                form_data['quantidade_estoque'],
                form_data['categoria_id'],
            )
        elif acao_form == 'Exclusão':
            self.service.excluir(form_data['id'])
        else:
            self.service.alterar(
                form_data['id'],
                form_data['descricao'],
                form_data['preco_unitario'],
                form_data['quantidade_estoque'],
                form_data['categoria_id'],
            )

        return HttpResponseRedirect('/produtos/')


def home(request):
    return render(request, 'home.html')