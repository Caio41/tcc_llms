Fase 1 - Pré-processamento
* Extração do texto do PDF das normas usando PyMuPDF (fitz)
* Refinamento do texto: Deixar apenas itens numerados, remover tabelas (?)
* Experimentando com função `extrair_secoes`, talvez de p remover as tabelas verificando o padrão Tabela {x}




Perguntas:
- Devo retirar as 'NOTAS' ?
- Devo retirar os números das seções ? (Exemplo: '5.1.2 Medidas de proteção')