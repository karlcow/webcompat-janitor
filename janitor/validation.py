#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Business Rules for labels in webcompat.com"""

import json
import logging

logger = logging.getLogger('issue')
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s: %(message)s',
    datefmt='%H:%M:%S')
console.setFormatter(formatter)
logger.addHandler(console)

OPEN_STATUS = ['status-needstriage', 'status-needsdiagnosis',
               'status-needscontact', 'status-contactready',
               'status-sitewait']
CLOSED_STATUS = ['status-fixed', 'status-incomplete', 'status-invalid',
                 'status-wontfix', 'status-worksforme', 'status-duplicate']

def get_status_labels(issue):
    """Takes a issue dictionary and returns status labels."""
    status_labels = [label['name'] for label in issue['labels']
                     if label['name'].startswith('status-')]
    if not status_labels:
        return None
    return status_labels


def has_status_label(issue):
    """Check if the issue has a real status label.

    Returns a tuple with True/False and the issue number."""
    status_labels = get_status_labels(issue)
    if status_labels and set(status_labels).intersection(
        OPEN_STATUS + CLOSED_STATUS):
            return True
    else:
        return False


def has_conflicting_status(issue):
    """Check if the issue has conflicting status."""
    labels = get_status_labels(issue)
    if labels and issue['state'] == 'open':
        if len(set(labels).intersection(OPEN_STATUS)) > 1:
            return True
    if labels and issue['state'] == 'closed':
        if len(set(labels).intersection(CLOSED_STATUS)) > 1:
            return True
    return False


def has_wrong_status(issue):
    """Check if the issue has conflicting status."""
    labels = get_status_labels(issue)
    if issue['state'] == 'open':
        if not set(labels).intersection(OPEN_STATUS):
            return True
    if issue['state'] == 'closed':
        if not set(labels).intersection(CLOSED_STATUS):
            return True
    return False


def check_issue(issue):
    """Take an issue as dictionary and check if there is a problem."""
    logger.info('Issue {number}'.format(number=issue['number']))
    if has_status_label(issue):
        if has_conflicting_status(issue):
            status_labels = get_status_labels(issue)
            logger.warn('Too many labels for {number}: {labels}'.format(
                number=issue['number'],
                labels=status_labels))
        if has_wrong_status(issue):
            status_labels = get_status_labels(issue)
            logger.warn(
                'Wrong label for {number}: {state} <> {labels}'.format(
                    state=issue['state'],
                    number=issue['number'],
                    labels=status_labels))
    else:
        logger.warn(
            'Issue {number} has no status label'.format(number=issue['number']))

