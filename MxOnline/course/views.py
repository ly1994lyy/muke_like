from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Course
from django.core.paginator import Paginator
from operation.models import UserFavorite
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


class CourseDetailView(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        course.click_nums += 1
        course.save()
        has_fav_course = False
        has_fav_org = False

        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True
        tag = course.tag
        if tag:
            # 需要从1开始不然会推荐自己
            relate_courses = Course.objects.filter(tag=tag)[:3]
        else:
            relate_courses = []
        context = {}
        context['course'] = course
        context['relate_courses'] = relate_courses
        context['has_fav_course'] = has_fav_course
        context['has_fav_org'] = has_fav_org
        return render(request, 'course-detail.html', context)