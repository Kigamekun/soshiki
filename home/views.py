
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
import datetime
import sys
from soshiki.settings import BASE_DIR
import os
from django.http import JsonResponse
from soshiki.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
#Post News

def index(request):
	posts = PostNews.objects.all()
	context = {
	'page_title':'HOME',
	'posts':posts,
	}
	paginator = Paginator(posts, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request,'home/index.html',context)

@login_required
def create(request):
	error = None
	
	forms = PostNewsForm(request.POST,request.FILES) 
	if request.method == 'POST':
		print(request.POST['judul'])
		
		if forms.is_valid():
			forms.save()
			messages.success(request, 'Data Created.')
			return redirect('home:index')
		else :
			return redirect('home:create')
	
	context = {
	"page_title":'CREATE',
	'forms':forms
	}
	return render(request,'home/create.html',context)


def loginView(request):
	context = {
	'page_title':'LOGIN',
	}
	if request.method == 'POST':
		user_log = request.POST['username']
		pass_log = request.POST['password']
		user = authenticate(request,username=user_log,password=pass_log)
		if user is not None:	
			if user.is_active:
				try:
					akun = Akun_perpus.objects.get(akun=user.id)
					login(request, user)

					request.session['anggota_id'] = akun.anggota.id
					request.session['username'] = request.POST['username']
					return redirect('home:index')

				except:
					messages.add_message(request, messages.WARNING, 'Akun ini belum terhubung dengan data anggota, silahkan hubungi administartor')
					return redirect('home:login')

			else:
				messages.add_message(request, messages.WARNING, 'User belum terverifikasi')

		else:
			messages.add_message(request, messages.WARNING, 'Username atau password Anda salah')

	return render(request, 'home/login.html')

	if request.method == 'GET':
		if request.user.is_authenticated():
			return redirect('home:index')

		else :
			return render(request,'home/login.html',context)


def logoutView(request):
	context = {
	'page_title':'LOGOUT',
	}
	if request.method == "POST":

		if request.POST['logout'] =='Submit Query' or 'submit':
			logout(request)

		return redirect('home:index')
	else :
		redirect("home:index")
		
	return render(request,'home/logout.html',context)


def register(request):
	forms = CreateUser(request.POST)
	context = {
	'page_title':'REGISTER',
	'forms':forms,

	}

	if request.method == 'POST':
		print("disini")
		if forms.is_valid():
			new_user = User.objects.create_user(username=forms.cleaned_data['username'],email= forms.cleaned_data['email'],password=forms.cleaned_data['password1'])
			print("Success No Error")
			#send_mail('Welcome to KigameKun Corps','I Hope You enjoy in this website', EMAIL_HOST_USER, [forms.cleaned_data['email']], fail_silently = False)
			return redirect('home:register_bio')
		else :
			print("Have A Error")
			print(forms.errors)

	return render(request,'home/register.html',context)


def detail(request,slugInput):
	posts = PostNews.objects.get(slug=slugInput)
	
	context = {
	'judul':'Detail',
	'contents':'BLOG AREA',
	'posts':posts,

	}
	return render(request,'home/detail.html',context)


@login_required
#@user_passes_test(lambda user:Group.objects.get(name='Guru') in user.groups.all())
def delete(request,delete_id):
	PostNews.objects.filter(id=delete_id).delete()
	messages.success(request, 'Data Deleted.')
	return redirect('home:index')

@login_required
#@user_passes_test(lambda user:Group.objects.get(name='Guru') in user.groups.all())
def update(request,update_id):
	news_update = PostNews.objects.get(id=update_id)
	data = {
	'judul':news_update.judul,	
	}

	forms = PostNewsForm(request.POST or None,initial= data,instance=news_update)
	if request.method == 'POST':
		if forms.is_valid():
			messages.success(request, 'Data Updated.')
			forms.save()
			return redirect('home:index')
	context = {
	'page_title':'Update',
	'forms':forms,
	}
	return render(request,'home/create.html',context)

def forgot_password(request):
    if request.method == 'POST':
        return password_reset(request, 
            from_email=request.POST.get('email'))
    else:
        return render(request, 'home/forgot_password.html')



#END POST NEWS



#AWAL LIBRARY

