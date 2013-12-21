#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django import forms
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

'''
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)
    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except:
            return cls()
'''

VOTES = (
        ('A','Канн'),
        ('B','Венеция'),
        ('C','Париж'),
        ('D','Берлин'),
    )

class Survey(models.Model):
    vote = models.CharField(max_length=1, choices=VOTES)

    @staticmethod
    def get_all_A():
        return "%s" % Survey.objects.filter(vote='A').count()
    @staticmethod
    def get_all_B():
        return "%s" % Survey.objects.filter(vote='B').count()
    @staticmethod
    def get_all_C():
        return "%s" % Survey.objects.filter(vote='C').count()
    @staticmethod
    def get_all_D():
        return "%s" % Survey.objects.filter(vote='A').count()


class SurveyForm(forms.Form):
    vote = forms.ChoiceField(VOTES, widget=forms.RadioSelect)
