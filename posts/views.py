from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request

from .Forms import PostForm
from .models import Post
# Create your views here.

def post_create(request):
     form = PostForm(request.POST or None)
     if form.is_valid():
         instance = form.save(commit=False)
         print(form.cleaned_data.get("title"))
         instance.save()
         return HttpResponseRedirect(instance.get_absolute_url())
     # if request.method == "POST":
     #     print(request.POST.get("content"))
     #     title = request.POST.get("title")
     #     Post.objects.create(title = title)
     context = {
         "form":form,
     }
     return render(request, "post_form.html", context)

     # if request.user.is_authenticated():
     # 	context = {
    	# 	"title": "My User List"
    	# }
     # else:
     #   context = {
    	# 	"title": "List"
     #   }
     # return render(request, "index.html", context)

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

def post_update(request, id = None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        #message success
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,

    }
    return render(request, "post_form.html", context)

def post_delete(request):
    return HttpResponse("<h1>delete</h1>")

