import json
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSerializable
from typing import Dict

# isso é pra ele achar o 'prompts.py'
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from preprocessamento.json_creation import quebrar_sentencas

from constants.prompts import ZERO_SHOT_R2, FEW_SHOT_R2

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
DELAY = 5 # p não estourar o limite de 15 RPM

prompt = PromptTemplate(
    template = FEW_SHOT_R2,
    input_variables=['texto']
)


gemini = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    temperature=0,
    max_tokens=None,
    timeout=None, 
    max_retries=2,
    api_key=API_KEY
)


chain: RunnableSerializable[Dict[str,str], str] = prompt | gemini 


with open('data/fs_r1_gemini_result.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print('===========================================================')
print(f'Iniciando prompting...')
print('===========================================================')

result_dict = {'data': []}

texto_reformulado_index = 1
for dict in dados['data']:
    for sentenca in dict['sentencas']:
        response = chain.invoke({'texto': sentenca})

        print(response.content)

        result_txt = {"index": texto_reformulado_index, "texto_original": dict['texto_reformulado'], "sentenca": sentenca, "operadores": quebrar_sentencas(response.content)}
        result_dict['data'].append(result_txt)

        with open('data/fs_r2_teste_gemini_result.json', 'w', encoding='utf-8') as f:
            json.dump(result_dict, f, ensure_ascii=False, indent=4)

        print('----------------------------------------')
        time.sleep(DELAY)
    texto_reformulado_index += 1
