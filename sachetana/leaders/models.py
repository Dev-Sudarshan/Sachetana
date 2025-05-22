from django.db import models
class Leader(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to='leaders/')
    province = models.CharField(max_length=200)  # Add province field

    def __str__(self):
        return self.name
    
class Promise(models.Model):
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE, related_name='promises')
    promise_text = models.TextField()
    date_made = models.DateField()
    fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return self.promise_text[:50] 

# Create your models here.
