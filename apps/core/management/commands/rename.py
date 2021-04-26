from django.core.management.base import BaseCommand
import os

ALREADY_RENAMED_ERROR_MESSAGE = """
I apologize for the inconvenience, but this Django Project has already been renamed.
"""

class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django Project name')

    def handle(self, *args, **kwargs):
        """
        x2 = 'StarterProj.urls'
        if x2 == 'StarterProj.urls':
            print(ALREADY_RENAMED_ERROR_MESSAGE)
            return
        """

        new_project_name = kwargs['new_project_name']

        # bit of logic to rename the project

        files_to_modify = [
            'ProjectTemplate/settings.py',
            'ProjectTemplate/wsgi.py',
            'manage.py',
        ]

        proj_folder_to_rename = 'ProjectTemplate'

        for f in files_to_modify:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('ProjectTemplate', new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(proj_folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('Project has been renamed to %s' % new_project_name))