from campaign.models import *
from django.forms import ModelForm

class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ['name','datetime_start']