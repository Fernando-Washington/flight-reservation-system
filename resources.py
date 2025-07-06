# aqui vai alguns estilos e recursos que serao usados no projeto
import random

from faker import Faker

fake = Faker('pt_BR')

def display_logo():
    logo = """
     █▀ █   █ ▄▀  █▄█ ▀█▀   █▀▄ ██▀ ▄▀▀ ██▀ █▀▄ █ █ ▄▀▄ ▀█▀ █ ▄▀▄ █▄ █
     █▀ █▄▄ █ ▀▄█ █ █  █    █▀▄ █▄▄ ▄██ █▄▄ █▀▄ ▀▄▀ █▀█  █  █ ▀▄▀ █ ▀█
     """
    print(logo)

display_logo()

def clean_cpf(cpf) -> str:
    return cpf.replace('.', '').replace('-', '')