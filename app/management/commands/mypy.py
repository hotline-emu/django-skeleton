import subprocess
import sys
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run Mypy on the project"

    def handle(self, *args, **options):
        try:
            subprocess.run(
                [
                    "mypy",
                    ".",
                ],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR("Mypy found issues."))
            sys.exit(e.returncode)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("Mypy is not installed."))
            sys.exit(1)

        self.stdout.write(self.style.SUCCESS("Mypy completed successfully."))
