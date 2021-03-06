from django.db import models


class VarCharField(models.CharField):
    description = "Unlimited-length string"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = int(1e9)
        super(models.CharField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'VarCharField'

    def db_type(self, connection):
        return 'varchar'

    def formfield(self, **kwargs):
        return super(models.CharField, self).formfield(**kwargs)


class PortfolioProject(models.Model):
    name_portfolio_project = models.CharField(max_length=30000)
    avatar = models.ImageField(upload_to='images/portfolioproject/', blank=True)
    description_portfolio = models.CharField(max_length=30000, null=True)

    class Meta:
        db_table = 'portfolioproject'


class Area(models.Model):
    name_area = models.CharField(max_length=30000)

    class Meta:
        db_table = 'area'


class Project(models.Model):
    name_project = models.CharField(max_length=30000)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    portfolio_project = models.ForeignKey(PortfolioProject, on_delete=models.DO_NOTHING)
    status_progress = models.BooleanField()
    description_project = models.CharField(max_length=30000)
    avatar_image = models.ImageField(upload_to='images/project', blank=True)
    year = models.IntegerField(default=0)
    date = models.DateField(null=True, blank=True)
    status_interior = models.BooleanField(default=False)

    class Meta:
        db_table = 'project'


class Album(models.Model):
    photo = models.ImageField(upload_to='images/albums', blank=True)
    id_project = models.IntegerField(default=0)

    class Meta:
        db_table = 'album'


class PortfolioPosts(models.Model):
    id_parent = models.IntegerField(default=0)
    name_portfolio_posts = models.CharField(max_length=30000)

    class Meta:
        db_table = 'portfolioposts'


class Posts(models.Model):
    portfolio_posts = models.ForeignKey(PortfolioPosts, on_delete=models.DO_NOTHING)
    avatar_posts = models.ImageField(upload_to='images/post/', blank=True)
    title = models.CharField(max_length=30000)
    content = models.CharField(max_length=30000)

    class Meta:
        db_table = 'posts'


class Member(models.Model):
    name_company_member = models.CharField(max_length=30000)
    avatar_member = models.ImageField(upload_to='images/member/', blank=True)
    description = models.CharField(max_length=30000)
    type = models.BooleanField(default=False)

    class Meta:
        db_table = 'member'


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    name_user = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        db_table = 'user'


class Slide(models.Model):
    title = models.CharField(max_length=30000)
    image = models.ImageField(upload_to='images/slide/', blank=True)
    url = models.CharField(max_length=30000, blank=True)
    position = models.BooleanField(default=True)

    class Meta:
        db_table = 'slide'


class Video(models.Model):
    title = models.CharField(max_length=30000)
    url = models.CharField(max_length=30000)
    avatar = models.ImageField(upload_to='images/video/', blank=True)

    class Meta:
        db_table = 'video'