from django.db import models

def upload_path(instance, filename):
    return '/media/'.join([filename])



class Book(models.Model):
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)
    print("cover, uploadpath")
    print(cover , upload_path)