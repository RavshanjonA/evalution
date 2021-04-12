from django.db import models
from django.utils import timezone
import uuid


class BaseModel(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Region(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'region'
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'


class Article(models.Model):
    title = models.CharField(max_length=512, unique=True)
    anons = models.TextField()
    text = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    region = models.ForeignKey(to=Region, on_delete=models.CASCADE, null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'article'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


def photo_upload_path(instance, filename):
    current_dt = timezone.now()
    return f"uploads/{current_dt.strftime('%Y_%m')}/{uuid.uuid4().hex} / {filename}"


class Attachment(models.Model):
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, )
    order = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to=photo_upload_path)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.article.name}, №: {self.order}'

    class Meta:
        db_table = 'attachment'
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'


class Message(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(max_length=64)
    theme = models.CharField(max_length=512)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} theme: {self.theme}'

    class Meta:
        db_table = 'message'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


def upload_employee_path(instance, filename):
    current_dt = timezone.now()
    return f"uploads/{current_dt.strftime('%Y_%m')}/{uuid.uuid4().hex}/{filename}"


class Employee(models.Model):
    POSITIONS = (
        ('muxbir', 'Muxbir'),
        ('maxsus muxbir', 'Maxsus muxbir'),
        ('hududiy muxbir', 'Hududiy muxbir'),
        ('muharrir', 'Muharrir'),
        ('tasvirchi', 'Tasvirchi'),
        ('fotograf', 'Fotograf'),
        ('bo\'lim boshlig\'i', 'Bo\'lim boshlig\'i'),
        ('kontent editor', 'Kontent editor'),
        ('kolumnist', 'Kolummist'),
        ('texnik xodim', 'Texnik xodim'),
    )
    full_name = models.CharField(max_length=128)
    image = models.ImageField(upload_to=upload_employee_path)
    position = models.CharField(max_length=32, choices=POSITIONS)

    def __str__(self):
        return f'{self.full_name} position: {self.theme}'

    class Meta:
        db_table = 'position'
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'
