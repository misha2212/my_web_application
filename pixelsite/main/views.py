from PIL import Image, ImageColor
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
    data_1 = BaseImages.objects.last()
    direct = str(data_1.image)
    SOURCE_DIR = 'media/'
    img = Image.open(SOURCE_DIR + direct)
    black = 0
    white = 0
    result = ''
    for pixel in img.getdata():
        if pixel == (0, 0, 0):
            black += 1
        if pixel == (255, 255, 255):
            white += 1
    if white > black:
        result = 'белых пикселей больше, чем черных'
    elif white < black:
        result = 'белых пикселей меньше, чем черных'
    return render(request, 'main/pix.html', {'white': white, 'black': black, 'result': result})


def hex(request):
    if request.method == 'POST':
        a = request.POST.__getitem__('hexi')
        data_1 = BaseImages.objects.last()
        direct = str(data_1.image)
        SOURCE_DIR = 'media/'
        img = Image.open(SOURCE_DIR + direct)
        color = 0
        b = ImageColor.getrgb(a)
        print(b)
        for pixel in img.getdata():
            if pixel == b:
                color += 1
        print(color)
    else:
        a = ''
        color = ''
    return render(request, 'main/hex.html', {'a': a, 'color': color})


def learn(request):
    return render(request, 'main/learn.html',)
