from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

def generate_email(username):
    email_address = username + "@mail.com"
    return email_address


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(f"{file_name}") as file:
            for row in file:
                username = row.lower().replace("\n", "").replace(" ", "").strip()
                email = generate_email(username)
                self.stdout.write(self.style.SUCCESS(f"{email} added"))
                User.objects.get_or_create(username=username, email=email, password="password99")
        self.stdout.write(self.style.SUCCESS("list of employees added"))
