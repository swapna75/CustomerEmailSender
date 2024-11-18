
## Custom Email Sender

This is a custom email-sending application that allows users to send personalized emails using data imported from Google Sheets or CSV files. It includes features like email scheduling, throttling, tracking, and real-time analytics for email delivery statuses.
## Features

 - Import Data: Upload email data from Google Sheets or CSV files.

 - Customizable Emails: Create personalized email content using  dynamic fields (e.g., {Company Name}, {Location}).

 - Email Scheduling: Schedule emails to be sent at specific times or intervals.

 - Email Throttling: Control the speed of email delivery to avoid being flagged as spam.

 - Email Tracking: Track email delivery statuses (Sent, Delivered, Opened, Bounced).

 - Real-Time Analytics: View real-time statistics on email delivery and status updates.
    
- Dashboard: Interactive web dashboard to manage email campaigns and monitor results.
## Technologies Used
- Backend: Flask (Python web framework)

- Frontend: HTML/CSS for the dashboard

- Database: SQLAlchemy (for ORM), SQLite (for development,PostgreSQL or other for production)

- Email Service Provider: SendGrid (for email sending and tracking)

- Task Queue: Celery (for scheduling and sending emails)
    
- Broker: Redis (for Celery task queue)
## Prerequisites
Before running this application, ensure that you have the following installed:

- Python 3.7+

- Redis (for Celery task queue)

- A SendGrid account for email sending and tracking

- Google Sheets API access (if using Google Sheets integration)
## Installation
1. Clone the repository:

```bash
  git clone https://github.com/your-username/Custom-Email-Sender.git
cd Custom-Email-Sender

```
2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use 

```
3. Install dependencies:
```bash
pip install -r requirements.txt


```
4. Set up Redis (required for Celery):

Install Redis and start the server locally, or use a hosted Redis service.

5. Configuration:

Create a .env file in the project root with the following environment variables:
```bash
SECRET_KEY=your-secret-key
GOOGLE_SHEET_ID=your-google-sheet-id
SENDGRID_API_KEY=your-sendgrid-api-key
DATABASE_URL=sqlite:///emails.db  # For production, use a more robust DB like PostgreSQL
REDIS_URL=redis://localhost:6379/0
```
Make sure to replace the placeholder values (your-secret-key, your-google-sheet-id, your-sendgrid-api-key) with actual values.

6. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```
## Running the Application

1. Start the Celery worker (for scheduling and sending emails):

```bash

celery -A tasks.celery worker --loglevel=info

```
2. Run the Flask application:
```bash

flask run

```
Access the dashboard by navigating to http://127.0.0.1:5000 in your web browser.

## Usage

- (1) Upload Data: Use the Google Sheets or CSV upload option to import recipient data such as email addresses and dynamic fields.

- (2) Create Custom Emails: Enter a customizable prompt with placeholders (e.g., {Company Name}, {Location}) that will be replaced with data from each row.
- (3) Schedule Emails: Choose scheduling options to send emails immediately or at specified intervals.
- (4) View Real-Time Analytics: Track email statuses (Sent, Scheduled, Failed) and delivery statuses (Delivered, Opened, Bounced) on the dashboard.

## Testing
- Test email sending and tracking features by configuring a limited test dataset.

- Ensure that scheduled emails are sent at the expected times and throttling is respected.

## Deployment
To deploy the application for production, follow these steps:

-  (1) Set up a production-ready database (e.g., PostgreSQL).
- (2) Use a production-ready server (e.g., Gunicorn) to run the Flask app.
- (3) Configure Redis on a hosted service for Celery (e.g., Redis Labs).
- (4) Host the app on a cloud provider (e.g., AWS, DigitalOcean).

## License
This project is licensed under the MIT License.
    