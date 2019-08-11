from email_handlers import (SpamHandler, FanHandler, RequestHandler,
                            ComplaintHandler, UnidentifiedEmailHandler)


def drive_run(email):
    for handler in [SpamHandler,
                    FanHandler,
                    RequestHandler,
                    ComplaintHandler,
                    UnidentifiedEmailHandler]:
        if handler().handle_request(email):
            break


fan_email = 'This is an email from a fan'
spam_email = 'This is spam email'
request_email = 'This is a request email'
complaint_email = 'This is a complaint email'
unidentified_email = 'Not sure that this email is'

for email in [fan_email, spam_email, request_email, complaint_email, unidentified_email]:
    drive_run(email)

"""
Output should be:
This is an email from fans. Sending it to CEO...
This is a spam. Deleting it...
This is a request from customer. Sending it to the business department...
This is a complaint. Sending it to the legal department...
This is an unidentified email. Sending it to the AI team to review...
"""