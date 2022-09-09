import smtplib
import datetime
from config import from_email, password, to
from email.message import EmailMessage


today = datetime.date.today()

def send_mail():
    msg = EmailMessage()
    subject = 'AV Updates -' + str(today.strftime("%d/%m/%y")) 
    html_body = '''
     <span style='color:red'>PFA</span> .
    ''' 
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to
    
    msg.set_content(html_body, subtype='html')

    # Image file
    with open('image.png', 'rb') as f:
        msg.add_attachment(f.read(),
                           maintype='image',
                           subtype='png',
                           filename='image.png'
                           )

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(from_email, password)
        smtp.send_message(msg)
        print('sent')


if __name__ == '__main__':
    send_mail()
