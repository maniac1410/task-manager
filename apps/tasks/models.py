from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    
    class Priority_Choices(models.IntegerChoices):
        URGENT = 1 , 'Urgent'
        HIGH = 2, 'High'
        MEDIUM = 3, 'Medium'
        LOW = 4, 'Low'
        
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=Priority_Choices, default=Priority_Choices.HIGH)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        
        
