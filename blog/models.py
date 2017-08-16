from django.db import models

# Create your models here.
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, blank=False, null=False)
    content = models.TextField(max_length=100, blank=False, null=False)
    time = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(protocol='both',blank=True, null=True, default='0.0.0.0')

    class Meta:
        db_table = 'message'
