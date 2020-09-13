from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.template import loader

from TechCourse.models import Allcourses


def course(request):
    ac = Allcourses.objects.all()
    template = loader.get_template('TechCourse/Courses.html')
    context = {
        'ac': ac,
    }
    return HttpResponse(template.render(context, request))


def detail(request, course_id):
    course = get_object_or_404(Allcourses, pk = course_id)
    return render(request, 'TechCourse/detail.html', {'course': course})

def is_interesting(request, course_id):
    course = get_object_or_404(Allcourses, pk = course_id)
    try:
        selected_course_type = course.details_set.get(pk=request.POST['interest'])
    except (KeyError, Allcourses.DoesNotExist):
        return render(request, 'TechCourse/detail.html', {
            'course': course,
            'error_message': 'Select a valid option'
        })
    else:
        selected_course_type.is_interesting = True
        selected_course_type.save()
        return render(request, 'TechCourse/detail.html', {'course': course})


