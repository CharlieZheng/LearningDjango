from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Test(models.Model):
  name = models.CharField(max_length=20)
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __str__(self):
    return self.question_text
  def was_published_recently(self):
    return self.pub_date >= timezone.now()
class Choice(models.Model):
  # CASCADE操作表示主表中数据删除了，依赖表中有引用到主表的行也删除
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
    return self.choice_text
datetime.timedelta(days=1)