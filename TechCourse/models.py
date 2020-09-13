from django.db import models
import datetime
from django.utils import timezone


class Allcourses(models.Model):
    coursename = models.CharField(max_length=200)
    insname = models.CharField(max_length=100)
    started_from = models.DateTimeField('Started from')

    def __str__(self):
        return self.coursename

    def is_published_within_day(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.started_from <= now


class Details(models.Model):
    course = models.ForeignKey(Allcourses, on_delete=models.CASCADE)
    course_type = models.CharField(max_length=500)
    is_interesting = models.BooleanField(default=False)

    def __str__(self):
        return str(self.course_type)
