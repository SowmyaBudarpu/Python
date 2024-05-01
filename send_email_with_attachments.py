import smtplib 
from email.message import EmailMessage

def send_email(sender_email, receiver_email, subject, body, attachments=None):
    email = EmailMessage() ## Creating a object for EmailMessage
    email['from'] = sender_email  ## Person who is sending
    email['to'] = receiver_email  ## Whom we are sending
    email['subject'] = subject  ## Subject of email
    email.set_content(body)  ## Content of email
    
    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as file:
                file_data = file.read()
                file_name = attachment.split('/')[-1]  # Extract file name
            email.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:     
        smtp.ehlo()  ## Server object
        smtp.starttls()  ## Used to send data between server and client
        smtp.login("email_id", "Password")  ## Login ID and password of Gmail
        smtp.send_message(email)  ## Sending email
        print("Email sent")  ## Printing success message

# Example usage:
sender_email = 'your_email@gmail.com'
receiver_email = 'recipient_email@example.com'
subject = 'Test Email with Attachment'
body = 'This is a test email with attachment.'
attachments = ['attachment1.txt', 'attachment2.pdf']  # List of attachment file paths

send_email(sender_email, receiver_email, subject, body, attachments)
