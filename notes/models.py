from django.db import models

class Note(models.Model):
    """
    Note model to store user notes
    
    Fields:
    - title: The title of the note
    - content: The main content/body of the note
    - created_at: Timestamp when the note was created
    - updated_at: Timestamp when the note was last updated
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']  # Order notes by most recently updated first

    def __str__(self):
        """String representation of the Note object"""
        return self.title 