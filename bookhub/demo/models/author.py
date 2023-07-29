from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    birthdate = models.DateTimeField()
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name[0]}."