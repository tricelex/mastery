import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Chuckz Okoye'
email['to'] = 'mypetniche@gmail.com'
email['subject'] = 'Recruitment at Kingsway Agency'

email.set_content(html.substitute({'name': 'Chuckz'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('3icelex@gmail.com', '#juxtapo_se1')
    smtp.send_message(email)
    print('all good chief!')
