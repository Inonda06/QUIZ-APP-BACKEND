from ast import Pass
from msilib.schema import Class
from random import choices
from django.db import models



class Category(models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quizzes(models.Model):
    category=models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    title= models.CharField(max_length=255)
    date_created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Updated(models.Model):
    date_updated= models.DateTimeField(auto_now=True)
    class Meta:
        abstract= True

class Question(Updated):

    TYPE=(
        (0,("Multiple Choice")),
    )

    SCALE=(
        (0, ('Fundamental')),
        (1, ('Beginner')),
        (3, ('Intermediate')),
        (4, ('Expert')),
    )

    quiz=models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    technique= models.IntegerField(choices=TYPE, default=0)
    title= models.CharField(max_length=255)
    difficulty= models.IntegerField(choices=SCALE, default=0)
    date_created= models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering =['id']
    def __str__(self):
        return self.title

class Answer(Updated):
    question=models.ForeignKey(Question, related_name='answer',on_delete=models.DO_NOTHING)
    answer_text= models.CharField(max_length=255)
    is_right= models.BooleanField(default=False)
