import requests
from exceptions import TemplateNotFoundException


class TemplateFetcher:
    def __init__(self):
        self.path = "https://raw.githubusercontent.com/github/gitignore/main/"
        self.file_extension = '.gitignore'

    def get_template(self, template: str) -> str:
        # Convert first character in template to upper case since they are PascalCase in the repository
        if not template.startswith(f"{template[0]}".upper()):
            template = f"{template[0]}".upper() + template[1:]

        res = requests.get(f"{self.path}{template}{self.file_extension}")

        if res.status_code != 200:
            raise TemplateNotFoundException(
                f"Template <{template}> was not found")

        return res.text
