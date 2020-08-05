from django.db import models
from django.contrib.auth import get_user_model


class Note(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField(max_length=150, db_index=True)
    author = models.ForeignKey(
        get_user_model(),
<<<<<<< HEAD
        related_name='notes', 
=======
>>>>>>> 520291b2b15db9c48bf562f464a1c1b8761d8a3b
        null=True,
        blank=True,
        on_delete=models.SET_NULL
      )

    def __str__(self):
        return self.title