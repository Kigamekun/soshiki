from django.conf.urls import url


from . import views


urlpatterns = [
	url(r'^datasiswa/$',views.student,name='dataSiswa'),
	url(r'^dataguru/$',views.teacher,name='dataGuru'),
]