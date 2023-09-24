from django.core.management.base import BaseCommand
from core.models import Contact 

class Command(BaseCommand):
    help = 'Deletes saved contact emails from the database'

    def handle(self, *args, **kwargs):
        try:
            Contact.objects.all().delete()  #deletes all contact records

            self.stdout.write(self.style.SUCCESS('Successfully deleted contact emails'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
