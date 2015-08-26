# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

import os

from django.core.management import call_command
from django.core.management import CommandError
from django.conf import settings
from django.test import TestCase

from core.models import DeudorRedam


class TestCommandImportRedam(TestCase):
    def setUp(self):
        dummy_data = os.path.join(settings.BASE_DIR, '..', '..', 'dummy_data', 'redam.jl')
        args = []
        opts = {'jsonfile': dummy_data}
        cmd = 'import_redam'
        call_command(cmd, *args, **opts)

    def test_import_fail(self):
        args = []
        opts = {}
        cmd = 'import_redam'
        self.assertRaises(CommandError, call_command, cmd, *args, **opts)

    def test_import(self):
        d = DeudorRedam.objects.get(dni='03847515')
        result = d.given_names
        expected = 'SEGUNDO HUMBERTO'
        self.assertEqual(expected, result)
