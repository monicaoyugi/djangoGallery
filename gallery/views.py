from django.shortcuts import render

from .models import Image

def index(request):
    images = Image.objects.all()
    return render(request,'index.html',{"images":images})


def search_results(request):
    if 'image' in request.Get and request.Get["image"]:
        search_term = request.GET.get("image")
        searched_Images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,'gallery/search.html',{"message": massage,"Images": searched_Images})

    else:
        message = " You didn't search for anything."
        return render(request,'gallery/search.html',{"message":message})

def search_location(request,location):
    images_by_location = Image.filter_by_location(location)

    return render(request,'gallery/location.html',{"images":images_by_location})

def search_image(request,pic):
    images_by_location = Image.get_image_by_id(pic)

    return render(request,'location.html',{"images":images_by_location})






