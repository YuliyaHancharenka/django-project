from django.test import TestCase
import datetime
from django.utils import timezone
from TechCourse.models import Allcourses, Details


# Create your tests here.

class AllcoursesModelTests(TestCase):

    def verify_future_course_date(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_course = Allcourses(started_from=time)
        self.assertIs(future_course.is_published_within_day(), False)

    def verify_old_course_date(self):
        time = timezone.now() - datetime.timedelta(days=1)
        old_course = Allcourses(started_from=time)
        self.assertIs(old_course.is_published_within_day(), False)

    def verify_recent_course_date(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59)
        recent_course = Allcourses(started_from=time)
        self.assertIs(recent_course.is_published_within_day(), True)