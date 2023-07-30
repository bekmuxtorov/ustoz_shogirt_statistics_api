from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


class Content(models.Model):
    message_id = models.IntegerField(verbose_name='Xabar Id')
    need_why = models.CharField(max_length=50, verbose_name='Bu ')
    texnologies = models.CharField(
        max_length=300, verbose_name='Texnalogiyalar')
    location = models.CharField(max_length=100, verbose_name='Joylashuv')

    def get_message(self):
        url = ''.join(['https://t.me/UstozShogird/', str(self.message_id)])
        return mark_safe(f'<a href={url} target="_blank">{url}</a>')

    def __str__(self):
        return ' || '.join([str(self.message_id), self.need_why])

    def get_texnologies(self):
        pass

    class Meta:
        db_table = 'contents'
        managed = True
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'
