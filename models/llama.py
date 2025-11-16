import json
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSerializable
from typing import Dict

# isso é pra ele achar o 'prompts.py'
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from preprocessamento.json_creation import quebrar_sentencas

from constants.prompts import FEW_SHOT, PROMPT_EIKE, ZERO_SHOT, ZERO_SHOT2


prompt = PromptTemplate(
    template = FEW_SHOT,
    input_variables=['texto']
)

llama = OllamaLLM(
    model='llama3.2:latest',
    temperature=0
)


chain: RunnableSerializable[Dict[str,str], str] = prompt | llama 
print(f'O prompt é: {prompt}')
print()


with open('data/norma_json.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)


result_dict = {'data': []}

for dict in dados['data']:
    txt = dict['texto']
    response = chain.invoke({'texto': txt})
    print(response)

    result_txt = {"texto_original": txt, "texto_reformulado": response, "sentencas": quebrar_sentencas(response)}
    result_dict['data'].append(result_txt)

    with open('data/fs_llama_result.json', 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, ensure_ascii=False, indent=4)

    print('----------------------------------------')


