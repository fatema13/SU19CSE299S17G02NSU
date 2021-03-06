from django.contrib.auth.models import User
from PIL import Image
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

#folowing model keeps user's list of books read
class MyLibraryList(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE,default='', null=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    bling = models.CharField(max_length=100, default='', null=True)

def __str__(self):
    return self.name



