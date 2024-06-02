import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Run a custom SQL file to set up the database.'

    def handle(self, *args, **kwargs):
        sql_file_path = os.path.join(settings.BASE_DIR, 'db_init.sql')
        
        with open(sql_file_path, 'r') as sql_file:
            sql_script = sql_file.read()
        
        with connection.cursor() as cursor:
            cursor.executescript(sql_script)
        
        self.stdout.write(self.style.SUCCESS('Successfully executed the SQL script.'))
