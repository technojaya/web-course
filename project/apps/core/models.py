from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

from django.conf import settings


class Client(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user.email

    class Meta:
        ordering = ['id']

    def as_json(self):
        return dict(
            first_name=self.first_name,
            last_name=self.last_name
        )


class ClientPost(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    text = models.TextField()

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ['id']

    def as_json(self):
        return dict(
            text=self.text
        )