from django.shortcuts import render, HttpResponse
from django.db.models.functions import ExtractMonth, ExtractYear
from .models import slider, featuredpls, recentProj, Blogs
import datetime
from pytz import timezone
import calendar as c
# Create your views here.

def index(request):
    s1 = slider()
    s1.title1 = 'Harshad Lasgare'
    s1.title2 = 'coder'
    s1.desc = 'Tata communications'

    s2 = slider()
    s2.title1 = 'Rahul Lasgare'
#    s2.title2 = 'BE Electonics & Telecommunications'
    s2.title2 = 'gamer'
    s2.desc = 'helo world helo world helo world helo world helo world'
    s2.img = '/static/img/slider_1.jpg'

    s3 = slider()
    s3.title1 = 'Priya Lasgare'
    s3.title2 = 'instagrammer'
    s3.desc = 'helo world helo world helo world helo world helo world'

    sa = [s1, s2, s3]

    featurepls = featuredpls.objects.all()

    recentproj = recentProj.objects.all()

    blog = Blogs.objects.all().annotate(month=ExtractMonth('date'), year=ExtractYear('date'))
    tz = timezone('Asia/Kolkata')
    cd = datetime.datetime.now(tz)
    month_name = [c.month_name[cd.month+1], c.month_name[cd.month], c.month_name[cd.month-1], c.month_name[cd.month-2]]
    month_num = [cd.month+1, cd.month, cd.month-1, cd.month-2]

    return render(request, 'index.html', {'slider': sa, 'f1': featurepls, 'f2': recentproj, 'blog': blog, 'date': cd, 'month_num': month_num, 'month_name': month_name})

'''
def recentproj(request):
    recentpr = recentProj.objects.all()
    return render(request, 'index.html', {'f2': recentpr})
'''
