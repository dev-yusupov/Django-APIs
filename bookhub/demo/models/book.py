from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    author =models.ForeignKey("demo.author", on_delete=models.CASCADE)
    publish_year = models.DateField()
    publisher = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['title']

    def __str__(self) -> str:
        return f"{self.title}"