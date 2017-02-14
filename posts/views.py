from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .Forms import PostForm
from .models import Post
# Create your views here.

def post_create(request):
     form = PostForm()
     if request.method == "POST":
         print(request.POST.get("content"))
         title = request.POST.get("title")
         Post.objects.create(title = title)
     context = {
         "form":form,
     }
     return render(request, "post_form.html", context)

        #if request.user.is_authenticated():
     #	context = {
    #		"title": "My User List"
    # 	}
     #else:
      #  context = {
    	#	"title": "List"
       # }
     #return render(request, "index.html", context)

def post_detail(request, id): #retrieve
    instance = get_object_or_404(Post, id = id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)

def post_list(request):#list items
    queryset = Post.objects.all()
    context = {
        "object_list" : queryset,
        "title": "List"
    }
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>update</h1>")

def post_delete(request):
    return HttpResponse("<h1>delete</h1>")

