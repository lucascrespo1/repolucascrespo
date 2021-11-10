import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


host = '10.0.4.1'
port = 25
user = 'lucas.ferreira@facilbh.com.br'
password = 'F@cil12345'


server = smtplib.SMTP(host, port)


server.ehlo()
server.smtp()
server.login(user, password)

message = 'teste'
msg = MIMEMultipart()
msg['From'] = user
msg['To'] = 'infra@facilinformatica.com.br;'
msg['Subject'] = 'TESTE TITULO'
print('\n\nEnviando...')
msg.attach(MIMEText(message, 'plain'))

server.sendmail (msg['From'], msg['To'], msg.as_string())
print(message)
print('\n\nMensagem enviada!')
server.quit()