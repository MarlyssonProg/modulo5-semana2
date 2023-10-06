# Responsável por redirecionar de uma url a outra url
from django.shortcuts import render, redirect
from base.forms import ContatoForm, ReservaForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
# View inicio, que é a primeira a ser acessada pelo usuário


def inicio(request):
    return render(request, "index.html")


# View contato
def contato(request):
    # Definir sucesso, para indicar se o envio da mensagem foi correto ou não
    sucesso = False

    if request.method == 'GET':  # Se for um método Get
        form = ContatoForm()
    # Se for um método POST
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():  # Verificar se form é válido
            sucesso = True
            # Alteração para salvar os dados informados na página contato
            form.save()

    contexto = {  # Definir o contexto da view contato
        'telefone': '(99) 97999-9891',
        'responsavel': 'João da Silva Santos',
        'form': form,
        'sucesso': sucesso
    }

    # Renderizar a página
    return render(request, "contato.html", contexto)


# View para reserva de banho do pet
def reserva(request):
    # Sucesso no envio da mensagem
    sucesso = False

    if request.method == 'GET':  # Se método da requisição é GET
        form = ReservaForm()
    # Método POST
    else:
        form = ReservaForm(request.POST)
        if form.is_valid():  # Verificar se form é válido
            sucesso = True
            # Alteração para salvar os dados informados na página reserva
            form.save()

    contexto = {  # Criar contexto da view de reserva
        'form': form,
        'sucesso': sucesso
    }

    return render(request, "reserva.html", contexto)


# View de login de usuário
# Define o nome e o parâmetro da função.
def login_usuario(request):
    # Verifica se o método da requisição é GET
    if request.method == 'GET':
        # Esta linha cria uma instância do formulário de login.
        formulario = AuthenticationForm()
        contexto = {
            'formulario': formulario
        }
        # Renderiza o template login.html e passa o formulário de login para o template.
        # Tá passando como parâmetro porque é só um se fosse mais seria certamente um dicionário
        return render(request, "login.html", {'formulario': formulario})

    else:
        # As variáveis nome_usuario e senha recebem o nome e senha do usuario do input da página
        nome_usuario = request.POST['username']
        senha = request.POST['password']
        # As variáveis nome_usuario e senha são autenticadas para o login do usuário ser feito
        usuario = authenticate(request, username=nome_usuario, password=senha)
        # Verifica se usuário não for nulo
        if usuario is not None:
            # Requisita a autenticação da variável que recebe a autenticação nome_usuario e senha
            login(request, usuario)
            # Faz referencia a urls urlpatterns contida em urls.py abaixo do path admin
            return redirect('inicio')

# View de logout é mais simples e menos autenticada já que é pra saida do software
def logout_usuario(request):
    logout(request)
    return redirect('inicio')
