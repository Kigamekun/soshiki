
from django.contrib import admin

# Register your models here.


from .models import *
from .forms import PostNewsForm
admin.site.register(PostNews)
import datetime

from .models import data_buku, suplier_buku, penyumbang_buku

# Register your models here.

class databuku_Admin(admin.ModelAdmin):
	list_display = ['judul_buku','jenis_buku','penulis','tgl_terbit','penerbit','jumlah_buku']
	list_filter = ['jenis_buku']
	search_fields = ['judul_buku','jenis_buku','penulis']
	list_per_page = 15

admin.site.register(data_buku, databuku_Admin)


class suplier_Admin(admin.ModelAdmin):
	list_display = ['nama_suplier','tgl_terima','alamat_suplier','judul_buku','jumlah_buku']
	#list_filter = []
	search_fields = ['nama_suplier']
	list_per_page = 15

admin.site.register(suplier_buku, suplier_Admin)


class penyumbang_Admin(admin.ModelAdmin):
	list_display = ['nama_penyumbang','tgl_terima','alamat_penyumbang','judul_buku','jumlah_buku']
	#list_filter = []
	search_fields = ['nama_penyumbag']
	list_per_page = 15

admin.site.register(penyumbang_buku, penyumbang_Admin) 






class biodata_Admin(admin.ModelAdmin):

	list_display = ['nama','jenis_kelamin','tgl_lahir','alamat','no_telepon','email','status']
	list_filter = ['status','jenis_kelamin']
	search_fields = ['nama','email','no_telepon']
	list_per_page = 15


admin.site.register(biodata, biodata_Admin)


class transaksi_peminjaman_Admin(admin.ModelAdmin):

	list_display = ['nama_peminjam','judul_buku']
	#list_filter = []
	search_fields = ['judul_buku']
	list_per_page = 15


admin.site.register(transaksi_peminjaman, transaksi_peminjaman_Admin)


class Akunperpus_Admin(admin.ModelAdmin):

	list_display = ['akun','anggota']
	#list_filter = []
	search_fields = ['akun','anggota']
	list_per_page = 15

admin.site.register(Akun_perpus, Akunperpus_Admin)



class peminjaman_Admin(admin.ModelAdmin):
	list_display = ['nama_peminjam','judul_buku','tgl_buku_dipinjam','tgl_buku_dikembalikan','status']
	#list_filter = []
	search_fields = ['nama_peminjam','judul_buku']
	list_per_page = 15

	actions = ['setuju_dipinjam','tidak_dipinjam']
	empty_value_display = 'Belum dikembalikan'


	def setuju_dipinjam(self, request, queryset):
		for pinjam in queryset:
		# 	diff = pinjam.tgl_buku_dikembalikan - pinjam.tgl_buku_dipinjam
		# 	base = pinjam.tgl_buku_dikembalikan
		# 	numdays = diff.days + 1
		# 	date_list = [base - datetime.timedelta(days = x)for x in range(0, numdays)]

			pinjam.status = True
			pinjam.save()

	#model save admin 
	def save_model(self, request, obj, form, change):
		datas = data_buku.objects.get(judul_buku=obj.judul_buku)
		databook = data_transaksi_peminjaman.objects.get(id=obj.id)
		
		

		# daftar_peminjam = data_transaksi_peminjaman.objects.all()
		
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

		

		if obj.tgl_buku_dikembalikan is not None :
			print('disini')
			tgl1 = list(map(int,str(obj.tgl_buku_dipinjam).split('-')))
			tgl2 = list(map(int,str(obj.tgl_buku_dikembalikan).split('-')))
			tg1 = datetime.date(tgl1[0],tgl1[1],tgl1[2])
			tg2 = datetime.date(tgl2[0],tgl2[1],tgl2[2])
			if tg1 == tg2 :
				pass
			else :
				solved = str(tg2 - tg1).split()
				y = int(solved[0])
					
					
				if y > 3 :
				
					x = 3000 * (y - 3)
					if obj.denda == x :
							 
						pass
					else :
						obj.denda = x
						
							
				
					obj.save()
					print("HEII INI DENDA",databook.denda)
			


		if databook.tgl_buku_dikembalikan is not None :
			obj.save()
		
		else :

			datas.jumlah_buku  = datas.jumlah_buku + 1
			datas.save()
			obj.save()

	setuju_dipinjam.short_description = "Setuju peminjaman yang dipilih"

	def tidak_dipinjam(self, request, queryset):
		queryset.update(status = False)

	tidak_dipinjam.short_description = "Batalkan peminjaman yang dipilih"


admin.site.register(data_transaksi_peminjaman, peminjaman_Admin)
