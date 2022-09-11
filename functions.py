import requests
from datetime import datetime

timezoneapikey = "acDmknoIUzJkoUZYemqS"
(requests.get('https://timezoneapi.io/api/ip/?token={timezoneapikey}&ip={Ip}')).json()

def printname(name):
    return name

def GetTime(Message, Ip, UserId):
    res = (requests.get(f'https://timezoneapi.io/api/ip/?token={timezoneapikey}&ip={Ip}')).json()
    Time = datetime.strptime(res['data']['datetime']['date_time'], '%m/%d/%Y %H:%M:%S').strftime('%I:%M %p')

    return  {
            "commend": f"It's {datetime.strptime(((requests.get(f'https://timezoneapi.io/api/ip/?token={timezoneapikey}&ip={Ip}')).json())['data']['datetime']['date_time'], '%m/%d/%Y %H:%M:%S').strftime('%I:%M %p')}",
            "SFunction": "",
            "CFunction": "",
            "CFunctionPrams": {} 
        }
    
    

def GetDate(Message, Ip, UserId):
    res = (requests.get(f'https://timezoneapi.io/api/ip/?token={timezoneapikey}&ip={Ip}')).json()
    Date = datetime.strptime(res['data']['datetime']['date_time'], '%m/%d/%Y %H:%M:%S').strftime('%A, %B %d, %Y')

    return {
        "commend": f"It's {Date}",
        "SFunction": "",
        "CFunction": "",
        "CFunctionPrams": {} 
    }

AssistantName = 'EDITH'
Oname = {"name": "yousefi", "type": "family/person"}


def WhatIsMyName(Message, Ip, UserId):
    return {
        "commend": "sorry, I'm not yet able to detect people",
        "SFunction": "",
        "CFunction": "",
        "CFunctionPrams": {} 
    }

def WhoAmI(Message, Ip, UserId):
    return {
        "commend": "sorry, I'm not yet able to detect people",
        "SFunction": "",
        "CFunction": "",
        "CFunctionPrams": {} 
    }


def TellJoke(Message, Ip, UserId):
    res = ((requests.get('https://v2.jokeapi.dev/joke/Any?type=single')).json())['joke']
    return {
        "commend": res,
        "SFunction": "",
        "CFunction": "",
        "CFunctionPrams": {} 
    }


def WhatIsYourName(Message, Ip, UserId):
    return {
        "commend": f"I'm {AssistantName}",
        "SFunction": "",
        "CFunction": "",
        "CFunctionPrams": {} 
    }
    
def WhoAreYou(Message, Ip, UserId):
    return {
        "commend": f"I'm {AssistantName}",
        "SFunction": "",
        "CFunction": "",
        "CFunctionPrams": {} 
    }

# print(GetJoke('hello world', "88.228.76.167", 1))