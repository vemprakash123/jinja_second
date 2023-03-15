from django.shortcuts import render

# Create your views here.
def csk(request):
    d={'captian':'dhoni'}
    return render(request,'sample.html',d)