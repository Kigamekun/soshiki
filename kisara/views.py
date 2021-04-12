from django.shortcuts import render,redirect


from .models import kotakSurat
from .forms import kotakSuratForm
# Create your views here.

def index(request):
	posts = kotakSurat.objects.all()
	context = {
	'page_title':'KISARA !!!',
	'posts':posts

	}
	return render(request,'kisara/index.html',context)

def create(request):
	forms = kotakSuratForm(request.POST)
	context = {
	'page_title':'Create KISARA',
	'forms':forms,
	}
	if request.method == 'POST':
		if forms.is_valid():
			forms.save()
			return redirect('kisara:kisara')

	return render(request,'kisara/create.html',context)
