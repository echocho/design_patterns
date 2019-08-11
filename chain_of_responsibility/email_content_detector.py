"""
A simplistic email detector
"""
from enum import Enum


class EmailType(Enum):
    FANS = 0
    SPAM = 1
    COMPLAINT = 2
    REQUEST = 3
    UNIDENTIFIED = 4


class EmailDetector(object):
    def detect(self, email):
        if 'fans' in email:
            return EmailType.FANS
        if 'spam' in email:
            return EmailType.SPAM
        if 'request' in email:
            return EmailType.REQUEST
        if 'complaint' in email:
            return EmailType.COMPLAINT
        return EmailType.UNIDENTIFIED
