from django.db import models


class Project(models.Model):
    thumb_image = models.ImageField(upload_to='img', null = True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='img', null = True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
class TimeLine(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Note(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    date = models.DateTimeField('date written')
    note = models.CharField(max_length=2000)
