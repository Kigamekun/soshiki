from django.urls import path,include
from django.contrib import admin
from django.conf.urls import handler404,handler500
from . import views
from django.views.defaults import page_not_found
from django.conf import settings
from django.views.static import serve 
import django.views.defaults
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('delete/<delete_id>',views.delete , name="delete"),
    path('update/<update_id>',views.update , name="update"),
    path('detail/<slugInput>',views.detail),
    path('',views.index,name='index'),
    
    path('create/',views.create,name='create'),
    path('login/',views.loginView,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutView,name='logout'),

	 
    #path('404/', views.error404),

    path('profile/',views.profil,name='profile'),
    path('profile/ganti_foto/',views.ganti_foto,name='ganti_foto'),
    path('register_bio/', views.register_bio_view ,name="register_bio"),
    path('pinjam_buku/',views.peminjaman_buku,name="pinjam"),
    path('daftar_pinjam_buku/',views.tampil_buku_dipinjam,name="databuku"),
    path('fail/',views.fail,name="fail"),
    path('success/',views.success,name="success"),
    path('empty/',views.empty,name="empty"),
    path('down_file/',views.down_file,name="down_file"),
  


    path('tampil_tabel/', views.tampil_tabel,name='data_buku'),   
    path('daftar_buku/', views.daftar_buku, name ='daftar_buku'),
    path('daftar_peminjam/', views.daftar_peminjam, name ='daftar_peminjam'),

  #url(r'^tampil_tabel/$', views.tampil_tabel,name='data_buku'), 
  #url(r'^daftar_suplier/', views.daftar_suplier_buku, name ='suplier'),
  #url(r'^daftar_penyumbang/', views.daftar_penyumbang_buku, name ='penyumbang'),


]


handler404 = 'home.views.handler404'

handler500 = 'home.views.handler500'

