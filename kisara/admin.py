from django.contrib import admin

# Register your models here.
from .models import kotakSurat
from .forms import kotakSuratForm


admin.site.register(kotakSurat)