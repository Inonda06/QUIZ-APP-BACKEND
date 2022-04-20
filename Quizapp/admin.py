from django.contrib import admin
from .models import Quizzes, Question,Category,Updated,Answer


class CatAdmin(admin.ModelAdmin):
    list_display=[
        'name',
    ]


class QuizAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'title',
    ]

class AnswerInlineModel(admin.TabularInline):
    model= Answer
    fields=[
        'answer_text',
        'is_right',
    ]

admin.site.register(Category,CatAdmin)
