from django.db import models

# Create your models here.
class students(models.Model):
    sid=models.IntegerField(primary_key=True)
    grade=models.IntegerField()
    course=models.CharField()

class school (models.Model):
    school_id=models.IntegerField(primary_key=True)
    school_name=models.CharField(max_length=100)
    