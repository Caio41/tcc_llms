import re

def refinar_texto(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()

    texto = remocao_cabecalho(texto)
    texto = remover_notas(texto)
           
    with open('texto_refinado.txt', 'w', encoding='utf-8') as f:
        f.write(texto)
    
    print('texto refinado!!!!')


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
ABNT NBR 5410:2004
© ABNT 2004 ņ Todos os direitos reservados 7
3 Definições
Para os efeitos desta Norma, aplicam-se as definições da ABNT NBR IEC 60050(826) e as seguintes:
3.1 Componentes da instalação
3.1.1 componente (de uma instalação elétrica): Termo empregado para designar itens da instalação que, dependendo do contexto, podem ser materiais, acessórios, dispositivos, instrumentos, equipamentos (de geração, conversão, transformação, transmissão, armazenamento, distribuição ou utilização de eletricidade), máquinas, conjuntos ou mesmo segmentos ou partes da instalação (por exemplo, linhas elétricas).
3.1.2 quadro de distribuição principal: Primeiro quadro de distribuição após a entrada da linha elétrica na edificação. Naturalmente, o termo se aplica a todo quadro de distribuição que seja o único de uma edificação.
NOTA Ver definição de "ponto de entrada (numa edificação)´ (3.4.4).
3.2 Proteção contra choques elétricos
3.2.1 elemento condutivo ou parte condutiva: Elemento ou parte constituída de material condutor, pertencente ou não à instalação, mas que não é destinada normalmente a conduzir corrente elétrica.
3.2.2 proteção básica: Meio destinado a impedir contato com partes vivas perigosas em condições normais.
3.2.3 proteção supletiva: Meio destinado a suprir a proteção contra choques elétricos quando massas ou partes condutivas acessíveis tornam-se acidentalmente vivas.
3.2.4 proteção adicional: Meio destinado a garantir a proteção contra choques elétricos em situações de maior risco de perda ou anulação das medidas normalmente aplicáveis, de dificuldade no atendimento pleno das condições de segurança associadas a determinada medida de proteção e/ou, ainda, em situações ou locais em que os perigos do choque elétrico são particularmente graves.
3.2.5 dispositivo de proteção a corrente diferencial-res3idual (formas abreviadas: dispositivo a corrente diferencial-residual, dispositivo diferencial, dispositivo DR): Dispositivo de seccionamento mecânico ou associação de dispositivos destinada a provocar a abertura de contatos quando a corrente diferencial- residual atinge um valor dado em condições especificadas.
NOTA O termo ³dispositivo´ não deve ser entendido como significando um produto particular, mas sim qualquer forma possível de se implementar a proteção diferencial-residual. São exemplos de tais formas: o interruptor, disjuntor ou tomada com proteção diferencial-residual incorporada, os blocos e módulos de proteção diferencial-residual acopláveis a disjuntores, os relés e transformadores de corrente que se podem associar a disjuntores, etc.
3.2.6 SELV (do inglês ³separated extra-low voltage´): Sistema de extrabaixa tensão que é eletricamente separado da terra, de outros sistemas e de tal modo que a ocorrência de uma única falta não resulta em risco de choque elétrico.
3.2.7 PELV (do inglês ³protected extra-low voltage´): Sistema de extrabaixa tensão que não é eletricamente separado da terra mas que preenche, de modo equivalente, todos os requisitos de um SELV.
3.3 Proteção contra choques elétricos e proteção contra sobretensões e perturbações eletromagnéticas
3.3.1 eqüipotencialização: Procedimento que consiste na interligação de elementos especificados, visando obter a eqüipotencialidade necessária para os fins desejados. Por extensão, a própria rede de elementos interligados resultante.
Cópia não autorizada
ABNT NBR 5410:2004
8 © ABNT 2004 ņ Todos os direitos reservados
NOTA A eqüipotencialização é um recurso usado na proteção contra choques elétricos e na proteção contra sobretensões e perturbações eletromagnéticas. Uma determinada eqüipotencialização pode ser satisfatória para a proteção contra choques elétricos, mas insuficiente sob o ponto de vista da proteção contra perturbações eletromagnéticas.
3.3.2 barramento de eqüipotencialização principal (BEP): Barramento destinado a servir de via de interligação de todos os elementos incluíveis na eqüipotencialização principal (ver 6.4.2.1).
NOTA A designação ³barramento´ está associada ao papel de via de interligação e não a qualquer configuração particular do elemento. Portanto, em princípio o BEP pode ser uma barra, uma chapa, um cabo, etc.
3.3.3 barramento de eqüipotencialização suplementar ou barramento de eqüipotencialização local (BEL): Barramento destinado a servir de via de interligação de todos os elementos incluíveis numa eqüipotencialização suplementar ou eqüipotencialização local.
3.3.4 equipamento de tecnologia da informação (ETI): Equipamento concebido com o objetivo de:
a) receber dados de uma fonte externa (por exemplo, via linha de entrada de dados ou via teclado);
b) processar os dados recebidos (por exemplo, executando cálculos, transformando ou registrando os dados, arquivando-os, triando-os, memorizando-os, transferindo-os); e
c) fornecer dados de saída (seja a outro equipamento, seja reproduzindo dados ou imagens).
NOTA Esta definição abrange uma ampla gama de equipamentos, como, por exemplo: computadores; equipamentos transceptores, concentradores e conversores de dados; equipamentos de telecomunicação e de transmissão de dados; sistemas de alarme contra incêndio e intrusão; sistemas de controle e automação predial, etc.
3.4 Linhas elétricas
3.4.1 linha (elétrica) de sinal: Linha em que trafegam sinais eletrônicos, sejam eles de telecomunicações, de intercâmbio de dados, de controle, de automação, etc.
3.4.2 linha externa: Linha que entra ou sai de uma edificação, seja a linha de energia, de sinal, uma tubulação de água, de gás ou de qualquer outra utilidade.
3.4.3 ponto de entrega: Ponto de conexão do sistema elétrico da empresa distribuidora de eletricidade com a instalação elétrica da(s) unidade(s) consumidora(s) e que delimita as responsabilidades da distribuidora, definidas pela autoridade reguladora.
3.4.4 ponto de entrada (numa edificação): Ponto em que uma linha externa penetra na edificação.
NOTAS
1 Em particular, no caso das linhas elétricas de energia, não se deve confundir ³ponto de entrada´ com ³ponto de entrega´. A referência fundamental do ³ponto de entrada´ é a edificação, ou seja, o corpo principal ou cada um dos blocos de uma propriedade. No caso de edificações com pavimento em pilotis (geralmente o térreo) e nas quais a entrada da linha elétrica externa se dá no nível do pavimento em pilotis, o ³ponto de entrada´ pode ser considerado como o ponto em que a linha penetra no compartimento de acesso à edificação (hall de entrada).
2 Além da edificação em si, outra referência indissociável de ³ponto de entrada´ é o ³barramento de eqüipotencialização principal´ (BEP), localizado junto ou bem próximo do ponto de entrada (ver 6.4.2.1).
3.4.5 ponto de utilização: Ponto de uma linha elétrica destinado à conexão de equipamento de utilização.
NOTAS
1 Um ponto de utilização pode ser classificado, entre outros critérios, de acordo com a tensão da linha elétrica, a natureza da carga prevista (ponto de luz, ponto para aquecedor, ponto para aparelho de ar-condicionado, etc.) e o tipo de conexão previsto (ponto de tomada, ponto de ligação direta).
Cópia não autorizada
ABNT NBR 5410:2004
© ABNT 2004 ņ Todos os direitos reservados 9
2 Uma linha elétrica pode ter um ou mais pontos de utilização.
3 Um mesmo ponto de utilização pode alimentar um ou mais equipamentos de utilização.
3.4.6 ponto de tomada: Ponto de utilização em que a conexão do equipamento ou equipamentos a serem alimentados é feita através de tomada de corrente.
NOTAS
1 Um ponto de tomada pode conter uma ou mais tomadas de corrente.
2 Um ponto de tomada pode ser classificado, entre outros critérios, de acordo com a tensão do circuito que o alimenta, o número de tomadas de corrente nele previsto, o tipo de equipamento a ser alimentado (quando houver algum que tenha sido especialmente previsto para utilização do ponto) e a corrente nominal da ou das tomadas de corrente nele utilizadas.
3.5 Serviços de segurança
3.5.1 serviços de segurança: Serviços essenciais, numa edificação,
ʊ para a segurança das pessoas;
ʊ para evitar danos ao ambiente ou aos bens.
NOTA São exemplos de serviços de segurança:
ʊ a iluminação de segurança (³iluminação de emergência´),
ʊ bombas de incêndio,
ʊ elevadores para brigada de incêndio e bombeiros,
ʊ sistemas de alarme, como os de incêndio, fumaça, CO e intrusão,
ʊ sistemas de exaustão de fumaça,
ʊ equipamentos médicos essenciais.
3.5.2 alimentação ou fonte normal: Alimentação ou fonte responsável pelo fornecimento regular de energia elétrica.
NOTA Uma determinada alimentação pode ser a ³normal´ durante certo período de tempo e não ser em outro. Por exemplo, em uma instalação cujo consumo de energia elétrica é suprido pela rede de distribuição pública durante certos períodos do dia, mas por geração própria em outros, a ³fonte normal´ pode ser a rede pública ou a geração local, dependendo do período considerado.
3.5.3 alimentação ou fonte de reserva: Alimentação ou fonte que substitui ou complementa a fonte normal.
3.5.4 alimentação ou fonte de segurança: Alimentação ou fonte destinada a assegurar o fornecimento de energia elétrica a equipamentos essenciais para os serviços de segurança.
NOTAS (comuns a 3.5.3 e 3.5.4)
1 O conceito de fonte de segurança está associado à função (serviços de segurança) desempenhada por equipamentos que a fonte alimenta, enquanto o conceito de fonte de reserva está associado ao fato de a fonte complementar a fonte normal ou suprir a sua falta. Como se trata de atributos distintos, que não são incompatíveis, uma fonte pode ser ao mesmo tempo de segurança e de reserva, desde que reúna os dois atributos. Mas uma fonte de reserva destinada a alimentar exclusivamente equipamentos outros que não os de serviços de segurança não pode ser qualificada como de segurança.
Cópia não autorizada
ABNT NBR 5410:2004
10 © ABNT 2004 ņ Todos os direitos reservados
2 Uma alimentação de segurança pode eventualmente atender a outros equipamentos, além dos essenciais aos serviços de segurança, observados os requisitos de 6.6.6.5.
3 Esta Norma não inclui, nesta edição, prescrições específicas para alimentações de reserva destinadas a outros serviços que não os de segurança.
4 Princípios fundamentais e determinação das características gerais
4.1 Princípios fundamentais
Os princípios que orientam os objetivos e as prescrições desta Norma são relacionados em 4.1.1 a 4.1.15.
4.1.1 Proteção contra choques elétricos
As pessoas e os animais devem ser protegidos contra choques elétricos, seja o risco associado a contato acidental com parte viva perigosa, seja a falhas que possam colocar uma massa acidentalmente sob tensão.
4.1.2 Proteção contra efeitos térmicos
A instalação elétrica deve ser concebida e construída de maneira a excluir qualquer risco de incêndio de materiais inflamáveis, devido a temperaturas elevadas ou arcos elétricos. Além disso, em serviço normal, não deve haver riscos de queimaduras para as pessoas e os animais.
4.1.3 Proteção contra sobrecorrentes
As pessoas, os animais e os bens devem ser protegidos contra os efeitos negativos de temperaturas ou solicitações eletromecânicas excessivas resultantes de sobrecorrentes a que os condutores vivos possam ser submetidos.
4.1.4 Circulação de correntes de falta
Condutores que não os condutores vivos e outras partes destinadas a escoar correntes de falta devem poder suportar essas correntes sem atingir temperaturas excessivas.
NOTAS
1 Convém lembrar que tais partes estão sujeitas à circulação desde pequenas correntes de fuga a correntes de falta direta à terra ou à massa, passando por correntes de falta de intensidade inferior à de uma falta direta.
2 No caso dos condutores vivos, considera-se que sua suportabilidade às correntes de falta deve ser assegurada mediante proteção contra sobrecorrentes, como enunciado em 4.1.3.
4.1.5 Proteção contra sobretensões
As pessoas, os animais e os bens devem ser protegidos contra as conseqüências prejudiciais de ocorrências que possam resultar em sobretensões, como faltas entre partes vivas de circuitos sob diferentes tensões, fenômenos atmosféricos e manobras.
4.1.6 Serviços de segurança
Equipamentos destinados a funcionar em situações de emergência, como incêndios, devem ter seu funcionamento assegurado a tempo e pelo tempo julgado necessário.
Cópia não autorizada
ABNT NBR 5410:2004
© ABNT 2004 ņ Todos os direitos reservados 11
4.1.7 Desligamento de emergência
Sempre que forem previstas situações de perigo em que se faça necessário desenergizar um circuito, devem ser providos dispositivos de desligamento de emergência, facilmente identificáveis e rapidamente manobráveis.
4.1.8 Seccionamento
A alimentação da instalação elétrica, de seus circuitos e de seus equipamentos deve poder ser seccionada para fins de manutenção, verificação, localização de defeitos e reparos.
4.1.9 Independência da instalação elétrica
A instalação elétrica deve ser concebida e construída livre de qualquer influência mútua prejudicial entre instalações elétricas e não elétricas.
4.1.10 Acessibilidade dos componentes
Os componentes da instalação elétrica devem ser dispostos de modo a permitir espaço suficiente tanto para a instalação inicial quanto para a substituição posterior de partes, bem como acessibilidade para fins de operação, verificação, manutenção e reparos.
4.1.11 Seleção dos componentes
Os componentes da instalação elétrica devem ser conforme as normas técnicas aplicáveis e possuir características compatíveis com as condições elétricas, operacionais e ambientais a que forem submetidos. Se o componente selecionado não reunir, originalmente, essas características, devem ser providas medidas compensatórias, capazes de compatibilizá-las com as exigências da aplicação.
4.1.12 Prevenção de efeitos danosos ou indesejados
Na seleção dos componentes, devem ser levados em consideração os efeitos danosos ou indesejados que o componente possa apresentar, em serviço normal (incluindo operações de manobra), sobre outros componentes ou na rede de alimentação. Entre as características e fenômenos suscetíveis de gerar perturbações ou comprometer o desempenho satisfatório da instalação podem ser citados:
ʊ o fator de potência;
ʊ as correntes iniciais ou de energização;
ʊ o desequilíbrio de fases;
ʊ as harmônicas.
4.1.13 Instalação dos componentes
Toda instalação elétrica requer uma cuidadosa execução por pessoas qualificadas, de forma a assegurar, entre outros objetivos, que:
ʊ as características dos componentes da instalação, como indicado em 4.1.11, não sejam comprometidas durante sua montagem;
ʊ os componentes da instalação, e os condutores em particular, fiquem adequadamente identificados;
ʊ nas conexões, o contato seja seguro e confiável;
ʊ os componentes sejam instalados preservando-se as condições de resfriamento previstas;
Cópia não autorizada
ABNT NBR 5410:2004
12 © ABNT 2004 ņ Todos os direitos reservados
ʊ os componentes da instalação suscetíveis de produzir temperaturas elevadas ou arcos elétricos fiquem dispostos ou abrigados de modo a eliminar o risco de ignição de materiais inflamáveis; e
ʊ as partes externas de componentes sujeitas a atingir temperaturas capazes de lesionar pessoas fiquem dispostas ou abrigadas de modo a garantir que as pessoas não corram risco de contatos acidentais com essas partes.
4.1.14 Verificação da instalação
As instalações elétricas devem ser inspecionadas e ensaiadas antes de sua entrada em funcionamento, bem como após cada reforma, com vista a assegurar que elas foram executadas de acordo com esta Norma.
4.1.15 Qualificação profissional
O projeto, a execução, a verificação e a manutenção das instalações elétricas devem ser confiados somente a pessoas qualificadas a conceber e executar os trabalhos em conformidade com esta Norma.
4.2 Determinação das características gerais
Na concepção de uma instalação elétrica devem ser determinadas as seguintes características:
a) utilização prevista e demanda (ver 4.2.1);
b) esquema de distribuição (ver 4.2.2);
c) alimentações disponíveis (ver 4.2.3);
d) necessidade de serviços de segurança e de fontes apropriadas (ver 4.2.4);
e) exigências quanto à divisão da instalação (ver 4.2.5);
f) influências externas às quais a instalação for submetida (ver 4.2.6);
g) riscos de incompatibilidade e de interferências (ver 4.2.7);
h) requisitos de manutenção (ver 4.2.8).
4.2.1 Utilização e demanda ± Potência de alimentação
4.2.1.1 Generalidades
4.2.1.1.1 A determinação da potência de alimentação é essencial para a concepção econômica e segura de uma instalação, dentro de limites adequados de elevação de temperatura e de queda de tensão.
4.2.1.1.2 Na determinação da potência de alimentação de uma instalação ou de parte de uma instalação devem ser computados os equipamentos de utilização a serem alimentados, com suas respectivas potências nominais e, em seguida, consideradas as possibilidades de não-simultaneidade de funcionamento destes equipamentos, bem como capacidade de reserva para futuras ampliações.
4.2.1.2 Previsão de carga
A previsão de carga de uma instalação deve ser feita obedecendo-se às prescrições de 4.2.1.2.1 a 4.2.1.2.3.
Cópia não autorizada
ABNT NBR 5410:2004
© ABNT 2004 ņ Todos os direitos reservados 13
4.2.1.2.1 Geral:
a) a carga a considerar para um equipamento de utilização é a potência nominal por ele absorvida, dada pelo fabricante ou calculada a partir da tensão nominal, da corrente nominal e do fator de potência;
b) nos casos em que for dada a potência nominal fornecida pelo equipamento (potência de saída), e não a absorvida, devem ser considerados o rendimento e o fator de potência.
4.2.1.2.2 Iluminação:
a) as cargas de iluminação devem ser determinadas como resultado da aplicação da ABNT NBR 5413;
b) para os aparelhos fixos de iluminação a descarga, a potência nominal a ser considerada deve incluir a potência das lâmpadas, as perdas e o fator de potência dos equipamentos auxiliares.
NOTA Em 9.5.2.1 são fixados critérios mínimos para pontos de iluminação em locais de habitação.
4.2.1.2.3 Pontos de tomada:
a) em locais de habitação, os pontos de tomada devem ser determinados e dimensionados de acordo com 9.5.2.2;
b) em halls de serviço, salas de manutenção e salas de equipamentos, tais como casas de máquinas, salas de bombas, barriletes e locais análogos, deve ser previsto no mínimo um ponto de tomada de uso geral. Aos circuitos terminais respectivos deve ser atribuída uma potência de no mínimo 1000 VA;
c) quando um ponto de tomada for previsto para uso específico, deve ser a ele atribuída uma potência igual à potência nominal do equipamento a ser alimentado ou à soma das potências nominais dos equipamentos a serem alimentados. Quando valores precisos não forem conhecidos, a potência atribuída ao ponto de tomada deve seguir um dos dois seguintes critérios:
ʊ potência ou soma das potências dos equipamentos mais potentes que o ponto pode vir a alimentar, ou
ʊ potência calculada com base na corrente de projeto e na tensão do circuito respectivo;
d) os pontos de tomada de uso específico devem ser localizados no máximo a 1,5 m do ponto previsto para a localização do equipamento a ser alimentado;
e) os pontos de tomada destinados a alimentar mais de um equipamento devem ser providos com a quantidade adequada de tomadas.
4.2.2 Esquema de distribuição
O esquema de distribuição pode ser classificado de acordo com os seguintes critérios:
a) esquema de condutores vivos;
b) esquema de aterramento.
4.2.2.1 Esquema de condutores vivos
São considerados os seguintes esquemas de condutores vivos:
a) corrente alternada:
ʊ monofásico a dois condutores;
ʊ monofásico a três condutores;
Cópia não autorizada
'''

#print(encontrar_estranhos('texto_extraido_fitz2.txt'))
#print(remocao_cabecalho(texto))
refinar_texto('texto_extraido.txt')