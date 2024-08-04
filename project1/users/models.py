from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from PIL import Image # type: ignore
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self) -> str:
        return f"{self.user.username} Profile \n {self.bio}"
    
    '''def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)'''