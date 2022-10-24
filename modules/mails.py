import smtplib
import email.message

mail_template = None
try:
    with open('../res/template_mail.html', 'r', encoding='utf-8') as html_file:
        mail_template = html_file.read()
except Exception as e:
    print(e)
email_content = mail_template

msg = email.message.Message()
msg['Subject'] = 'Tutsplus Newsletter'
msg['From'] = 'castanedacristian2016@gmail.com'
msg['To'] = 'crcastanedao@unal.edu.co'
password = "uygjdptgwrzratps"

msg.add_header('Content-Type', 'text/html')
msg.set_payload(email_content)
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)
server.sendmail(msg['From'], [msg['To']], msg.as_string())
server.quit()
print(f"successfully sent email to {msg['To']}")
