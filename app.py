from pywebio import start_server
from pywebio.output import put_table
from pywebio.input import input
import os
from dotenv import load_dotenv
load_dotenv()
from langchain.chains.question_answering import load_qa_chain
from langchain import PromptTemplate, LLMChain
from langchain.prompts import PromptTemplate
from langchain import HuggingFaceHub

repo_id=os.getenv('repo_id')
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

llm = HuggingFaceHub(repo_id=repo_id,
                     model_kwargs={"min_length":100,
                                   "max_new_tokens":1024, "do_sample":True,
                                   "temperature":0.1,
                                   "top_k":50,
                                   "top_p":0.95, "eos_token_id":49155})

prompt_template = """You are a very helpful AI assistant. Please response to the user's input question with as many details as possible.
Question: {user_question}
Helpufl AI AI Repsonse:
"""  
llm_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(prompt_template))

def chat_response(user_query):
    initial_response=llm_chain.run(user_query)
    temp_ai_response_1=initial_response.partition('<|end|>\n<|user|>\n')[0]
    temp_ai_response_2=temp_ai_response_1.replace('<|end|>\n<|assistant|>\n', '') 
    final_ai_response=temp_ai_response_2.replace('<|end|>\n<|system|>\n', '')   
    print(final_ai_response)
    return final_ai_response

def main():
    while True:
        user_query = input('Ask something')
        put_table([
            ['Q:', user_query],
            ['A:', chat_response(user_query)]
        ])

if __name__ == '__main__':
    start_server(main, port=8080, debug=True)
