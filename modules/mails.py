import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .classes import students as STUDENTS


def get_email(connection, studentID):
    """Get the email of a student by his ID:

    Args:
        connection (object): Connection to the database
        studentID (int): Student ID

    Returns:
        str: Student email
    """
    objectStudent = STUDENTS.student()
    try:
        return str(objectStudent.selectStudentByID(connection, studentID)[0][7])
    except Exception as e:
        print("ERROR: " + str(e))


def sendEmail(destinationEmail, bodyMail):
    """Send an email to a destination email

    Args:
        destinationEmail (str): Destination email
        bodyMail (str): Body of the email

    Raises:
        e: Error

    Returns:
        str: Message of success
    """
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
