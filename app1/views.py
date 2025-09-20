from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'sample1.html')

def index(request):

    return render(request, 'app1/index.html')