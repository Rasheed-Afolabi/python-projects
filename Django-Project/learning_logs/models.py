from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    
    
    
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        #it allows us to set a special attribute telling Django to use 'entries' as the plural name for this model
        # when it needs to refer to multiple entries.
        # would refer to multiple entries as 'Entrys'
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
        