def tampil_tabel(request):
	#data buku

	daftar_buku = data_buku.objects.all()

	#pagination
	paginator = Paginator(daftar_buku, 10)
	page = request.GET.get('page')
	try:
		daftar_buku = paginator.page(page)
	except PageNotAnInteger:
		daftar_buku = paginator.page(1)
	except EmptyPage:
		daftar_buku = paginator.page(paginator.num_pages)

	#daftar peminjam buku
	daftar_pinjam = data_transaksi_peminjaman.objects.all()

	#pagination
	paginator = Paginator(daftar_pinjam, 5)
	page = request.GET.get('page')
	try:
		daftar_pinjam = paginator.page(page)
	except PageNotAnInteger:
		daftar_pinjam = paginator.page(1)
	except EmptyPage:
		daftar_pinjam = paginator.page(paginator.num_pages)
	
	return render(request, "home/tampil_tabel.html",{'daftar_buku':daftar_buku,'daftar_pinjam':daftar_pinjam,'daftar_suplier':daftar_suplier,'daftar_penyumbang':daftar_penyumbang})


def daftar_buku(request):
    daftar_buku  = data_buku.objects.all()
    data = ""
    company = ''
    if request.method == "POST":
          
        try:
            excel_file = request.FILES["fl"]
        except MultiValueDictKeyError:
            return HttpResponse('Salah')
    
        if (str(excel_file).split(".")[-1] == "xls"):
            data = xls_get(excel_file, column_limit=13)
        elif (str(excel_file).split(".")[-1] == "xlsx"):
            data = xlsx_get(excel_file, column_limit=13)
        else:
            print("salah")
       

        key = ''.join(data.keys())
        solve = data[key]
        solved = 0
        for i in range(len(solve)):
            if len(solve[i]) != 0 :
                solved += 1
            else :
                pass
            
        for i in range(1,solved):
            try :
                data_buku.objects.create(judul_buku=solve[i][1],jenis_buku=solve[i][2],penulis=solve[i][3],tgl_terbit=solve[i][4],penerbit=solve[i][5],jumlah_buku=solve[i][6])
                messages.add_message(request, messages.INFO, 'Buku berhasil ditambahkan')
                return redirect('home:daftar_buku')
            except:
                messages.add_message(request, messages.WARNING, 'Buku gagal ditambahkan')
                return redirect('home:daftar_buku')
    return render(request, 'home/daftar_buku.html',{'daftar_buku':daftar_buku})




def down_file(request):
   
    path = os.path.join(str(BASE_DIR)+'/templates/', 'format.xlsx')

   
    with open(path, 'rb') as model_excel:
        result = model_excel.read()
    response = HttpResponse(result)
    response['Content-Disposition'] = 'attachment; filename=format.xlsx'
    return response


@login_required
def daftar_peminjam(request):

	daftar_peminjam = None
	# obj = data_transaksi_peminjaman.objects.get(id = 1)
	# print(obj)
	if request.method == 'POST':

		daftar_peminjam = data_transaksi_peminjaman.objects.filter(judul_buku = request.POST['judul_buku'])
		
	else:
		daftar_peminjam = data_transaksi_peminjaman.objects.all()
			
		# for i in daftar_peminjam:
		# 	field_name = 'tgl_buku_dipinjam'
		# 	obj =data_transaksi_peminjaman.objects.first()
		# 	field_value = getattr(obj, field_name)
		# 	print("WOOEEEE",field_value)
		
		# for pinjam in daftar_peminjam:
		# 	if pinjam.tgl_buku_dikembalikan is not None :
		# 		datas = data_buku.objects.get(judul_buku=pinjam.judul_buku)
				
		# 		tgl1 = list(map(int,str(pinjam.tgl_buku_dipinjam).split('-')))
		# 		tgl2 = list(map(int,str(pinjam.tgl_buku_dikembalikan).split('-')))
		# 		tg1 = datetime.date(tgl1[0],tgl1[1],tgl1[2])
		# 		tg2 = datetime.date(tgl2[0],tgl2[1],tgl2[2])
		# 		if tg1 == tg2 :
		# 			pass
		# 		else :
		# 			solved = str(tg2 - tg1).split()
		# 			y = int(solved[0])
					
					
		# 			if y > 3 :
				
		# 				x = 3000 * (y - 3)
		# 				if pinjam.denda == x :
							 
		# 					pass
		# 				else :
		# 					pinjam.denda = x
						
							
				
		# 				pinjam.save()
		# 			print("HEII INI DENDA",pinjam.denda)
			
		# 	else :
		# 		print(pinjam.judul_buku," belum dikembalikan")

		#pagination
		paginator = Paginator(daftar_peminjam, 10)
		page = request.GET.get('page')
		try:
			daftar_peminjam = paginator.page(page)
		except PageNotAnInteger:
			daftar_peminjam = paginator.page(1)
		except EmptyPage:
			daftar_peminjam = paginator.page(paginator.num_pages)

	return render(request, 'home/daftar_peminjam.html',{'daftar_peminjam':daftar_peminjam})

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
	anggota = biodata.objects.get(id=request.session['anggota_id'])

	return render(request,'home/profil.html', {'anggota':anggota})

