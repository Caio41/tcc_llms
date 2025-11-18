ZERO_SHOT_R1 = '''
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


ZERO_SHOT2_R1 = '''
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


PROMPT_EIKE_R1 = '''
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


FEW_SHOT_R1 = ''' 
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



ZERO_SHOT_R2 = '''
A metodologia RASE é responsável por desenvolver regras computáveis a partir de textos normativos. Sendo baseada em quatro operadores principais:

1. Requisito (R): Representa uma condição que **precisa** ser cumprida.
2. Aplicabilidade (A): Delimita o universo de uma regra.
3. Seleção (S): Apresenta diferentes opções em que a regra pode ser pertinente.
4. Exclusão (E): Define exceções à regra.

** Instruções **
-> Você receberá trechos contendo regras computáveis e deve aplicar a metodologia RASE neles, identificando os quatro operadores da metodologia.
-> Caso não identifique algum operador específico, retorne "".
-> Separe cada operador com um '\n'.
-> Sua resposta deve conter apenas os operadores identificados, sem reformulações, explicações ou formatações adicionais.
-> Sua resposta deve ter o formato: Requisito: <resposta> \n Aplicabilidade: <resposta> \n Seleção <resposta> \n Exclusão <resposta>
-> Retorne os operadores na ordem: Requisito, Aplicabilidade, Seleção, Exclusão.


Transforme o texto seguindo as instruções passadas:
Texto: {texto}


Resposta:

'''


ZERO_SHOT2_R2 = '''
A metodologia RASE é responsável por desenvolver regras computáveis a partir de textos normativos. Sendo baseada em quatro operadores principais:

1. Requisito (R) -> OBRIGATÓRIO
2. Aplicabilidade (A) -> OPCIONAL
3. Seleção (S) -> OPCIONAL
4. Exclusão (E) -> OPCIONAL

### **Instruções para cada operador**
** Operador Requisito **
-> Esse operador deve **SEMPRE** existir
-> Deve conter **APENAS** a ação que deve ser cumprida
-> Sua resposta deve começar com um verbo no infinitivo ou imperativo
-> Não deve incluir o universo onde a regra se aplica


** Operador Aplicabilidade ** 
-> Esse operador é **opcional**
-> Deve conter apenas o universo da regra
-> Não repita o que já está no requisito


** Operador Seleção **
-> Esse operador é **opcional**
-> Apresenta diferentes opções em que a regra é pertinente


** Operador Exclusão **
-> Esse operador é **opcional**
-> Define exceções à regra



### **Instruções Gerais**
-> Você receberá trechos contendo regras computáveis e deve aplicar a metodologia RASE neles, identificando os quatro operadores da metodologia.
-> Caso não identifique algum operador específico, retorne "".
-> Separe cada operador com um '\n'.
-> Sua resposta deve conter apenas os operadores identificados, sem reformulações, explicações ou formatações adicionais.
-> Retorne os operadores na ordem: Requisito, Aplicabilidade, Seleção, Exclusão.
-> Não repita informações entre os operadores.
-> Sua resposta deve conter somente os quatro operadores, exatamente no formato: 

Requisito: <conteúdo>
Aplicabilidade: <conteúdo>
Seleção: <conteúdo>
Exclusão: <conteúdo>


Transforme o texto seguindo as instruções passadas:
Texto: {texto}


Resposta:

'''




