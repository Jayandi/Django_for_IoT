from django.db import models    

class Messages(models.Model):
    message_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=300)
    topic = models.CharField(max_length=300)
    time = models.CharField(max_length=300, default='None')
