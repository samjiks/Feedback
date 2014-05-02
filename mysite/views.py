from django.http import HttpResponse

def hello(request):
	
	return HttpResponse("<H3>Hello World</H3>")