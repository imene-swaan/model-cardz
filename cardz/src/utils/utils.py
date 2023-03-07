import pandas as pd
from typing import Literal
from jinja2 import Environment, FileSystemLoader
import jinja2
import os
import json
import openai
import inspect
from importlib import import_module
#import backoff




# Path: cardz/src/utils/utils.py


def gpt_api():
    with open('../assets/api_key.txt') as f:
        api_key = f.read()
    return api_key


def get_task(model):
    m = str(type(model)).split("'")[1]
    if m.split('.')[0] == 'sklearn':
        task = 'ML'
    else:
        task = 'DL'
    
    model_name =  type(model).__name__ 

    return model_name, task



#@backoff.on_exception(backoff.expo, openai.error.RateLimitError, max_time=120)
def gpt3_model_description(model_name: str, task: str):
    # Replace YOUR_API_KEY with your OpenAI API key
    openai.api_key = gpt_api()


    # Set the model and prompt
    model_engine = "text-davinci-003"

    prompt = f'what type of {task} model is {model_name}? is it a classification model, a clustering model, or a regression model? give me a short description of the model. what is the model used for? answer me in 3 to 4 sentences'
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



def get_model_type(model_description: str) -> str:
    if 'classification' in model_description:
        model_type = 'classification'
    elif 'regression' in model_description:
        model_type = 'regression'
    elif 'clustering' in model_description:
        model_type = 'clustering'
    else:
        model_type = 'other'
    return model_type



def get_current_model_params(model):

    task = get_task(model)[1]

    if task == 'ML':
        current_model_params = model.get_params()
    return current_model_params


def get_default_model(model):
    mod = str(type(model)).split("'")[1]
    p, m = mod.rsplit('.', 1)

    mod = import_module(p)
    default_model = getattr(mod, m)
    return default_model()


def get_model_default_params(model):

    default_model = get_default_model(model)
    signature = inspect.signature(default_model)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }

def get_model_params(model):
    current_model_params = get_current_model_params(model)
    default_model_params = get_model_default_params(model)

    model_params = {k: [current_model_params[k], default_model_params[k]] for k in current_model_params.keys()}
    return model_params

    

def gpt3_model_params_description(model_name: str):
    # Replace YOUR_API_KEY with your OpenAI API key
    openai.api_key = gpt_api()


    # Set the model and prompt
    model_engine = "text-davinci-003"

    prompt = f'Describe all the hyperparameters of the {model_name} model. Each hyperparamater description should be in a separate sentence and format should be: "hyperparameter name: description of the hyperparameter".'
    # Set the maximum number of tokens to generate in the response
    max_tokens = 250

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
    params_description = completion.choices[0].text.split('.')
    model_params_description = {}
    for i in params_description:
        model_params_description[i.split(':')[0]] = i.split(':')[1]
    
    return model_params_description













def save_meta_data(meta_data: dict, path: str):
    """ 
    Save the meta data of the model in a json file. 
    """ 
    with open(path, 'w') as f:
        json.dump(meta_data, f, indent=4)



def  get_model_card_template( model_type: str, task: str):
    """ 
    Generate a model card template from a prompt. 
    """ 
    environment = Environment(loader=FileSystemLoader("Templates/"))
    model_card_template = environment.get_template(f'{model_type}_{task}.md')

    return  model_card_template



def fill_template(model_type: str, task: str,  meta_data:dict):
        
    temp = get_model_card_template(model_type, task)
    content = temp.render(meta_data)

    return content


