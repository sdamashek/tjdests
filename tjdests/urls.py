# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""tjdests URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from destinations import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^accounts/login/$', views.login_view),
    url(r'^register$', views.register_view, name='register'),
    url(r'^verify/(?P<verify_key>[\w-]+)?$', views.verify_view, name='verify'),
    url(r'^update$', views.update_view, name='update'),

    url(r'^update/schools$', views.update_schools_view, name='update_schools'),
    url(r'^update_school$', views.update_school_view, name='update_school'),
    url(r'^update_school/(?P<app_id>\d+)?$', views.update_school_view, name='update_school'),

    url(r'^update/apexams$', views.update_apexams_view, name='update_apexams'),
    url(r'^update_apexam$', views.update_apexam_view, name='update_apexam'),
    url(r'^update_apexam/(?P<exam_id>\d+)?$', views.update_apexam_view, name='update_apexam'),

    url(r'^update/sat2s$', views.update_sat2s_view, name='update_sat2s'),
    url(r'^update_sat2$', views.update_sat2_view, name='update_sat2'),
    url(r'^update_sat2/(?P<exam_id>\d+)?$', views.update_sat2_view, name='update_sat2'),
    

    url(r'^students$', views.students_view, name='students'),
    url(r'^colleges$', views.colleges_view, name='colleges'),
    url(r'^destinations$', views.destinations_view, name='destinations'),
    url(r'^student/(?P<student_id>\d+)?$', views.student_view, name='student'),
    url(r'^college/(?P<college_ceeb>[\w\d]+)?$', views.college_view, name='college'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
]


handler503 = 'destinations.views.maintenance_mode'
