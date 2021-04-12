from django.urls import path

from . import views
urlpatterns = [
	path('',views.index,name='kisara'),
	path('create/',views.create,name='create'),

]