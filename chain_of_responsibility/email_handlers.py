from abc import ABCMeta, abstractmethod

from email_content_detector import EmailType, EmailDetector

class EmailHandlerInterface(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.detector = EmailDetector()

    @abstractmethod
    def handle_request(self, email: str):
        raise NotImplementedError()


class SpamHandler(EmailHandlerInterface):
    def _should_handle(self, email) -> bool:
        if self.detector.detect(email) == EmailType.SPAM:
            return True
        return False

    def handle_request(self, email: str) -> bool:
        if self._should_handle(email):
            print('This is a spam. Deleting it...')
            return True
        return False


class FanHandler(EmailHandlerInterface):
    def _should_handle(self, email) -> bool:
        if self.detector.detect(email) == EmailType.FANS:
            return True
        return False

    def handle_request(self, email: str) -> bool:
        if self._should_handle(email):
            print('This is an email from fans. Sending it to CEO...')
            return True
        return False


class ComplaintHandler(EmailHandlerInterface):
    def _should_handle(self, email) -> bool:
        if self.detector.detect(email) == EmailType.COMPLAINT:
            return True
        return False

    def handle_request(self, email: str) -> bool:
        if self._should_handle(email):
            print('This is a complaint. Sending it to the legal department...')
            return True
        return False


class RequestHandler(EmailHandlerInterface):
    def _should_handle(self, email):
        if self.detector.detect(email) == EmailType.REQUEST:
            return True
        return False

    def handle_request(self, email: str):
        if self._should_handle(email):
            print('This is a request from customer. Sending it to the business department...')
            return True
        return False


class UnidentifiedEmailHandler(EmailHandlerInterface):
    def _should_handle(self, email):
        if self.detector.detect(email) == EmailType.UNIDENTIFIED:
            return True
        return False

    def handle_request(self, email: str):
        if self._should_handle(email):
            print('This is an unidentified email. Sending it to the AI team to review...')
            return True
        return False