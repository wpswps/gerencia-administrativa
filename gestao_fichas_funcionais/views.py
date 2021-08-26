from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .models import *

from django.views.generic import View
from django.http import JsonResponse

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

	return render(request, 'acompanhar_ficha.html', {'servidores':servidores, 'unidade':unidade})



class UpdateServidor(View):
	def get(self, request):
		id1 = request.GET.get('id', None)
		matricula1 = request.GET.get('matricula', None)
		nome1 = request.GET.get('nome', None)
		status_recebido1 = request.GET.get('status_recebido', None)
		data_status_recebido1 = request.GET.get('data_status_recebido', None)
		status_conferido1 = request.GET.get('status_conferido', None)
		data_status_conferido1 = request.GET.get('data_status_conferido', None)
		status_encaminhado_sead1 = request.GET.get('status_encaminhado_sead', None)
		data_status_encaminhado_sead1 = request.GET.get('data_status_encaminhado_sead', None)
		num_oficio_encaminhado_sead1 = request.GET.get('num_oficio_encaminhado_sead', None)
		status_devolucao1 = request.GET.get('status_devolucao', None)
		data_status_devolucao1 = request.GET.get('data_status_devolucao', None)
		status_encaminhado_gabinete1 = request.GET.get('status_encaminhado_gabinete', None)
		data_status_encaminhado_gabinete1 = request.GET.get('data_status_encaminhado_gabinete', None)












		obj = RelacaoGeralServidor.objects.get(id=id1)
		obj.matricula = matricula1
		obj.nome = nome1
		obj.status_recebido = status_recebido1
		obj.data_status_recebido = data_status_recebido1
		obj.status_conferido = status_conferido1
		obj.data_status_conferido = data_status_conferido1
		obj.status_encaminhado_sead = status_encaminhado_sead1
		obj.data_status_encaminhado_sead = data_status_encaminhado_sead1
		obj.num_oficio_encaminhado_sead = num_oficio_encaminhado_sead1
		obj.status_devolucao = status_devolucao1
		obj.data_status_devolucao = data_status_devolucao1
		obj.status_encaminhado_gabinete = status_encaminhado_gabinete1
		obj.data_status_encaminhado_gabinete = data_status_encaminhado_gabinete1

		obj.save()

		gerencia = {'id':obj.id,'matricula':obj.matricula,'nome':obj.nome,'status_recebido':obj.status_recebido,
		'data_status_recebido':obj.data_status_recebido,'status_conferido':obj.status_conferido,
		'data_status_conferido':obj.data_status_conferido,'status_encaminhado_sead':obj.status_encaminhado_sead,
		'data_status_encaminhado_sead':obj.data_status_encaminhado_sead,
		'num_oficio_encaminhado_sead':obj.num_oficio_encaminhado_sead,'status_devolucao':obj.status_devolucao,
		'data_status_devolucao':obj.data_status_devolucao,'status_encaminhado_gabinete':obj.status_encaminhado_gabinete,
		'data_status_encaminhado_gabinete':obj.data_status_encaminhado_gabinete}

		data = {
		'gerencia': gerencia
		}

		return JsonResponse(data)