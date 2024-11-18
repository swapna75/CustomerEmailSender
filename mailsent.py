import sendgrid
from sendgrid.helpers.mail import Mail
from config import Config

def send_email(to_email, subject, content):
    if not Config.SENDGRID_API_KEY:
        print("SendGrid API Key is missing in the configuration.")
        return None
    
    sg = sendgrid.SendGridAPIClient(api_key=Config.SENDGRID_API_KEY)
    from_email = 'your-email@example.com'  
    
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=content
    )

    try:
     
        response = sg.send(message)
        print(f"Email sent successfully! Response code: {response.status_code}")
        print(f"Response Body: {response.body}")
        print(f"Response Headers: {response.headers}")
        
        return response.status_code
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
