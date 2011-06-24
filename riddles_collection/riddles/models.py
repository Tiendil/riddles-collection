from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=128)

    url = models.CharField(max_length=128, default='')

    caption = models.CharField(max_length=256, default='')

    description = models.TextField(max_length=1024, default='')

    def __unicode__(self):
        return self.name


class Riddle(models.Model):

    text = models.TextField(max_length=1024)

    answer = models.CharField(max_length=128)

    category = models.ForeignKey(Category, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, default=None)

