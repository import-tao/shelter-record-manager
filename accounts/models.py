from django.db import models

class PermittedEmails(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified= models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Permitted Emails'
        verbose_name_plural = 'Permitted Emails'
