
from django.core.mail import EmailMessage
class Util:
    """
    Sends an email using Django's EmailMessage class.

    :param data: Dictionary containing necessary information for email sending.
                 Must contain keys 'email_subject', 'email_body', and 'to_email'.
    :type data: dict
    :return: No return value.
    :rtype: None
    """
    @staticmethod
    def send_email(data):
        email=  EmailMessage(subject=data['email_subject'], body=data['email_body'],to=[data['to_email']])
        email.send()