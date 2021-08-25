from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .models import *

# Create your views here.

def login_page(request):
	return render(request, 'login_page.html')


@csrf_protect
def login_submit(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			return render(request, 'login_page.html')
			#messages.error(request, 'Usuário e/ou senha inválido!')
	return redirect('/login/')



@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def index(request):
	return render(request, 'index.html')


@login_required(login_url='/login/')
def informar_dados_ficha(request):
	return render(request, 'informar_dados_ficha.html')


@login_required(login_url='/login/')
def set_informar_dados_ficha(request):
	return redirect('index')


@login_required(login_url='/login/')
def localizar_fichas(request):
	relacao_all = RelacaoGeralServidor.objects.order_by('unidade').distinct('unidade')


	return render(request, 'localizar_fichas.html', {'relacao_all':relacao_all})


@login_required(login_url='/login/')
def set_localizar_fichas(request):
	unidade = request.POST.get('unidade')
	request.session['unidade'] = unidade
	#contexto = {'servidores': None}
	'''
	if request.method=='POST':
		unidade = request.POST.get('unidade')
		servidores = RelacaoGeralServidor.objects.filter(unidade=unidade)
		contexto = {'servidores': servidores}
		#qtd = len(list(contexto.values()))
		#print("entrou no if. Valor unidade:", unidade, "qtd:", contexto['matricula'])
		'''

	return redirect('acompanhar_ficha')


@login_required(login_url='/login/')
def acompanhar_ficha(request):
	relacao_all = RelacaoGeralServidor.objects.all()
	unidade = request.session['unidade']
	servidores = RelacaoGeralServidor.objects.filter(unidade=unidade).order_by('nome')

	return render(request, 'acompanhar_ficha.html', {'servidores':servidores})