from django.shortcuts import render, redirect, HttpResponse
from .models import Meus_livros
from .forms import Meus_livros_form


def pagina_inicial(request):
    return HttpResponse("Livros para ler!")


def pagina_contato(request):
    return HttpResponse("Nosso contato! Luizinho_2002@hotmail.com")


def motivos_para_ler(request):
    return render(request, "meus_livros/motivos_para_ler.html")


def novo_livro(request):
    return render(request, "meus_livros/novo_livro.html")


def livro_registrado(request):
    livro = {"tipo_livro": request.POST.get("TipoLivro")}
    return render(request, "meus_livros/livro_registrado.html", livro)


# com a função criada na variável livro as informações são passadas para a página livro registrado.html.
# #É necessário especificar na função render a variável livro.


def livros_lidos(request):
    dados = {"dados": Meus_livros.objects.all()}
    return render(request, "meus_livros/livros_lidos.html", context=dados)


def detalhe(request, id_livros_lidos):
    dados = {"dados": Meus_livros.objects.get(pk=id_livros_lidos)}
    return render(request, "meus_livros/detalhe.html", dados)


def criar(request):
    if request.method == "POST":
        livros_form = Meus_livros_form(request.POST)
        if livros_form.is_valid():
            livros_form.save()
        return redirect("livros_lidos")
    else:
        livros_form = Meus_livros_form()
        formulário = {"formulário": livros_form}
        return render(request, "meus_livros/novo_livro.html", context=formulário)


def editar(request, id_livros_lidos):
    meus_livros = Meus_livros.objects.get(pk=id_livros_lidos)
    if request.method == "GET":
        formulário = Meus_livros_form(instance=meus_livros)
        return render(
            request, "meus_livros/novo_livro.html", {"formulário": formulário}
        )
    else:
        formulário = Meus_livros_form(request.POST, instance=meus_livros)
        if formulário.is_valid():
            formulário.save()
        return redirect("livros_lidos")


def excluir(request, id_livros_lidos):
    meus_livros = Meus_livros.objects.get(pk=id_livros_lidos)
    if request.method == "POST":
        meus_livros.delete()
        return redirect("livros_lidos")
    return render(request, "meus_livros/confirmar_exclusao.html", {"item": meus_livros})
