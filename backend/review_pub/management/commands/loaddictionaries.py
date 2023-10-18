from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Loads predefined dictionaries: Languages and Domains"

    def handle(self, *args, **options):
        print('Loading domains: ', end='')
        call_command("loaddata", "review_pub/domains.json")
        print('Loading languages: ', end='')
        call_command("loaddata", "review_pub/languages.json")
        print('Loading user groups: ', end='')
        call_command("loaddata", "review_pub/groups.json")
