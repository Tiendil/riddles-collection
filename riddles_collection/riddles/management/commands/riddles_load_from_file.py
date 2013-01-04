# -*- coding: utf-8 -*-
import re
from django.core.management.base import BaseCommand
from optparse import make_option

from dext.utils.decorators import nested_commit_on_success

from ...models import Riddle, Category

class Command(BaseCommand):

    help = 'load riddles from file'

    option_list = BaseCommand.option_list + (
        make_option('-i', '--input',
                    action='store',
                    type=str,
                    dest='input',
                    default='-',
                    help='input file'),
        )


    @nested_commit_on_success
    def handle(self, *args, **options):

        input = options['input']

        f = open(input, 'r')

        content = f.read()

        f.close()

        riddle_pattern = re.compile(r"^(.*)===Answer===(.*)===CATEGORY===(.*)$", re.DOTALL)

        riddles = re.split('===TEXT===', content)[1:]

        for riddle in riddles:

            match = riddle_pattern.match(riddle)

            if match is None:
                print riddle
                raise Exception('match failed')

            text = match.group(1)
            answer = match.group(2)
            category = match.group(3)

            category_object, created = Category.objects.get_or_create(name=category)
            Riddle.objects.create(text=text,
                                  answer=answer.lower(),
                                  category=category_object)

        print '%i riddles added' % len(riddles)
