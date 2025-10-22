import re

def refinar_texto(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()

    texto = remocao_cabecalho(texto)
    texto = remover_tabelas(texto)
    texto = extrair_secoes(texto)

    # texto = remover_notas(texto)
           
    with open('texto_refinado5.txt', 'w', encoding='utf-8') as f:
        f.write(texto)
    
    print('texto refinado!!!!')
    



def remover_tabelas(texto):
    padrao = (
        r"(?:Conforme tabelas?\s*\d+|Tabela\s*\d+)"
        r".*?(?=\n\d+(?:\.\d+)*\s*[A-Za-zÁ-ú])"
    )

    texto_limpo = re.sub(padrao, "", texto, flags=re.DOTALL)
    return texto_limpo



def extrair_secoes(texto):
    padrao = r'(\d+(?:\.\d+)+\s+[^\n]+(?:\n(?!\d+(?:\.\d+)+).*)*)'
    secoes = re.findall(padrao, texto)
    

    tamanho_minimo = 70
    secoes_extraidas = ''
    for s in secoes:
        if len(s.strip()) >= tamanho_minimo:
            secoes_extraidas += s.strip() + '\n\n-----------------------------------------------------------------------------\n\n'

    return secoes_extraidas


def remocao_cabecalho(texto):
    # ABNT NBR 5410:2004 com ou sem número antes/depois
    # © ABNT 2004 ... reservados com ou sem número antes/depois
    # Cópia não autorizada
    to_remove = [
        r"\d*\s*ABNT\s*NBR\s*5410:2004\s*\d*",
        r"\d*\s*©\s*ABNT\s*2004.*?reservados\s*\d*",
        r"\d*\s*C[oó]pia\s*n[aã]o\s*autorizada\s*\d*",
    ]

    for pattern in to_remove:
        texto = re.sub(pattern, "", texto, flags=re.IGNORECASE)

    return texto



def remover_notas(texto):
    '''Remove trechos como `NOTA xxxxxxxxxx` '''
    texto = re.sub(r'NOTA.*', '', texto)
    
    return texto



def encontrar_estranhos(arquivo):
    '''Função p encontrar erros como `res3idual` que eu tinha visto antes, verifica se tem palavras com números no meio delas'''
    padrao = r'\b[A-Za-zÀ-ú]+\d+[A-Za-zÀ-ú]+\b'

    with open(arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()

    palavras_estranhas = re.findall(padrao, texto)

    return palavras_estranhas



texto = '''

'''

#print(encontrar_estranhos('texto_extraido_fitz2.txt'))
#print(remocao_cabecalho(texto))
#refinar_texto('texto_extraido.txt')
refinar_texto('texto_extraido.txt')