
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.utils.text import slugify

class PostNews(models.Model):
	judul = models.CharField(max_length=50)
	isi = models.CharField(max_length=500)
	publish = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	slug = models.SlugField(blank=True ,editable=False)
	thumb = models.FileField(upload_to='documents/')
	def save(self):
		self.slug = slugify(self.judul)
		super(PostNews,self).save()
	def __str__(self):
		return '{}/{}'.format(self.id,self.judul)


class biodata(models.Model):

	JENIS_KELAMIN_CHOICE = {

		('Pria','pria'),
		('Wanita','wanita')
	}

	PILIH_STATUS_CHOICE = {

		('Bekerja','bekerja'),
		('Pelajar','pelajar'),
		('Mahasiswa','mahasiswa'),
		('Umum','umum')
	}

	nama = models.CharField(max_length = 100)
	jenis_kelamin = models.CharField(max_length = 15, choices = JENIS_KELAMIN_CHOICE)
	tgl_lahir = models.DateField()
	alamat = models.TextField()
	no_telepon = models.CharField(max_length=13)
	email = models.EmailField()
	status = models.CharField(max_length = 50, choices = PILIH_STATUS_CHOICE)
	foto_anggota = models.ImageField(upload_to = "upload/", null = True)


	

	def __unicode__(self):
		return self.nama
	def __str__(self):
		return "{}".format(self.nama)


class data_transaksi_peminjaman(models.Model):

	nama_peminjam = models.ForeignKey(biodata,on_delete=models.CASCADE)

	judul_buku = models.CharField(max_length = 100)
	tgl_buku_dipinjam = models.DateField(auto_now_add=True)
	tgl_buku_dikembalikan = models.DateField(null = True)
	status = models.BooleanField(default = False)
	denda = models.IntegerField(default=0)
	


	def __unicode__(self):
		return self.nama_peminjam.nama
	# def __init__(self, *args, **kwargs):
	# 	self.nama_peminjam = kwargs.pop('user')
	# 	super(data_transaksi_peminjaman, self).__init__(*args, **kwargs)


class transaksi_peminjaman(models.Model):


	nama_peminjam = models.ForeignKey(biodata,on_delete=models.CASCADE)
	judul_buku = models.CharField(max_length = 100)


	def __unicode__(self):
		return self.nama_peminjam.nama


class Akun_perpus(models.Model):

	akun = models.ForeignKey(User,related_name='akun',on_delete=models.CASCADE)
	anggota = models.ForeignKey(biodata,related_name='biodata',on_delete=models.CASCADE)

	def __unicode__(self):
		return self.anggota.nama


class kehadiran_anggota(models.Model):

	JENIS_ABSEN_CHOICE = {

		('masuk','Masuk'),
		('keluar','Keluar')
	}

	anggota = models.ForeignKey(biodata,on_delete=models.CASCADE)
	jenis_absen = models.CharField(max_length = 6, choices = JENIS_ABSEN_CHOICE)
	waktu = models.DateTimeField()

	def __unicode__(self):
		return anggota.nama






class data_buku(models.Model):

	JENIS_BUKU_CHOICE = {

		('Novel','novel'),
		('Cerpen','Cerpen'),
		('Majalah','majalah'),
		('Komik','komik'),
		('Manga','manga'),
		('Komputer','komputer'),
		('Sekolah','sekolah')
	}

	judul_buku = models.CharField(max_length = 100)
	jenis_buku = models.CharField(max_length = 50, choices = JENIS_BUKU_CHOICE)
	penulis = models.CharField(max_length = 50)
	tgl_terbit = models.DateField()
	penerbit = models.CharField(max_length = 50)
	jumlah_buku = models.IntegerField()
	def __unicode__(self):
		return self.judul_buku


class suplier_buku(models.Model):

	nama_suplier = models.CharField(max_length = 100)
	tgl_terima = models.DateField()
	alamat_suplier= models.TextField()
	judul_buku = models.CharField(max_length = 100)
	jumlah_buku = models.IntegerField()

	def __unicode__(self):
		self.nama_suplier


class penyumbang_buku(models.Model):

	nama_penyumbang = models.CharField(max_length = 100)
	tgl_terima = models.DateField()
	alamat_penyumbang= models.TextField()
	judul_buku = models.CharField(max_length = 100)
	jumlah_buku = models.IntegerField()

	def __unicode__(self):
		self.nama_penyumbang	

