from string import Template
from datetime import  datetime


with open('template.html','r') as html:
    tamplate = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    #corpo_msg = tamplate.substitute(nome='josue', data=data_atual)
    corpo_msg = tamplate.safe_substitute(nome='josue', data=data_atual)

print(corpo_msg)