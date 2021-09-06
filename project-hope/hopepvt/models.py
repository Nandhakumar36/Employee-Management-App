from django.db import models

# Create your models here.

class Employee(models.Model):
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    eid = models.CharField(max_length=30, blank=True, null=True)
    skill1 = models.CharField(max_length=30, blank=True, null=True)
    skill2 = models.CharField(max_length=30, blank=True, null=True)
    skill3 = models.CharField(max_length=30, blank=True, null=True)
    skill4 = models.CharField(max_length=30, blank=True, null=True)
    skilll5 = models.CharField(max_length=30, blank=True, null=True)
    skillpercentage1 = models.CharField(max_length=5, blank=True, null=True)
    skillpercentage2 = models.CharField(max_length=5, blank=True, null=True)
    skillpercentage3 = models.CharField(max_length=5, blank=True, null=True)
    skillpercentage4 = models.CharField(max_length=5, blank=True, null=True)
    skillpercentage5 = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'employee'


class Manager(models.Model):
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    mid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'manager'
