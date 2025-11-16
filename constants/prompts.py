ZERO_SHOT = '''
** Instruções **
-> Você receberá trechos de um texto normativo e deve separá-lo em sentenças curtas e diretas
-> Cada sentença deve conter somente uma regra computável
-> Separe cada sentença com um \n
-> Sua resposta deve conter apenas as sentenças reformuladas, sem cabeçalhos, explicações adicionais ou formatações
-> Nunca remova os seguintes pontos ao extrair essas sentenças:
   - Condição que precisa ser cumprida
   - Universo da regra
   - Diferentes opções em que a regra se aplica
   - Exceções à regra

Transforme o texto abaixo seguindo as instruções passadas:
Texto: {texto}

Resposta: 
'''


ZERO_SHOT2 = '''
** Instruções ** 

Você receberá um trecho de texto normativo. Sua tarefa é transformá-lo em uma lista de sentenças curtas, diretas e computáveis.

Regras:
1. Cadas sentença deve expressar somente **uma** regra computável.
2. Cada sentença deve preservar integralmente:
   - A condição necessária.
   - O universo/contexto onde a regra se aplica.
   - Todas as alternativas/opções listadas no texto
   - Todas as exceções, ressalvas ou limitações
3. Nunca introduza conteúdo novo.
4. Nunca remova informações.
5. **Separe cada sentença com um caractere '\n'.
6. A saída final deve conter **apenas** as sentenças resultantes, sem explicações, comentários, títulos, bullets ou formatação adicional


Tarefa:
Transforme o texto abaixo seguindo **todas** as instruções:

Texto de entrada:
{texto}

Resposta:
'''


PROMPT_EIKE = '''
A metodologia **RASE N1** transforma textos em unidades menores, onde cada unidade contém **apenas uma única regra computável** com métricas claras.  

### **Instruções:**  
1. **Divida o texto** em sentenças curtas e diretas, respeitando a metodologia **RASE N1**.  
2. **Cada sentença deve conter somente uma única regra computável**.  
3. **Não remova nenhum dos seguintes elementos:**  
   - **Aplicabilidade:** Onde ou quando a regra se aplica.  
   - **Seleção:** Elemento específico dentro da aplicabilidade.  
   - **Requisito:** O que deve ser feito.  
   - **Exceção:** Casos que não precisam seguir a regra.  
4. **A resposta deve conter apenas os textos reformulados, sem explicações ou títulos.**  
5. **Cada frase deve ser separada por `\n`, garantindo uma quebra de linha entre elas.**  
6. **Todas as frases devem ser convertidas em afirmações lógicas.**  

### **Exemplo 1:**  

#### **Entrada:**  
"A inclinação transversal da superfície deve ser de até 2 % para pisos internos e de até 3 % para pisos externos. A inclinação longitudinal da superfície deve ser inferior a 5 %. Inclinações iguais ou superiores a 5 % são consideradas rampas e, portanto, devem atender a 6.6."  

#### **Saída:**  
Pisos internos devem ter inclinação transversal de no máximo 2%.\n  
Pisos externos devem ter inclinação transversal de no máximo 3%.\n  
A inclinação longitudinal da superfície deve ser inferior a 5%.\n  
Inclinações iguais ou superiores a 5% são consideradas rampas e devem atender à norma 6.6.\n  

### **Exemplo 2:**  

#### **Entrada:**  
"Os acessos devem ser vinculados através de rota acessível à circulação principal e às circulações de emergência. Os acessos devem permanecer livres de quaisquer obstáculos de forma permanente."  

#### **Saída:**  
Os acessos devem ser vinculados através de rota acessível à circulação principal e às circulações de emergência.\n  
Os acessos devem permanecer livres de quaisquer obstáculos de forma permanente.\n  

### **Agora, transforme o texto abaixo utilizando a metodologia RASE N1:**  

#### **Texto:**  
{texto}  

#### **Resposta:**  

'''


FEW_SHOT = ''' 
** Instruções **
-> Você receberá trechos de um texto normativo e deve separá-lo em sentenças curtas e diretas
-> Cada sentença deve conter somente uma regra computável
-> Separe cada sentença com um \n
-> Sua resposta deve conter apenas as sentenças reformuladas, sem cabeçalhos, explicações adicionais ou formatações
-> Nunca remova os seguintes pontos ao extrair essas sentenças:
   - Condição que precisa ser cumprida
   - Universo da regra
   - Diferentes opções em que a regra se aplica
   - Exceções à regra

** Exemplos ** 
Exemplo 1:

Entrada: 
Nas ediﬁcações e equipamentos urbanos, todas as entradas, bem como as rotas de interligação às funções do edifício, devem ser acessíveis.

Saída: 
Todas as entradas em ediﬁcações e equipamentos urbanos devem ser acessíveis. \n
Todas as rotas de interligação às funções do edifício devem ser acessíveis. \n


Exemplo 2:
Entrada: 
Os boxes devem ser providos de banco articulado ou removível, com cantos arredondados e superfície antiderrapante impermeável, ter profundidade mínima de 0,45 m, altura de 0,46 m do piso acabado e comprimento mínimo de 0,70 m, instalados no eixo entre as barras, conforme Figura 126. O banco e os dispositivos de fixação devem suportar um esforço de 150 kg.


Saída:
Os boxes devem ser providos de banco articulado ou removível com cantos arredondados e superfície antiderrapante impermeável.  
Os bancos articulados ou removíveis instalados nos boxes devem ter profundidade mínima de 0,45 m.  
Os bancos articulados ou removíveis instalados nos boxes devem ter altura de 0,46 m do piso acabado.  
Os bancos articulados ou removíveis instalados nos boxes devem ter comprimento mínimo de 0,70 m.  
Os bancos articulados ou removíveis instalados nos boxes devem ser instalados no eixo entre as barras conforme a Figura 126.  
O banco e os dispositivos de fixação devem suportar um esforço de 150 kg.


Transforme o texto abaixo seguindo as instruções passadas:
Texto: {texto}

Resposta: 
'''


COT_PROMPT = ''' '''