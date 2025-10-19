import PyPDF2
import pdfplumber
import fitz

def extract_pypdf2():
    with open('normas/nbr5410.pdf', 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        texto = ''

        for i in range(14, len(reader.pages)):
            page = reader.pages[i]
            texto += page.extract_text()

    with open('texto_extraido_pypdf2.txt', 'w', encoding='utf-8') as txt:
        txt.write(texto)
    
    print('Salvo')


def extract_pdfplumber():
    texto = ''
    with pdfplumber.open('normas/nbr5410.pdf') as pdf:
        for pag in pdf.pages:
            texto += pag.extract_text()
    

    with open('texto_extraido_pdfplumber.txt', 'w', encoding='utf-8') as txt:
        txt.write(texto)
    
    print('Salvo')


def extract_pymupdf():
    doc = fitz.open('normas/nbr5410.pdf')
    texto = ''

    # Se for precisar fazer mais nuancias nessa extração de texto, investigar essa extração por 'blocks'.
    for i in range(14, len(doc)):
        page = doc[i]
        blocks = page.get_text('blocks')  # retorna uma lista de blocos [(x0, y0, x1, y1, texto, bloco_num), ...]


        for b in blocks:
            block_text = b[4].replace('\n', ' ').strip()  # remove quebras internas do bloco
            texto += block_text + '\n' 
    
    doc.close()

    with open('texto_extraido_fitz2.txt', 'w', encoding='utf-8') as txt:
        txt.write(texto)


    print('Salvo!!!')


extract_pymupdf()