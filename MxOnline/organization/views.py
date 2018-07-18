from django.shortcuts import render
from django.views.generic.base import View
from .models import CityDict, CourseOrg, Teacher
from django.core.paginator import Paginator
# Create your views here.


class OrgView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        category = request.GET.get('ct', '')
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")
        if category:
            all_orgs = all_orgs.filter(category=category)
        all_citys = CityDict.objects.all()
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        org_onums = all_orgs.count()
        paginator = Paginator(all_orgs, 2)
        page_num = request.GET.get('page', 1)
        page_of_org = paginator.get_page(page_num)
        return render(request, 'org-list.html', {
            'all_orgs': page_of_org,
            'org_onums': org_onums,
            'all_citys': all_citys,
            'city_id': city_id,
            'hot_orgs': hot_orgs
        })