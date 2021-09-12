from django.contrib import admin
from django.db import models
from .models import Question, Answer, Point


@admin.register(Question)
class QuizAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'show_answer', 'correct'
    ]


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'attempt', 'points', 'passed'
    ]
