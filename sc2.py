import os 
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


llm = OpenAI(temperature=0.7, openai_api_key=api_key)

prompt = "Suggest me a skill that is in demand?"
response = llm.invoke(prompt)
print("suggested skill:\n", response)

template = "Give me 3 career skills that are in high demand in {year}."
prompt_template = PromptTemplate.from_template(template)

chain = prompt_template | llm | StrOutputParser()

response = chain.invoke({"year": 2025})
print("\n Career Skills in 2025:\n", response)


