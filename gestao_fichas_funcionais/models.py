from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class RelacaoGeralServidor(models.Model):

	codigo = models.IntegerField(blank=True, null=True)
	utb = models.CharField(max_length = 200, null=True, blank=True)
	unidade = models.CharField(max_length = 200, null=True, blank=True)
	cidade = models.CharField(max_length=200, blank=True, null=True)
	matricula = models.CharField(max_length = 200, null=True, blank=True)
	nome = models.CharField(max_length = 200, null=True, blank=True)
	cargo = models.CharField(max_length = 200, null=True, blank=True)
	funcao = models.CharField(max_length = 200, null=True, blank=True)
	cpf = models.CharField(max_length = 200, null=True, blank=True)
	nivel = models.IntegerField(blank=True, null=True)
	

	status_recebido = models.CharField(max_length = 100, null=True, blank=True)
	data_status_recebido = models.DateField(null=True)
	user_status_recebido = models.CharField(max_length = 200, null=True, blank=True)
	

	status_conferido = models.CharField(max_length=100, blank=True, null=True)
	data_status_conferido = models.DateField(null=True)
	user_status_conferido = models.CharField(max_length = 200, null=True, blank=True)
	
	
	status_encaminhado_sead = models.CharField(max_length=100, blank=True, null=True)
	data_status_encaminhado_sead = models.DateField(null=True)
	user_status_encaminhado_sead = models.CharField(max_length = 200, null=True, blank=True)
	num_oficio_encaminhado_sead = models.CharField(max_length = 200, null=True, blank=True)
	
	
	status_retorno_sead = models.CharField(max_length=100, blank=True, null=True)
	data_status_retorno_sead = models.DateField(null=True)
	user_status_retorno_sead = models.CharField(max_length = 200, null=True, blank=True)

	status_assinatura_contrato = models.CharField(max_length=100, blank=True, null=True)
	data_status_assinatura_contrato = models.DateField(null=True)
	user_status_assinatura_contrato = models.CharField(max_length = 200, null=True, blank=True)


	status_reconducao_sead = models.CharField(max_length=100, blank=True, null=True)
	data_status_reconducao_sead = models.DateField(null=True)
	user_status_reconducao_sead = models.CharField(max_length = 200, null=True, blank=True)
	
	
	status_encaminhado_gabinete = models.CharField(max_length=100, blank=True, null=True)
	data_status_encaminhado_gabinete = models.DateField(null=True)
	user_status_encaminhado_gabinete = models.CharField(max_length = 200, null=True, blank=True)

	nova_matricula = models.CharField(max_length = 200, null=True, blank=True)
	


	def __str__(self):
		return str(self.codigo)