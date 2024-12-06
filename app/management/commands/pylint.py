import subprocess
import sys
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run Pylint on the project"

    def handle(self, *args, **options):
        try:
            subprocess.run(
                [
                    "pylint",
                    "app",
                    "tests",
                ],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR("Pylint found issues."))
            sys.exit(e.returncode)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("Pylint is not installed."))
            sys.exit(1)

        self.stdout.write(self.style.SUCCESS("Pylint completed successfully."))
