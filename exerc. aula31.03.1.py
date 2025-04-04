import re
Nome = (input ("Digite o seu Nome:"))
if re.match('^[A-Za-z]+$',Nome):
    print('Nome digitado:',Nome)
else:
    print('O campo deve conter apenas letras!')