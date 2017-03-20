# -*- coding: utf-8 -*-
from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo


def home(request):
    photos = Photo.objects.all().order_by('-created_at')
    context ={
        'photos_list': photos[:5]
    }
    return render(request, 'photos/home.html', context)

def detail(request, pk):
    """
    Carga la pagina de detalle de una foto
    :param request: HttpRequest
    :param pk: id de la foto
    :return: HttpREsponse
    """
    possible_photos = Photo.objects.filter(pk=pk)
    photo = possible_photos[0] if len(possible_photos) == 1 else None
    if photo is not None:
        context = {
            'photo': photo
        }
        return render(request, 'photos/datail.html', context )
    else:
        return HttpResponseNotFound()

