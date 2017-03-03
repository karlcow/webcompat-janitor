#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''Tests for Webcompat Janitor Business Rules.'''

import json
import unittest

from janitor import validation

FIXTURE_DIR = './tests/fixtures/'


class TestJanitorLabels(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def read_issue(self, issue_fixture):
        '''Reads the fixture for a test.'''
        with open(FIXTURE_DIR + issue_fixture) as f:
            json_issue = json.load(f)
        return json_issue

    def test_has_no_status_label(self):
        '''Send an error when issue has no status label.'''
        json_issue = self.read_issue('issue_no_status_label.json')
        expected = (False, 1)
        actual = validation.has_status_label(json_issue)
        self.assertTupleEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
