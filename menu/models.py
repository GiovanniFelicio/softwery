from django.db import models
from .enums import EnumTypeMenu

class Menu(models.Model):

    name = models.CharField(name='name',max_length=100,null=False)
    path = models.CharField(name='path',max_length=250, null=False)
    url = models.CharField(name='url',max_length=250, null=False)
    type = models.IntegerField(name='type', null=False, choices=EnumTypeMenu.choices())
    active = models.BooleanField(name='active',default=False)
    users = models.ManyToManyField('user.User', through='user.User_menus', blank=True)
    created_at = models.DateTimeField(name='createdAt',auto_now_add=True)
    updated_at = models.DateTimeField(name='updatedAt',auto_now_add=True)

    class Meta():
        db_table = 'SFT_MENU'