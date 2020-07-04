from PIL import Image
from django.db import models
from django.core.validators import RegexValidator
from .furn_types import FURNITURE_CHOICES
from .condition_type import CONDITION_CHOICES
from .category_types import CATEGORY_CHOICES

# Create your models here.
class Furniture(models.Model):
    furniture_name      = models.CharField(max_length=100, default="Coffee Table")
    furniture_type      = models.CharField(choices=FURNITURE_CHOICES, max_length=2, default="Table")
    category            = models.CharField(choices=CATEGORY_CHOICES ,max_length=2)
    seller              = models.CharField(max_length=100)
    phone_regex         = RegexValidator(regex = r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered int the format: '+254700000000'. Up to 14 digits allowed.")
    phone_number        = models.CharField(validators=[phone_regex], max_length=15, null=True, blank=True)
    photo               = models.ImageField(default='feature_2.png',upload_to='furniture_images')
    price               = models.FloatField()
    condition           = models.CharField(choices=CONDITION_CHOICES, max_length=2)


    def __str__(self):
        return f"{self.furniture_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        #Setting Size
        new_size = (263, 280)
        img.thumbnail(max_size, Image.ANTIALIAS)
        img.save(self.image.path)


