
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.conf.urls import handler404
from django.views.static import serve 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('media/<path>.*', serve,{'document_root': settings.MEDIA_ROOT}), 
	# path('static/<path>.*', serve,{'document_root': settings.STATIC_ROOT}), 
    path('home/', include(('home.urls', 'home'), namespace='home')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    #path('data/', include(('data.urls', 'data'), namespace='data')),
    path('kisara/', include(('kisara.urls', 'kisara'), namespace='kisara')),
    path('about/',views.about,name="about"),
    path('',views.index,name="index"),


]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
