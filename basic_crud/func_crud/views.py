from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Crud
from .form import createForm
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    cruds = Crud.objects

    posts = Crud.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    page_numbers_range = 10

    max_index = len(paginator.page_range)
    current_page = int(page) if page else 1
    start_index = int((current_page -1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range

    if end_index >= max_index:
        end_index = max_index
    paginator_range = paginator.page_range[start_index:end_index]

    return render(request, 'home.html', {'cruds': cruds, 'posts': posts, 'paginator_range': paginator_range})

def createPage(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = createForm()
        return render(request, 'create.html', {"form": form})


def createFunction(request):
    cruds = Crud()
    cruds.title = request.POST.get('title', False)
    cruds.description = request.POST.get('description', False)
    cruds.src = request.FILES.get('photo', False)
    cruds.save()
    messages.info(request, 'ADD')
    return redirect('homePage')


def updatePage(request, update_id):
    update = get_object_or_404(Crud, pk=update_id)
    form = createForm()
    return render(request, 'update.html', {'content': update, "form": form})


def updateFunction(request, update_id):
    update = get_object_or_404(Crud, pk=update_id)
    if request.method == "POST":
        update.title = request.POST.get('title', False)
        update.description = request.POST.get('description', False)
        update.src = request.FILES.get('photo', False)
        update.save()
        messages.info(request, 'UPDATE')
        return redirect('homePage')


def deleteFunction(request, delete_id):
    crud = get_object_or_404(Crud, pk=delete_id)
    if request.method == "GET":
        crud.delete()
        messages.info(request, 'DELETE')
        return redirect('homePage')
    else:
        pass

def detailPage(request, detail_id):
    detail = get_object_or_404(Crud, pk=detail_id)
    return render(request, 'detail.html', {'detail': detail})
