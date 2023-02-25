from sys import argv
from os import getcwd
from exceptions import InvalidTemplateException
from iohandler import IoHandler


def main():
    # TODO: Handle with click instead
    iohandler = IoHandler()
    current_dir = getcwd()
    template = iohandler.get_template_argument()

    if not template:
        raise InvalidTemplateException(
            f"Invalid template provided: {template}")

    template_content = iohandler.fetch_template_content(template)
    iohandler.write_gitignore(current_dir, template_content)


main()
