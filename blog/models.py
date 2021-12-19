from django.db import models


class Blog(models.Model):
    post_title = models.CharField(max_length=100)
    post_date = models.DateField(auto_now_add=True)
    post_desc = models.TextField()

    def __str__(self):
        return self.post_title
