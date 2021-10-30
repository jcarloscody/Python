#https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NfOx7ragB1TV1iMslKFa0DfnoXkM1ks5kiTpYmE1nuO8h0OCCRC1d6CTfSnaFAiDK4zu1V2ft4i1Lmal5RiTtH5SQJjA
#https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
#https://stackoverflow.com/questions/63063811/typeerror-utf8-is-an-invalid-keyword-argument-for-compat32-smtplib-email-erro

from string import Template
from datetime import  datetime

from dados_email import meu_email,minha_senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


with open('template.html','r') as html:
    tamplate = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    #corpo_msg = tamplate.substitute(nome='josue', data=data_atual)
    corpo_msg = tamplate.safe_substitute(nome='josue', data=data_atual)


msg = MIMEMultipart()
msg['from'] = 'Josue Carlos da Silva'
msg['to'] = 'josuecarlosos@gmail.com'  #email do cliente
msg['subject'] = 'Atenção: este é um e-mail de teste.'

corpo = MIMEText(corpo_msg,'html')
msg.attach(corpo)

#enviando foto
with open('f.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)
    print('img com sucesso')


#enviando o email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()  #menssagem de helo
        smtp.starttls()  #dando start
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('enviado com sucesso')
    except Exception as e:
        print(e)

