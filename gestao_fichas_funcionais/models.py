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
	

	RECEBIDO = 'Recebido'
	NAORECEBIDO = 'Não Recebido'
	RECEBIDO_TYPE = (
		(RECEBIDO, 'Recebido'),
		(NAORECEBIDO, 'Não Recebido'),
		)

	status_recebido = models.CharField(max_length = 200, choices=RECEBIDO_TYPE, null=True, blank=True)
	data_status_recebido = models.DateField(null=True)
	user_status_recebido = models.CharField(max_length = 200, null=True, blank=True)
	

	CONFERIDO = 'Conferido'
	NAOCONFERIDO = 'Não Conferido'
	CONFERIDO_TYPE = (
		(CONFERIDO, 'Conferido'),
		(NAOCONFERIDO, 'Não Conferido'),
		)

	status_conferido = models.CharField(max_length=200, choices=CONFERIDO_TYPE, blank=True, null=True)
	data_status_conferido = models.DateField(null=True)
	user_status_conferido = models.CharField(max_length = 200, null=True, blank=True)
	
	
	ENCAMINHADOSEAD = 'Enc. SEAD'
	NAOENCAMINHADOSEAD = 'Não Enc. SEAD'
	ENCAMINHADOSEAD_TYPE = (
		(ENCAMINHADOSEAD, 'Enc. SEAD'),
		(NAOENCAMINHADOSEAD, 'Não Enc. SEAD'),
		)
	status_encaminhado_sead = models.CharField(max_length=200, choices=ENCAMINHADOSEAD_TYPE, blank=True, null=True)
	data_status_encaminhado_sead = models.DateField(null=True)
	user_status_encaminhado_sead = models.CharField(max_length = 200, null=True, blank=True)
	num_oficio_encaminhado_sead = models.CharField(max_length = 200, null=True, blank=True)
	

	DEVOLUCAOCOLHERASSIN = 'Devolvido Colher Assinatura'
	NAODEVOLVIDOCOLHERASSIN = 'Não Devolvido Colher Assinatura'
	DEVOLUCAOCOLHERASSIN_TYPE = (
		(DEVOLUCAOCOLHERASSIN, 'Devolvido Colher Assinatura'),
		(NAODEVOLVIDOCOLHERASSIN, 'Não Devolvido Colher Assinatura'),
		)
	status_devolucao_colher_assinatura = models.CharField(max_length=200, choices=DEVOLUCAOCOLHERASSIN_TYPE, blank=True, null=True)
	data_status_devolucao_colher_assinatura = models.DateField(null=True)
	user_status_devolucao_colher_assinatura = models.CharField(max_length = 200, null=True, blank=True)


	data_devolucao_contrato_assinado = models.DateField(null=True)
	user_data_devolucao_contrato_assinado = models.CharField(max_length = 200, null=True, blank=True)

	
	DEVOLUCAO = 'Devolvido'
	NAODEVOLVIDO = 'Não Devolvido'
	DEVOLUCAO_TYPE = (
		(DEVOLUCAO, 'Devolvido'),
		(NAODEVOLVIDO, 'Não Devolvido'),
		)
	status_devolucao = models.CharField(max_length=200, choices=DEVOLUCAO_TYPE, blank=True, null=True)
	data_status_devolucao = models.DateField(null=True)
	user_status_devolucao = models.CharField(max_length = 200, null=True, blank=True)
	
	
	GABINETE = 'Enc. Gabinete'
	NAOENCGABINETE = 'Não Enc. Gabinete'
	GABINETE_TYPE = (
		(GABINETE, 'Enc. Gabinete'),
		(NAOENCGABINETE, 'Não Enc. Gabinete'),
		)
	status_encaminhado_gabinete = models.CharField(max_length=200, choices=GABINETE_TYPE, blank=True, null=True)
	data_status_encaminhado_gabinete = models.DateField(null=True)
	user_status_encaminhado_gabinete = models.CharField(max_length = 200, null=True, blank=True)
	


	def __str__(self):
		return str(self.codigo)