import subprocess
from contextlib import suppress

from django.core.management.base import BaseCommand
from django.core.management import execute_from_command_line


class Command(BaseCommand):
    help = 'Run database migrations.'

    def handle(self, *args, **options):
        print("This is a mock data!")

    # def is_database_available(self):
    #     try:
    #         subprocess.check_output(
    #             'docker exec -t db psql -c "SELECT 1"',
    #             stderr=suppress(),
    #             shell=True,
    #         )
    #         return True
    #     except subprocess.CalledProcessError:
    #         return False

    # def make_migrations(self):
    #     execute_from_command_line(['python', 'manage.py', 'makemigrations'])
