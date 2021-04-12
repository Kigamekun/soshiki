from django import forms

from .models import kotakSurat


class kotakSuratForm(forms.ModelForm):
	class Meta :
		model = kotakSurat
		fields = ['nama','saran','keluhan']

		widgets = {
		'nama':forms.TextInput(attrs = {'class':'form-control',}),
		'saran':forms.TextInput(attrs = {'class':'form-control',}),
		'keluhan':forms.TextInput(attrs = {'class':'form-control',}),
		}