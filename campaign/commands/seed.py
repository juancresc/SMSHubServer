# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand
import random

# python manage.py seed --mode=refresh

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete campaign status instances")
    CampaignStatus.objects.all().delete()



def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 15 addresses
    
    campaignStatus = CampaignStatus(
        name="Pending"
    )
    campaignStatus.save()

    campaignStatus = CampaignStatus(
        name="Completed"
    )
    campaignStatus.save()
    
    messageStatus = MessageStatus(
        name="Pending"
    )
    messageStatus.save()
    
    messageStatus = MessageStatus(
        name="Sending"
    )
    messageStatus.save()
    
    messageStatus = MessageStatus(
        name="Sent"
    )
    messageStatus.save()
    
    messageStatus = MessageStatus(
        name="Delivered"
    )
    messageStatus.save()

    messageStatus = MessageStatus(
        name="Failed"
    )
    messageStatus.save()
    
    
    return True