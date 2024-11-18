from celery import Celery
from email_sender import send_email
from config import Config
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
celery.conf.update(result_backend=Config.CELERY_RESULT_BACKEND)

@celery.task(bind=True)
def schedule_email(self, email_data):
    """
    Task to send an email with the given data. This task is scheduled to be run asynchronously.
    Args:
        email_data (dict): Dictionary containing the email details:
            - 'to': recipient email address
            - 'subject': subject of the email
            - 'content': content (HTML or plain text) of the email
    """
    try:

        send_email(to_email=email_data['to'], subject=email_data['subject'], content=email_data['content'])
        return f"Email successfully sent to {email_data['to']}."
    except Exception as e:
        self.retry(exc=e, countdown=60, max_retries=3)  
        return f"Failed to send email to {email_data['to']}. Error: {str(e)}"
