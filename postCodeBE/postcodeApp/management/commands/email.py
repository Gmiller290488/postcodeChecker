from postcodeApp.emailWinner import start
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Calls function to check for winning postcode and email the winner'

    def handle(self, *args, **options):
        start()