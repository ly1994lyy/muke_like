from django.shortcuts import render
from django.views.generic import View
from .models import Course
from django.core.paginator import Paginator
# Create your views here.


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all().order_by('-add_time')
        hot_courses = Course.objects.all().order_by('-click_nums')[:3]
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'student':
                courses = Course.objects.all().order_by('-students')
            elif sort == 'hot':
                courses = Course.objects.all().order_by('-click_nums')
        page_nums = request.GET.get('page', 1)
        paginator = Paginator(courses, 3)
        all_courses = paginator.get_page(page_nums)
        context = {}
        context['all_courses'] = all_courses
        context['sort'] = sort
        context['hot_courses'] = hot_courses
        return render(request, 'course-list.html', context)