from PIL import Image
from django.shortcuts import render, redirect

from main.forms import AddPostForm
from main.models import BaseImages


def index(request):
    data = BaseImages.objects.all()
    return render(request, 'main/index.html', {'data': data})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # try:
                # BaseImages.objects.create(**form.cleaned_data)
            form.save()
            return redirect('home')
            # except:
            #     form.add_error(None, 'Ошибка добавления в базу')
    else:
        form = AddPostForm()
    return render(request, 'main/addpage.html', {'form': form})


def pix(request):
    data_1 = BaseImages.objects.all()
    direct = str(data_1[6].image)
    SOURCE_DIR = 'C:/Users/Настя/Desktop/29_11_21/pixelsite/media/'
    img = Image.open(SOURCE_DIR + direct)
    black = 0
    white = 0
    grey = 0
    other = 0
    for pixel in img.getdata():
        if pixel == (0, 0, 0):
            black += 1
        if pixel == (255, 255, 255):
            white += 1
        if pixel == (128, 128, 128):
            grey += 1
        else:
            other += 1
    return render(request, 'main/pix.html', {'white': white})

