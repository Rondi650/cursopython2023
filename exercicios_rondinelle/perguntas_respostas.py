from typing import TypedDict
import os
os.system('cls')

class Dict_Perguntas(TypedDict):
    Pergunta: str
    Opções: list[str]
    Resposta: str

perguntas: list[Dict_Perguntas] = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Qual é a capital do Brasil?',
        'Opções': ['Rio de Janeiro', 'Brasília', 'São Paulo', 'Salvador'],
        'Resposta': 'Brasília',
    },
    {
        'Pergunta': 'Qual é o maior planeta do Sistema Solar?',
        'Opções': ['Saturno', 'Marte', 'Júpiter', 'Netuno'],
        'Resposta': 'Júpiter',
    },
    {
        'Pergunta': 'Qual é a cor da bandeira do Brasil?',
        'Opções': ['Verde, Amarelo, Azul e Branco', 'Vermelho e Branco', 'Azul e Branco', 'Verde e Amarelo'],
        'Resposta': 'Verde, Amarelo, Azul e Branco',
    },
    {
        'Pergunta': 'Em que ano o Brasil foi descoberto?',
        'Opções': ['1400', '1500', '1600', '1700'],
        'Resposta': '1500',
    },
    {
        'Pergunta': 'Qual é o maior rio do Brasil?',
        'Opções': ['Rio Paraná', 'Rio Amazonas', 'Rio São Francisco', 'Rio Negro'],
        'Resposta': 'Rio Amazonas',
    },
    {
        'Pergunta': 'Quantos continentes existem?',
        'Opções': ['5', '6', '7', '8'],
        'Resposta': '7',
    },
    {
        'Pergunta': 'Qual é o animal mais rápido da Terra?',
        'Opções': ['Leão', 'Gazela', 'Guepardo', 'Cavalo'],
        'Resposta': 'Guepardo',
    },
        {
        'Pergunta': 'Qual é o maior país do mundo por área?',
        'Opções': ['Canadá', 'China', 'Rússia', 'Estados Unidos'],
        'Resposta': 'Rússia',
    },
    {
        'Pergunta': 'Qual é a língua mais falada no mundo?',
        'Opções': ['Espanhol', 'Inglês', 'Mandarim', 'Português'],
        'Resposta': 'Mandarim',
    },
    {
        'Pergunta': 'Em que continente fica a Austrália?',
        'Opções': ['Ásia', 'Oceania', 'América', 'Europa'],
        'Resposta': 'Oceania',
    },
    {
        'Pergunta': 'Qual é o oceano mais profundo?',
        'Opções': ['Oceano Índico', 'Oceano Atlântico', 'Oceano Pacífico', 'Oceano Ártico'],
        'Resposta': 'Oceano Pacífico',
    },
    {
        'Pergunta': 'Quantas patas tem uma aranha?',
        'Opções': ['4', '6', '8', '10'],
        'Resposta': '8',
    },
    {
        'Pergunta': 'Qual é o metal mais precioso?',
        'Opções': ['Prata', 'Ouro', 'Platina', 'Diamante'],
        'Resposta': 'Platina',
    },
    {
        'Pergunta': 'Qual é a estrela mais próxima da Terra?',
        'Opções': ['Alpha Centauri', 'Proxima Centauri', 'Sirius', 'Betelgeuse'],
        'Resposta': 'Proxima Centauri',
    },
]

contador: int = 0
contador_pergunta: int = 0

for dados in perguntas:
    
    pergunta: str = dados['Pergunta']
    opcoes: list[str] = dados['Opções']
    resposta: str = dados['Resposta']
    i: int = 0
    
    contador_pergunta += 1
    print(f'Pergunta {contador_pergunta}: {pergunta}\n')
    while i < len(opcoes):
        print(f'{i+1}) {opcoes[i]}')
        i += 1
         
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        resultado = opcoes[opcao_escolhida-1]
        
        if resultado == resposta:
            print('Acertou\n')
            contador += 1 
        else:
            print(f'Errou!!\nResposta correta: {resposta}\n')
            
    except Exception as e:
        print(f'Entrada Invalida\nErro: {e}\n')
        
print(f'Voce acertou {contador} de {len(perguntas)} perguntas | {contador/len(perguntas)*100:.1f}%\n')
