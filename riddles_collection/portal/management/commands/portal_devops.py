# coding: utf-8

import subprocess

from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings as project_settings

from dext.utils.meta_config import MetaConfig

FABFILE = '/home/tie/repos/mine/devops/riddles/deploy.py'

USER = 'root'
HOST = 'zagadki.org'

FULL_HOST = "%s@%s" % (USER, HOST)


meta_config = MetaConfig(config_path=project_settings.META_CONFIG_FILE)


class Command(BaseCommand):

    help = 'devops commands'

    requires_model_validation = False

    option_list = BaseCommand.option_list + ( make_option('-c', '--command',
                                                          action='store',
                                                          type=str,
                                                          dest='command',
                                                          help='command'),
                                            )


    def handle(self, *args, **options):

        command = options['command']

        if command == 'setup':
            subprocess.call(['fab', '-f', FABFILE, 'setup:static_data_version=%s,version=%s,base_url=%s,host=%s' % (meta_config.static_data_version,
                                                                                                                    meta_config.version,
                                                                                                                    HOST,
                                                                                                                    FULL_HOST)])
        else:
            print 'unknown command'
