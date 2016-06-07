from django.db import models


class Comment(models.Model):

    post = model.ForeignKey("Post")

    content = model.TextField()

    def __str__(self):
        return self.content
