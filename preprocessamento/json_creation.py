import json 
import re


def create_json(arquivo_txt):
    with open(arquivo_txt, 'r', encoding='utf-8') as f:
        texto = f.read()

    secoes = [s.strip() for s in texto.split('-----------------------------------------------------------------------------')]

    data = [{'texto': s.replace('\n', ''), 'textos': quebrar_sentencas(s)} for s in secoes]

    estrutura_json = {'data': data}

    with open('data/norma_json.json', 'w', encoding='utf-8') as f:
        json.dump(estrutura_json, f, ensure_ascii=False, indent=2)

    print(texto)


def quebrar_sentencas(texto):
    padrao = r'(?<!\d)\.(?=\s+[A-ZÁÉÍÓÚÂÊÔÃÕÀ]|$)|\n+'
    sentencas = [s.strip() for s in re.split(padrao, texto) if s.strip()]
    return sentencas



# create_json('data/txts/txt_nbr9050_ref.txt')


# Funcionando! Porém tem que ver como separar o texto em sentenças diferentes pelo '.', oq eu tenho feito é quase certo mas vai falhar 
# por conta dos números das seções, como 2.4.5, tem que ver como vai fazer. Eu pensei em só remover o número do inicio de cada linha
# mas ainda existem momentos em que temos referencias às seções no próprio texto que quero capturar

# Uma solução que estou pensando é em verificar se o caractere a esquerda do ponto é uma letra e se o da direita é um espaço, mas vamo
# testando ai p ver



# Considerações: acredito que agora para o modelo 1 é só polir o prompt, o resultado está aceitavel até
