
from django.db import models
from django.contrib.auth.models import User

"""
创建3个表格：文章（Post）、分类（Category）、标签（Tag）
"""
class Category(models.Model):#分类
    """
    Django 要求模型必须继承models.Model类
    Category 只需要一个简单的分类名那么就可以了
    name为数据库表Category中的一个列 
    name为列名，CharField是字符型
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库
    当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    document：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):#标签
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    
class Post(models.Model):
    #文章涉及字段多，需要创建多个列
    
    #文章标题
    title = models.CharField(max_length=100)
    #文章正文，用的是TextField类型，因为正文将会是一大段
    body = models.TextField()
    #创建时间和最后一次修改时间，用的是DateTimeField类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #文章摘要，写文章时可以没有文章摘要，但是CharField要求必须存入数据，否则报错。
    #指定CharField的blank=True 参数值后就可以运行空值了。
    excerpt = models.CharField(max_length=200,blank=True)
    """
    这是分类与标签，分类与标签的模型我们已经定义在上面。
    我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    参考官方文档：
    https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    """
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    """
    这个是作者，User是从django.contrib.auth.models导入的，
    Django为我们准备的一个内置的应用，专门处理网站的用户注册、登陆等流程。
    一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系
    """
    author = models.ForeignKey(User)
    def __str__(self):
        return self.name

# Create your models here.
