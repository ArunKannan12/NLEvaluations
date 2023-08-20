from django.db import models
from django.core.validators import RegexValidator
POINTS=RegexValidator(r'^[0-9]{}','only numbersare allowed')
from django.contrib.auth.models import User
# Create your models here.
APP_CATEGORY=(
    ('entertainment','entertainment'),
    ('shopping','shopping')
)
SUB_CATEGORY=(
    ('social media','social media'),
    ('online shopping','online shopping'),
    ('gaming','gaming')
)
class admin_task(models.Model):
    image=models.ImageField( upload_to='static/images/uploads', height_field=None, width_field=None, max_length=None)
    app_name=models.CharField( max_length=50)
    app_category=models.CharField(choices=APP_CATEGORY,max_length=50)
    sub_category=models.CharField(choices=SUB_CATEGORY, max_length=50)
    points=models.FloatField(null=True)
    def __str__(self):
        return self.app_name
    @property
    def imageURL(self):
        try:
            URL=self.image.url
        except:
            URL=""
        return URL
    
class UserPoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(admin_task, on_delete=models.CASCADE)
    points_earned = models.PositiveIntegerField(default=0)
    screenshot = models.ImageField(upload_to='static/images/screenshots/', blank=True, null=True)
    def __str__(self):
        return self.app.app_name
    