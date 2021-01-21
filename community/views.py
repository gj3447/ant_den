from django.shortcuts import render
from .models import Post

def index(request):
    postList = Post.objects.order_by('-date')
    context = {'postList':postList}
    return render(request,'header/index.html',context)
# Create your views here.
