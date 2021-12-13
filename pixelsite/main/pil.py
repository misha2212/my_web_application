from PIL import Image
from main.models import BaseImages


data = BaseImages.objects.all()
direct = str(data[4].image)
SOURCE_DIR = 'C:/Users/Настя/Desktop/29_11_21/pixelsite/media/'
img = Image.open(SOURCE_DIR + direct)


# '/images_dir/2021/12/08/elektrika.jpg'
# C:/Users/Настя/Desktop/29_11_21/pixelsite/media/

# SOURCE_DIR = '../media/'