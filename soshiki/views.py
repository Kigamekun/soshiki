from django.shortcuts import render,redirect



def index(request):
	context = {
	'page_title':'HOME',
	'posts':'post',

	}

	return render(request,'index.html',context)


def error404(request):
	return render(request,'home/404.html')


def about(request):
	context = {
	'page_title':'AboutMe',
	}

	return render(request,'about.html',context)


