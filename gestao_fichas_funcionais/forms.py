from django import forms

from .models import RelacaoGeralServidor

class RelacaoGeralServidorForm(forms.ModelForm):
	class Meta:
		model: RelacaoGeralServidor
		fields = ()