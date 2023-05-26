from django.shortcuts import render
from .models import blog

# Create your views here.
def blog(request):


    return render(request,'blog/blog.html')

