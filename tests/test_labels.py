#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Tests for Webcompat Janitor Business Rules."""

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
        """Reads the fixture for a test."""
        with open(FIXTURE_DIR + issue_fixture) as f:
            json_issue = json.load(f)
        return json_issue

    def test_get_status_labels(self):
        """Returns the list of labels."""
        json_issue = self.read_issue('issue_with_status_label.json')
        expected = ['status-needstriage']
        actual = validation.get_status_labels(json_issue)
        self.assertListEqual(expected, actual)
        json_issue = self.read_issue('issue_no_status_label.json')
        actual = validation.get_status_labels(json_issue)
        self.assertIsNone(actual)

    def test_has_status_label(self):
        """Send True when issue has status label, else False."""
        json_issue = self.read_issue('issue_no_status_label.json')
        actual = validation.has_status_label(json_issue)
        self.assertFalse(actual)
        json_issue = self.read_issue('issue_with_status_label.json')
        actual = validation.has_status_label(json_issue)
        self.assertTrue(actual)

    def test_has_conflicting_status(self):
        """Send True for mutually exclusive labels."""
        json_issue = self.read_issue('issue_multiple_status_labels.json')
        actual = validation.has_conflicting_status(json_issue)
        self.assertTrue(actual)
        json_issue = self.read_issue('issue_with_status_label.json')
        actual = validation.has_wrong_status(json_issue)
        self.assertFalse(actual)

    def test_has_wrong_status(self):
        """Send True for issues with wrong labels with regards to state."""
        json_issue = self.read_issue('issue_wrong_open_status_label.json')
        actual = validation.has_wrong_status(json_issue)
        self.assertTrue(actual)
        json_issue = self.read_issue('issue_wrong_closed_status_label.json')
        actual = validation.has_wrong_status(json_issue)
        self.assertTrue(actual)
        json_issue = self.read_issue('issue_with_status_label.json')
        actual = validation.has_wrong_status(json_issue)
        self.assertFalse(actual)



if __name__ == '__main__':
    unittest.main()
