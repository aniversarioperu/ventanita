# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

import codecs
import json
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from core.models import DeudorRedam
from core.models import DeudorRedamBond


class Command(BaseCommand):
    """
    Imports data from REDAM from JsonLines file
    """
    option_list = BaseCommand.option_list + (
        make_option('--jsonfile',
                    dest='jsonfile',
                    help='Enter name of json file as argument.'
                    ),
    )

    def handle(self, *args, **options):
        if options['jsonfile'] is None:
            error_msg = 'Enter name of json file as argument.' \
                        ' "python manage.py import_redam --jsonfile=redam.jl --settings=ventanita.settings.local'
            raise CommandError(error_msg)

        json_file = options['jsonfile']

        with codecs.open(json_file, "r") as file_handle:
            dump = file_handle.readlines()

        bond_obj = []
        for line in dump:
            line = line.strip()
            if line != '':
                item = json.loads(line)
                bond = item['bond']
                del item['bond']

                d = DeudorRedam(**item)
                d.save()
                if len(bond) > 0:
                    bond_obj += [DeudorRedamBond(debtor=d,
                                                 bond_type=i['bond_type'],
                                                 full_name=i['full_name'],
                                                 ) for i in bond]
        DeudorRedamBond.objects.bulk_create(bond_obj)
