from django.core.management.base import BaseCommand

from ...models import ApplicationType
from django.conf import settings

from django.contrib.auth.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(f"{file_name}") as file:
            for row in file:
                name = row.capitalize().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                ApplicationType.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS("list of easement added"))
