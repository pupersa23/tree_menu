from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MainMenu(MPTTModel):
    title = models.CharField('Основной раздел', unique=True, max_length=50)
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True, blank=True,
        related_name='children',
        db_index=True,
        verbose_name='Родительская категория'
    )
    slug = models.SlugField('URL пункта-меню', max_length=50, unique=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = ('Основной раздел')
        verbose_name_plural = ('Основные разделы')

    def get_absolute_url(self):
        return '/%s' % self.slug

    def __str__(self):
        return self.title
