from django.db import models

# Create your models here.


class Todo(models.Model):
    tid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return f"{self.title[:7]}({self.tid})"