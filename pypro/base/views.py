from django.http import HttpResponse


# Create your views here.
def home(request):
    raise ValueError()
    return HttpResponse('<html><body>Olá</body></html>', content_type='text/html')
