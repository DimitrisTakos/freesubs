from django.utils import timezone
from .models import Post, Old, Mov, Tato
from .models import Cheatsheet
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def base(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'movie/base.html', {'posts': posts})


def download_cheatsheet(request, cheatsheet_id):
    cheatsheet = get_object_or_404(Cheatsheet, pk=cheatsheet_id)
    file_path = cheatsheet.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{cheatsheet.title}"'
    return response


def cheatsheet(request):
    files = Cheatsheet.objects.all()
    print(files)
    context = {
        'files': files
    }
    return render(request, 'movie/base.html', context)


def page2(request):
    return render(request, 'movie/second_page.html', {})


def wildcards(request):
    return render(request, 'movie/third_page.html', {})


def season_1_wildcards(request):
    cards = Old.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'movie/fourth_page.html', {'cards': cards})


def movies2024(request):
    movies = Mov.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'movie/fifth_page.html', {'movies': movies})

def thetattooist(request):
    tattoos = Tato.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'movie/sixth_page.html', {'tattoos': tattoos})

def thewayhome(request):
    return render(request, 'movie/seventh_page.html',{})