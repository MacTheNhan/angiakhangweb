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
    id_portfolio_project = models.CharField(max_length=10)
    name_portfolio_project = VarCharField()

    class Meta:
        db_table = 'portfolioproject'


class Area(models.Model):
    id_area = models.CharField(max_length=10)
    name_area = VarCharField()

    class Meta:
        db_table = 'area'


class Project(models.Model):
    id_project = models.CharField(max_length=10)
    name_project = VarCharField()
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    portfolio_project = models.ForeignKey(PortfolioProject, on_delete=models.DO_NOTHING)
    status_progress = models.IntegerField(default=0)
    photo_album = models.ImageField(upload_to='/')
    description_project = VarCharField()
    avatar_image = models.ImageField(upload_to='/')

    class Meta:
        db_table = 'project'


class PortfolioPosts(models.Model):
    id_portfolio_posts = models.CharField(max_length=10)
    id_parent = models.IntegerField(default=0)
    name_portfolio_posts = VarCharField()

    class Meta:
        db_table = 'portfolioposts'


class Posts(models.Model):
    id_posts = models.CharField(max_length=10)
    portfolio_posts = models.ForeignKey(PortfolioPosts)
    avatar_posts = models.ImageField(upload_to='/')
    title = VarCharField()
    content = VarCharField()

    class Meta:
        db_table = 'posts'


class Member(models.Model):
    id_company_member = models.CharField(max_length=10)
    name_company_member = VarCharField()
    avatar_member = models.ImageField(upload_to='/')
    description = VarCharField()
    type = models.IntegerField(default=1)

    class Meta:
        db_table = 'member'

