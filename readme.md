本项目是根据(链接)[https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial03/]而作的，其中TestModel对应教程中的polls，LearningDjango对应教程中的mysite

 - 使用的编辑器

Visual Studio Code

 - 安装Django
```sudo pip3 install Django```

 - 运行程序
```python manage.py runserver```
 - 创建表
```python manage.py migrate```

具体会创建什么，取决于你的/LearningDjango/settings.py设置文件和每个应用的数据库迁移文件

 - python manage.py makemigrations TestModel

没搞懂这条命令

执行完这条命令后，/TestModel/migrations目录下会生产一些文件

 - python manage.py sqlmigrate polls 0001

这个好像是是数据库升级，帮你自动生成升级数据库的时候该做的工作

## 改变模型需要三步

1. 编辑 models.py 文件，改变模型。
2. 运行 python manage.py makemigrations 为模型的改变生成迁移文件。
3. 运行 python manage.py migrate 来应用数据库迁移。

## 安装mysqlclient-python

1. 环境变量```export PATH=$PATH:/usr/local/mysql/bin```
2. Download source by git clone git@github.com:PyMySQL/mysqlclient-python.git
3. python3 setup.py install

```python manage.py shell```

```
>>> from TestModel.models import Choice, Question
>>> Question.objects.all()
>>> Question.objects.filter(id=1)
>>> Question.objects.filter(question_text__startswith='What')
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
>>> Question.objects.get(id=2)
>>> Question.objects.get(pk=1)
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
>>> q = Question.objects.get(pk=1)
>>> q.choice_set.all()
>>> q.choice_set.create(choice_text='Not much', votes=0)
>>> q.choice_set.create(choice_text='The sky', votes=0)
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
>>> c.question
>>> q.choice_set.all()
>>> q.choice_set.count()
>>> Choice.objects.filter(question__pub_date__year=current_year)
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```

 - Create superuser
```python manage.py createsuperuser```
 - Run server
```python manage.py runserver```

 - 运行自动化测试

```python manage.py test TestModel```

## 样式等静态文件
使用STATICFILES_FINDERS设置查找器
AppDirectoriesFinder查找器实现了一种简单引用模板路径的方式