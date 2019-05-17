from campaign.models import Campaign
from django.forms import ModelForm

class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        exclude = ['status', 'user']