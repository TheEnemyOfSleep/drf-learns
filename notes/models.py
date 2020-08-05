from django.db import models
from django.contrib.auth import get_user_model


class Note(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField(max_length=150, db_index=True)
    author = models.ForeignKey(
        get_user_model(),
        related_name='notes', 
        null=True,
        blank=True,
        on_delete=models.SET_NULL
      )

    def __str__(self):
        return self.title