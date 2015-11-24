# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import College, CollegeApp, APExam, SAT2, Senior, User

class AuthenticateForm(AuthenticationForm):

    username = forms.CharField(required=True,
                               widget=forms.widgets.TextInput(attrs={"placeholder": "Username"}),
                               error_messages={"required": "Invalid username",
                                               "inactive": "Access disallowed."})

    password = forms.CharField(required=True,
                               widget=forms.widgets.PasswordInput(attrs={"placeholder": "Password"}),
                               error_messages={"required": "Invalid password",
                                               "inactive": "Access disallowed."})


class CollegeForm(forms.ModelForm):

    class Meta:
        model = College
        fields = ["name",
                  "ceeb"]

class CollegeAppForm(forms.ModelForm):

    class Meta:
        model = CollegeApp
        fields = ["college",
                  "program",
                  "applied",
                  "submitted",
                  "notified",
                  "result",
                  "attending",
                  "legacy",
                  "interview",
                  "deferred",
                  "waitlisted",
                  "recruited",
                  "supplement",
                  "comments"]

class APExamForm(forms.ModelForm):

    class Meta:
        model = APExam
        fields = ["name",
                  "score",
                  "year",
                  "took_class"]

class SAT2Form(forms.ModelForm):

    class Meta:
        model = SAT2
        fields = ["name",
                  "score",
                  "year"]

class SeniorForm(forms.ModelForm):

    class Meta:
        model = Senior
        fields = ["gender",
                  "email",
                  "race",
                  "hispanic",
                  "international",
                  "gpa",
                  "sat2400",
                  "sat1600",
                  "act",
                  "honors"]

class UserForm(UserCreationForm):
    

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "TJ Username"
        self.fields["username"].help_text = "e.x. 2016jwoglom"
        self.fields["password1"].help_text = "Do NOT use your TJHSST password."

    class Meta:
        model = User
        fields = ["first_name",
                  "last_name",
                  "username",
                  "password1",
                  "password2"]