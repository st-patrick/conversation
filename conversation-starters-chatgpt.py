import requests
import random

her_name = "Alicia"

def get_starter():
    api_endpoints = {
        "icanhazdadjoke": "https://icanhazdadjoke.com/",
        "opentdb": "https://opentdb.com/api.php?amount=1&type=multiple",
        "dad-jokes-rapidapi": "https://dad-jokes.p.rapidapi.com/random/joke",
        "love-calculator": "https://love-calculator.p.rapidapi.com/getPercentage",
    }
    
    api_headers = {
        api_endpoints["dad-jokes-rapidapi"]: {
            "x-rapidapi-host": "dad-jokes.p.rapidapi.com",
            "x-rapidapi-key": "ddc3ca0c34msh011967171559ccfp117a35jsn1df2de149ef3"
        },
        api_endpoints["love-calculator"]: {
            'X-RapidAPI-Key': 'ddc3ca0c34msh011967171559ccfp117a35jsn1df2de149ef3',
            'X-RapidAPI-Host': 'love-calculator.p.rapidapi.com'
        },
        api_endpoints["icanhazdadjoke"]: {
            "Accept": "application/json"
        }
    }
    
    api_params = {
        api_endpoints["love-calculator"]: {"sname": her_name, "fname": 'Patrick'},
    }

    endpoint = random.choice(list(api_endpoints.values()))
    print(endpoint)
    headers = api_headers.get(endpoint, {}) # get headers or empty object if none
    #print(headers)
    params = api_params.get(endpoint, {}) # get params or empty object if none
    #print(params)

    response = requests.get(endpoint, headers=headers, params=params)
    data = response.json()
    
    
    
    if endpoint == api_endpoints["icanhazdadjoke"]:
        return data["joke"]
    elif endpoint == api_endpoints["opentdb"]:
        return data["results"][0]["question"]
    elif endpoint == api_endpoints["dad-jokes-rapidapi"]:
        headers = {
            "x-rapidapi-host": "dad-jokes.p.rapidapi.com",
            "x-rapidapi-key": "ddc3ca0c34msh011967171559ccfp117a35jsn1df2de149ef3"
        }
        return data["body"][0]["setup"] + " - " + data["body"][0]["punchline"]
    elif endpoint == api_endpoints["love-calculator"]:
        return f"Compatibility: {data['percentage']}% - {data['result']}"

print(get_starter())