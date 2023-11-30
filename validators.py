from marshmallow import ValidationError #Para validação de dados
import re

def valida_idade(n):
    age = int(n)
    if not age:
        raise ValidationError("Not an age.")
    if not (age > 0 and age < 140):
        raise ValidationError("Not a possible age value")

def valida_cpf(cpf):
    padrao = re.compile(r'\d{3}\.\d{3}\.\d{3}\-\d{2}')
    busca = padrao.search(cpf)
    
    if not busca:
        return False

    cpf_numeros = ''.join(filter(str.isdigit, cpf))

    if len(cpf_numeros) != 11 or cpf_numeros == cpf_numeros[0] * len(cpf_numeros):
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf_numeros[i]) * (10 - i)

    digito_1 = 11 - (soma % 11)
    digito_1 = 0 if digito_1 > 9 else digito_1

    soma = 0
    for i in range(10):
        soma += int(cpf_numeros[i]) * (11 - i)

    digito_2 = 11 - (soma % 11)
    digito_2 = 0 if digito_2 > 9 else digito_2

    return cpf_numeros[-2:] == f'{digito_1}{digito_2}'