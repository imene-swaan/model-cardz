import pandas as pd
from typing import Literal
from jinja2 import Environment, FileSystemLoader
import jinja2
import os
import json
import openai
#import backoff




# Path: cardz/src/utils/utils.py


def get_task(model):
    if type(model).split('.')[0] == 'sklearn':
        task = 'ML'
    else:
        task = 'DL'
    
    model_name =  type(model).__name__ 

    return model_name, task



#@backoff.on_exception(backoff.expo, openai.error.RateLimitError, max_time=120)

def gpt3_model_description(model_name: str, task: str):
    # Replace YOUR_API_KEY with your OpenAI API key
    openai.api_key = "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"


    # Set the model and prompt
    model_engine = "text-davinci-003"

    prompt = 'what type of {task} model is {model_name}? is it a classification model? is it a regression model? give me a short description of the model. what is the model used for?'
    # Set the maximum number of tokens to generate in the response
    max_tokens = 200

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.6,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    model_description = completion.choices[0].text
    return model_description





def save_meta_data(meta_data: dict, path: str= 'results/metrics.json'):
    """ 
    Save the meta data of the model in a json file. 
    """ 
    with open(path, 'w') as f:
        json.dump(meta_data, f, indent=4)



def get_meta_data():
    with open('metrics.json', 'r') as f:
        meta_data = json.load(f)

    return meta_data

def  get_model_card_template ( task :  str, MD: str= 'ML'):
    """ 
    Generate a model card template from a prompt. 
    """ 
    environment = Environment(loader=FileSystemLoader("Templates/"))
    model_card_template = environment.get_template(f'{task}_{MD}.md')

    return  model_card_template



def fill_template(task, meta_data:dict):
        
    temp = get_model_card_template(task)
    content = temp.render(meta_data)

    return content



def save_card(task, file_name: str):

    meta_data = get_meta_data()
    content = fill_template(task, meta_data)
        
    with open('results/' + file_name, mode = 'w', encoding= 'utf-8') as message:
        message.write(content)


        
    print('card saved in directory: ../results/' + file_name)