@login_required(login_url=settings.LOGIN_URL)
def ganti_foto(request):
	anggota = biodata.objects.get(id=request.session['anggota_id'])
	anggota.foto_anggota = request.FILES['files']
	anggota.save()

	return redirect('home:profile')


def fail(request):
	return render(request,'home/fail.html')

def success(request):
	return render(request,'home/success.html')


def empty(request):
	return render(request,'home/empty.html')

@login_required(login_url=settings.LOGIN_URL)
def peminjaman_buku(request):
	if 'term' in request.GET:
		qs = data_buku.objects.filter(judul_buku__istartswith=request.GET.get('term'))
		title = list()
		for tit in qs:
			title.append(tit.judul_buku)
		return JsonResponse(title,safe=False)
	if request.method == 'POST':
		form_data = request.POST
		
		form = peminjaman_form(form_data)
		
		if form.is_valid():
			
			pinjam = data_transaksi_peminjaman(

				nama_peminjam = biodata.objects.get(id = request.session['anggota_id']),
				judul_buku = request.POST['judul_buku'],

				)
			pinjam1 = transaksi_peminjaman(

				nama_peminjam = biodata.objects.get(id = request.session['anggota_id']),
				judul_buku = request.POST['judul_buku'],

				)
			data = data_buku.objects.filter(judul_buku= request.POST['judul_buku'])
			datafilt = data_buku.objects.filter(judul_buku= request.POST['judul_buku']).values_list('jumlah_buku',flat=True)
			
			if data.exists() :
				datas = data_buku.objects.get(judul_buku=request.POST['judul_buku'])
		
				if datafilt[0] != 0:
					
					datas.jumlah_buku = datas.jumlah_buku - 1
				
					datas.save()
					pinjam.save()
					pinjam1.save()
					return redirect('home:success')
				else :
					return redirect('home:empty')

				
				
			else :
				return redirect('home:fail')
							
	else:
		form = peminjaman_form()
		

	return render(request,'home/form_peminjaman.html',{'form':form})


@login_required(login_url = settings.LOGIN_URL)
def tampil_buku_dipinjam(request):

	#daftar buku yang dipinjam

	daftar_buku_dipinjam = data_transaksi_peminjaman.objects.filter(nama_peminjam__id = request.session['anggota_id'])

	#pagination
	paginator = Paginator(daftar_buku_dipinjam, 5)
	page = request.GET.get('page')
	try:
		daftar_buku_dipinjam = paginator.page(page)
	except PageNotAnInteger:
		daftar_buku_dipinjam = paginator.page(1)
	except EmptyPage:
		daftar_buku_dipinjam = paginator.page(paginator.num_pages)


	#daftar history buku

	history_buku_pinjam= transaksi_peminjaman.objects.filter(nama_peminjam__id = request.session['anggota_id'])

	#pagination
	paginator = Paginator(history_buku_pinjam, 5)
	page = request.GET.get('page')
	try:
		history_buku_pinjam = paginator.page(page)
	except PageNotAnInteger:
		history_buku_pinjam = paginator.page(1)
	except EmptyPage:
		history_buku_pinjam = paginator.page(paginator.num_pages)

	return render(request,'home/daftar_buku_dipinjam.html',{'daftar_buku_dipinjam':daftar_buku_dipinjam,'history_buku_pinjam':history_buku_pinjam})


def register_bio_view(request):
	if request.method == 'POST':
		
		form_data = request.POST
		form = anggota_form(form_data)


		if form.is_valid():
			day = request.POST['tgl_lahir_day']
			month = request.POST['tgl_lahir_month']
			year = request.POST['tgl_lahir_year']
			solve = year+'-'+month+'-'+day			
			bio = biodata(

				nama = request.POST['nama'],
				jenis_kelamin = request.POST['jenis_kelamin'],
				tgl_lahir = solve,
				alamat = request.POST['alamat'],
				no_telepon = request.POST['no_telepon'],
				email = request.POST['email'],
				status = request.POST['status'],
				
				)
			bio.save()

			return redirect('home:login')
	else:
		form = anggota_form()

	return render(request, 'home/register.html',{'forms':form})


#END LIBRARY


#HANDLE ERROR
def handler404(request, exception):
    context = {}
    response = render(request, "pages/errors/404.html", context=context)
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    context = {}
    response = render(request, "pages/errors/500.html", context=context)
    response.status_code = 500
    return response

#END ERROR


#NOTIF


# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['to@example.com'],
#     fail_silently=False,
# )
