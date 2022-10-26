import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from . import students as STUDENTS


def get_email(connection, studentID):
    try:
        return str(STUDENTS.selectStudentByID(connection, studentID)[0][7])
    except Exception as e:
        print("ERROR: " + str(e))


def sendEmail(destinationEmail, bodyMail):
    try:
        # create message object instance
        msg = MIMEMultipart()
        message = str(bodyMail)
        # setup the parameters of the message
        msg['Subject'] = 'Informe de promedio académico'
        msg['From'] = 'castanedacristian2016@gmail.com'
        msg['To'] = destinationEmail
        password = "uygjdptgwrzratps"
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        # create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
        # send the message via the server.
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
        server.quit()
        return f"Successfully sent email to {destinationEmail}"
    except Exception as e:
        raise e
