# pages/models.py
from typing import Any
from django.db import models


class Book(models.Model):
    """These books will be displayed in the home page book library to represent
    the books I read through out my development that laid the foundation to my
    approach and view of program and development"""

    title = models.CharField(max_length=75)
    author = models.CharField(max_length=100)
    topic = models.CharField(max_length=45)
    notes = models.CharField(max_length=100)  # the notes should be quick messages
    book_link = models.URLField()  # link to book source purchase

    def __str__(self):
        return f"{self.title} by {self.author}"
