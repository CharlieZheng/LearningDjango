"""Models"""
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Test(models.Model):
    """Model Test"""
    name = models.CharField(max_length=20)


class Question(models.Model):
    """Model Question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """Is question published recently"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """Model Choice"""
    # CASCADE操作表示主表中数据删除了，依赖表中有引用到主表的行也删除
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


datetime.timedelta(days=1)
