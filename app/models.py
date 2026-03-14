from django.db import models

class Empolyee(models.Model):

    DEPARTMENT_CHOICES = [
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Finance', 'Finance'),
        ('Sales', 'Sales'),
    ]

    name = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    email = models.EmailField()

    def __str__(self):
        return self.name