from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)


    def __str__(self):
        return self.first_name