# coding: utf-8
import sys
import subprocess
from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings as project_settings

from dext.utils.meta_config import MetaConfig

meta_config = MetaConfig(config_path=project_settings.META_CONFIG_FILE)

class Command(BaseCommand):

    help = 'prepair all generated static files'

    requires_model_validation = False

    option_list = BaseCommand.option_list + ( make_option('-t', '--tag',
                                                          action='store',
                                                          type=str,
                                                          dest='version',
                                                          help='tag name (version)'),
                                              )


    def handle(self, *args, **options):

        version = options['version']

        if version is None:
            print >> sys.stderr, 'tag name (version) MUST be specified'
            sys.exit(1)

        subprocess.call(['./manage.py', 'less_generate_css'])

        meta_config.increment_static_data_version()
        meta_config.version = version
        meta_config.save_config()
