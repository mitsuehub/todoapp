from django.db import models

class Todo(models.Model):
    do = models.CharField(max_length=50)
    
    def __str__(self):
        return self.do

class DoneTable(models.Model):
    done = models.CharField(max_length=50)
    donetime = models.CharField(max_length=50)
    
    def __str__(self):
        return self.done