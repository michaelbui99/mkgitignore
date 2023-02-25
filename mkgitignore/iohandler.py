from pathlib import Path
from exceptions import InvalidTemplateException
from os import linesep
from sys import argv
from template_fetcher import TemplateFetcher


class IoHandler:
    def __init__(self):
        self.file_name = ".gitignore"

    def write_gitignore(self, target_dir_absolute_path: str, content: str):

        path = Path(target_dir_absolute_path, self.file_name)

        if (path.exists()):
            override = input(
                "existing .gitignore exists. Override existing .gitignore? [y]es/[n]o: ")
            if (override.lower() != "y"):
                print("Aborting creation of .gitignore")
                return

        with open(Path(target_dir_absolute_path, self.file_name), mode="w") as file:
            for line in content.splitlines():
                file.write(f"{line}{linesep}")
        print(f"Created gitignore at {str(path)}")

    def get_template_argument(self):
        if (len(argv) == 1):
            raise InvalidTemplateException(f"No template was provided")

        return argv[1]

    def fetch_template_content(self, template: str) -> str:
        template_fetcher = TemplateFetcher()
        return template_fetcher.get_template(template)
