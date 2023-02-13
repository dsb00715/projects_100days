import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
EMAIL_TO = "dsb007151@gmail.com"
LINK = "https://www.python.org"

msg = MIMEMultipart()
msg["Subject"] = "This is a test message"
msg["From"] = EMAIL
msg["To"] = EMAIL_TO

html = """\
<html>
  <head>Hi!</head>
  <body>
    <p>Hello<br>
       How are you?<br>
       Here is the <a href={LINK}>link</a> you wanted.
    </p>
  </body>
</html>
""".format(
    **locals()
)
msg.attach(MIMEText(html, "html"))

email_string = msg.as_string()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(EMAIL, EMAIL_TO, email_string)
