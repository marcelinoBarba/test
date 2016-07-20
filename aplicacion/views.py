from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404, redirect
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
# Create your views here.
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

@login_required
def crear_post(request):
	form=PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.save()
		messages.success(request, 'Fue creado exitosamente')
		return HttpResponseRedirect('/post/')
	context = {
		"form":form,
	}
	return render (request,"form_post.html",context)

@login_required
def actualizar_post(request, id=None):
	query = get_object_or_404(Post, pk=id)
	form=PostForm(request.POST or None,request.FILES or None,instance=query)
	if form.is_valid():
		post = form.save(commit=False)
		post.save()
		messages.success(request, 'Fue Editado Correctamente')
		return HttpResponseRedirect('/post/')
	context = {
		'detalle':query,
		'form': form,
	}
	return render (request,"form_post.html",context)

@login_required
def post_home(request):
    saludo="hola"
    print "hola mundo!"
    context={
        "saludo":saludo,
    }
    return render(request,"index.html", context)

@login_required
def lista_post(request):
	query_list = Post.objects.all().order_by("-creado")
	paginator = Paginator(query_list, 5) # Show 5 contacts per page
	page = request.GET.get('page')
	try:
	    query = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    query = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    query = paginator.page(paginator.num_pages)
	saludo = "Contenido"
	print "hola mundo!"
	context = {
		"lista":query,
		"saludo":saludo,	
		}
	return render(request,"post.html",context)

@login_required
def detalle_post(request, id = None):
	query = get_object_or_404(Post, pk=id)
	context = {
		"detalle":query
	}
	return render(request, "detalle.html", context)
@login_required
def borrar_post(request, id=id):
	query=get_object_or_404(Post, pk=id)
	query.delete()
	messages.success(request, 'Fue Eliminado Correctamente')
	return redirect("/post/")
