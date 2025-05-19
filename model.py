from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """
You are an AI Assistant. Summarize the following youtube video transcript in the following format:
- Name of Channel: (only if it's directly mentioned like this is <name>, I'm <name> etc)
- A short title of the summary
- Main Summary in keypoints (bold important points)
- Final conclusion of the video: (if any)

{transcript}
"""

prompt = ChatPromptTemplate.from_template(template)

model =  OllamaLLM(model="deepseek-r1")

chain = prompt | model 

def summarize(transcript:str)-> str:
    return chain.invoke({f"transcript":transcript})