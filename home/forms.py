from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
class PostNewsForm(forms.ModelForm):
	class Meta:
		model = PostNews
		fields = [
		'judul',
		'isi',
		'thumb',
		]
		widgets = {

		'judul':forms.TextInput(
			attrs = {
			'class':'form-control',
			'placeholder':'fill with title of News',


			}



			),
		'isi':forms.TextInput(
			attrs = {
			'class':'form-control',
			'placeholder':'fill this body of News',

			}
			


			),
		'thumb':forms.FileInput(
			attrs = {
			'class':'form-control',
			'id': 'inputGroupFile01',	
			
			}
			 


			),


		}
class CreateUser(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		widgets = {

			'username':forms.TextInput(
			attrs = {
			'class':'form-control',
			'placeholder':'fill with title of News',
			'autocomplete':"off",

			}



			),
			'email':forms.TextInput(
			attrs = {
			'class':'form-control',
			'placeholder':'fill with title of News',
			'autocomplete':"off",

			}



			),
			'password1':forms.PasswordInput(
			attrs = {
			'class':'form-control form-control-user',
			'placeholder':'fill with title of News',
			'autocomplete':"off",

			}



			),
			'password2':forms.PasswordInput(
			attrs = {
			'class':'form-control form-control-user',
			'placeholder':'fill with title of News',
			'autocomplete':"off",

			}



			),

		}
		def __init__(self,*args,**kwargs):
			super(CreateUser,self).__init__(*args,**kwargs)
			self.fields['password1'].widget = PasswordInput(attrs={'class':'form-control'})
			self.fields['password2'].widget = PasswordInput(attrs={'class':'form-control'})
			for visible in self.visible_fields():
				visible.field.widget.attrs['class'] = 'form-control'





class anggota_form(forms.ModelForm):
	class Meta:
		model = biodata

		fields = ['nama','jenis_kelamin','tgl_lahir','alamat','no_telepon','email','status']
		labels = {

			'nama':'Nama Lengkap',
			'jenis_kelamin':'Jenis Kelamin',
			'tgl_lahir':'Tanggal Lahir',
			'alamat':'Alamat',
			'no_telepon':'No Telepon',
			'email':'Email',
			'status':'status',

		}
		error_messages = {

			'nama':{
				'required':'Anda harus mengisi nama'
			},
			'jenis_kelamin':{
				'required':'Anda harus memilih jenis kelamin'
			},
			'tgl_lahir':{
				'required':'Anda harus mengisi tanggal lahir'
			},
			'alamat':{
				'required':'Anda harus mengisi alamat'
			},
			'no_telepon':{
				'required':'Anda harus mengisi nomer telepon'
			},
			'email':{
				'required':'Anda harus mengisi email'
			},
			'status':{
				'required':'Anda harus memilih status'
			}
		}
		# tgl_lahir = forms.DateField(
  #       input_formats=['%Y-%m-%d'],
  #       widget=forms.DateInput(attrs={
  #           'class': 'form-control datetimepicker-input',
  #           'data-target': '#datetimepicker4'
  #       })
  #   )

		#tgl_lahir = forms.DateField(widget= forms.SelectDateWidget(attrs={'class':'form-control',},years= range(1945,2019,1)))
		#tgl_lahir = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
		widgets = {
		'nama':forms.TextInput(attrs = {'class':'form-control',}),
		'tgl_lahir':forms.SelectDateWidget(attrs={'class':'form-control col-sm-4','autocomplete':"off"},years= range(1945,2019,1), ),
		# 'tgl_lahir':forms.DateTimeInput(attrs={
  #           'class': 'form-control datetimepicker-input',
  #           'data-target': '#datetimepicker1'
  #       }),
		'alamat':forms.TextInput(attrs = {'class':'form-control','autocomplete':"off"}),
		'no_telepon':forms.TextInput(attrs = {'class':'form-control','autocomplete':"off"}),
		'email':forms.TextInput(attrs = {'class':'form-control','autocomplete':"off"}),
		
		
		}

# class akun_form(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ['username','password']



class peminjaman_form(forms.ModelForm):
	class Meta:

		model = transaksi_peminjaman
		
		fields = ['judul_buku']
		labels = {

			'judul_buku':'Judul',

		}

		error_messages = {
			'judul_buku':{
				'required':'anda harus mengisi judul buku'
			},
		}
