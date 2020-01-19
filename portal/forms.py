from django import forms
from .models import Area, Noticia

class AreaForm(forms.ModelForm):

	class Meta:
		model = Area
		fields = ('descricao', 'cor')

class NoticiaForm(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ('photo','area','title','text')