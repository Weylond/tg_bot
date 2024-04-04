from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Телеграм-бот"

    def handle(self, *args, **options):
        Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