FEW_SHOT_R2 = '''
A metodologia RASE é responsável por desenvolver regras computáveis a partir de textos normativos. Sendo baseada em quatro operadores principais:

1. Requisito (R) -> OBRIGATÓRIO
2. Aplicabilidade (A) -> OPCIONAL
3. Seleção (S) -> OPCIONAL
4. Exclusão (E) -> OPCIONAL

### **Instruções para cada operador**
** Operador Requisito **
-> Esse operador deve **SEMPRE** existir
-> Deve conter **APENAS** a ação que deve ser cumprida
-> Sua resposta deve começar com um verbo no infinitivo ou imperativo
-> Não deve incluir o universo onde a regra se aplica


** Operador Aplicabilidade ** 
-> Esse operador é **opcional**
-> Deve conter apenas o universo da regra
-> Não repita o que já está no requisito


** Operador Seleção **
-> Esse operador é **opcional**
-> Apresenta diferentes opções em que a regra é pertinente


** Operador Exclusão **
-> Esse operador é **opcional**
-> Define exceções à regra



### **Instruções Gerais**
-> Você receberá trechos contendo regras computáveis e deve aplicar a metodologia RASE neles, identificando os quatro operadores da metodologia.
-> Caso não identifique algum operador específico, retorne "".
-> Separe cada operador com um '\n'.
-> Sua resposta deve conter apenas os operadores identificados, sem reformulações, explicações ou formatações adicionais.
-> Retorne os operadores na ordem: Requisito, Aplicabilidade, Seleção, Exclusão.
-> Não repita informações entre os operadores.
-> Sua resposta deve conter somente os quatro operadores, exatamente no formato: 

Requisito: <conteúdo>
Aplicabilidade: <conteúdo>
Seleção: <conteúdo>
Exclusão: <conteúdo>


Exemplo 1:
Entrada: Sinalização tátil de escadas rolantes deve ter largura entre 0,25 m e 0,60 m

Saída:
Requisito: devem ter largura entre 0,25m e 0,60m
Aplicabilidade: sinalização tátil
Seleção: escadas rolantes
Exclusão: ""


Exemplo 2:
Entrada: Os acessos devem ser vinculados através de uma rota acessível à circulação principal e às circulações de emergência

Saída:
Requisito: devem ser vinculados através de uma rota acessível à circulação principal e às circulações de emergência
Aplicabilidade: acessos
Seleção: ""
Exclusão: ""




Transforme o texto seguindo as instruções passadas:
Texto: {texto}


Resposta:


'''





EIKE_R2 = '''
A metodologia **RASE N2** transforma textos normativos em uma estrutura organizada, garantindo que cada parte do texto apareça apenas uma vez, respeitando a seguinte ordem:

---

### **1. Aplicabilidade (Opcional)**
- **Onde ou quando a regra se aplica.**
- **Deve ser extraída primeiro, antes de outros elementos.**
- **Extraído SOMENTE do TEXTO N1.**
- **NÃO pode conter verbos, ações ou condições.**
- **Se não houver aplicabilidade, retornar `""` (string vazia).**

### **2. Seleção (Opcional)**
- **Parte mais específica da aplicabilidade.**
- **Extraído SOMENTE do TEXTO N1, após a remoção de aplicabilidade.**
- **Deve ser um subconjunto da aplicabilidade, sem repetir o requisito.**
- **NÃO pode conter verbos, ações ou condições.**
- **Se não houver seleção, retornar `""` (string vazia).**

### **3. Exceção (Opcional)**
- **Casos que NÃO precisam seguir a regra.**
- **Extraído SOMENTE do TEXTO N1, após a remoção de aplicabilidade e seleção.**
- **Se um elemento for uma exceção, ele não pode estar em outro campo.**
- **Se não houver, retornar `""` (string vazia).**

### **4. Requisito (Obrigatório)**
- **O que deve ser feito (ação ou condição).**
- **Extraído SOMENTE do TEXTO N1, após a remoção de aplicabilidade, seleção e exceção.**
- **NÃO pode conter informações da aplicabilidade, seleção ou exceção.**
- **O requisito deve começar com um verbo e expressar uma ação ou condição clara.**

---

## **Regras obrigatórias**
**Os elementos devem ser extraídos APENAS do Texto N1.**
**Cada parte do texto deve aparecer apenas uma vez, na ordem Aplicabilidade > Seleção > Exceção > Requisito.**
**Se um elemento não existir, retornar `""` (string vazia).**
**O requisito deve ser a ação ou condição principal e nunca pode ser colocado na seleção.**
**A seleção deve ser um subconjunto da aplicabilidade e não pode conter ações.**
**O requisito deve começar com um verbo e expressar uma ação clara.**
**Retorne somente as resposta.**

---

### **Agora, processe o seguinte texto:**

**Texto N1:**
"{transform}"

#### **Resposta:**
aplicabilidade:
selecao:
execao:
requisito:

'''