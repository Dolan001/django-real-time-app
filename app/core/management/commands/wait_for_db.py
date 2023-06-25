# Django command to wait for the database to be available

import time
from abc import ABC

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Entry point
        self.stdout.write("Waiting for database")
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database not available, please wait...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database Ready"))



