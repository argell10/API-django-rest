from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """ Model Base to use with others apps """
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('State', default=True)
    created_date = models.DateField('Date of created',auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Date of modified',auto_now=True, auto_now_add=False)
    delete_date = models.DateField('Date of delete',auto_now=True, auto_now_add=False)
    
    class Meta:
        abstract = True #define que es un modelo base y no una tabla en la db
        verbose_name = 'Model Base'
        verbose_name_plural = 'Models Base'
        app_label = ['products']