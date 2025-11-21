import json
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSerializable
from typing import Dict

# isso é pra ele achar o 'prompts.py'
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from preprocessamento.json_creation import quebrar_sentencas

from constants.prompts import FEW_SHOT_R2, FEW_SHOT_R2_TESTE, ZERO_SHOT2_R2

prompt = PromptTemplate(
    template = FEW_SHOT_R2_TESTE,
    input_variables=['texto']
)

llama = OllamaLLM(
    model='llama3.2:latest',
    temperature=0
)


chain: RunnableSerializable[Dict[str,str], str] = prompt | llama 
print(f'O prompt é: {prompt}')
print()


# entrada = resultado do modelo r1
with open('data/fs_llama_result.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)


result_dict = {'data': []}

texto_reformulado_index = 1
for dict in dados['data']:
    for sentenca in dict['sentencas']:
        response = chain.invoke({'texto': sentenca})

        print(response)

        result_txt = {"index": texto_reformulado_index, "texto_original": dict['texto_reformulado'], "sentenca": sentenca, "operadores": quebrar_sentencas(response)}
        result_dict['data'].append(result_txt)

        with open('data/fs_r2_teste_llama_result.json', 'w', encoding='utf-8') as f:
            json.dump(result_dict, f, ensure_ascii=False, indent=4)

        print('----------------------------------------')
    texto_reformulado_index += 1
