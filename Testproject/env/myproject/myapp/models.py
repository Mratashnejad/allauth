from django.db import models

# Create your models here.


class Article(models.Model):
    pub_date = models.DateField()
    slug = models.CharField(max_length=80, null=True)
    headline = models.CharField(max_length=180)
    content = models.TextField()
    #reporter = models.ForeignKey(reporter, on_delete=models.CASCADE)
    thumb = models.ImageField(default='defult.png', blank=True)

    def __str__(self):
        return self.slug
