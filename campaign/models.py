from django.contrib.auth.models import User
from django.db import models

class CampaignStatus(models.Model):
    name = models.CharField(max_length=200)

class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    sourcefile = models.FileField(upload_to='sources')
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.ForeignKey(CampaignStatus, on_delete=models.CASCADE)

class CampaignStatusChange(models.Model):
    status = models.ForeignKey(CampaignStatus, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

class MessageStatus(models.Model):
    name = models.CharField(max_length=200)

class Message(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    status = models.ForeignKey(MessageStatus, on_delete=models.CASCADE)

class MessageStatusChange(models.Model):
    status = models.ForeignKey(MessageStatus, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Message, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

class Contact(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
