from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    is_done = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 