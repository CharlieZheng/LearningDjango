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