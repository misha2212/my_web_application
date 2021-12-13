from django.db import models


class BaseImages(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images_dir/%Y/%m/%d/")

    def __str__(self):
        return self.title
