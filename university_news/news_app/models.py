from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=20, verbose_name='mobile number')

    def __str__(self):
        return self.name
