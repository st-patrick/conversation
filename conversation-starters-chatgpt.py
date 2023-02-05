import requests
import random

# get basics out of the way
rapidapi_key = "ddc3ca0c34msh011967171559ccfp117a35jsn1df2de149ef3"

her_name = "Alicia"
faulty_endpoints = []
timedout_endpoints = []

def get_starter(api_number=-1):
    api_endpoints = {
        "icanhazdadjoke": "https://icanhazdadjoke.com/",
        "opentdb": "https://opentdb.com/api.php?amount=1&type=multiple",
        "dad-jokes-rapidapi": "https://dad-jokes.p.rapidapi.com/random/joke",
        "love-calculator": "https://love-calculator.p.rapidapi.com/getPercentage",
        "number-fact": "http://numbersapi.com/random/trivia",
        "roast": "https://evilinsult.com/generate_insult.php?lang=en&type=json",
        "chuck-norris-joke": "https://api.chucknorris.io/jokes/random",
        "riddlie": "https://riddlie.p.rapidapi.com/api/v1/riddles/random",
        "jokeAPI": "https://v2.jokeapi.dev/joke/Any?format=txt"
    }
    
    api_headers = {
        api_endpoints["dad-jokes-rapidapi"]: {
            "x-rapidapi-host": "dad-jokes.p.rapidapi.com",
            "x-rapidapi-key": rapidapi_key
        },
        api_endpoints["love-calculator"]: {
            'X-RapidAPI-Key': rapidapi_key,
            'X-RapidAPI-Host': 'love-calculator.p.rapidapi.com'
        },
        api_endpoints["icanhazdadjoke"]: {
            "Accept": "application/json"
        },
        api_endpoints["riddlie"]: {
            'X-RapidAPI-Key': rapidapi_key,
            'X-RapidAPI-Host': 'riddlie.p.rapidapi.com'
        }
    }
    
    api_params = {
        api_endpoints["love-calculator"]: {"sname": her_name, "fname": 'Patrick'}
    }

    if api_number > -1:
        endpoint = list(api_endpoints.values())[api_number]
        if endpoint in faulty_endpoints: return "then endpoint " + endpoint + " is faulty"
    else:
        endpoint = random.choice(list(api_endpoints.values()))
        while endpoint in faulty_endpoints:
            endpoint = random.choice(list(api_endpoints.values()))
    #print(endpoint)
    headers = api_headers.get(endpoint, {}) # get headers or empty object if none
    #print(headers)
    params = api_params.get(endpoint, {}) # get params or empty object if none
    #print(params)

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        
        try:
            data = response.json()
        except:
            data = response.text    

        if endpoint == api_endpoints["icanhazdadjoke"]:
            return data["joke"]
        elif endpoint == api_endpoints["opentdb"]:
            return data["results"][0]["question"] + " ===========> " + data["results"][0]["correct_answer"]
        elif endpoint == api_endpoints["dad-jokes-rapidapi"]:
            headers = {
                "x-rapidapi-host": "dad-jokes.p.rapidapi.com",
                "x-rapidapi-key": "ddc3ca0c34msh011967171559ccfp117a35jsn1df2de149ef3"
            }
            return data["body"][0]["setup"] + " - " + data["body"][0]["punchline"]
        elif endpoint == api_endpoints["love-calculator"]:
            return f"{her_name} and Patrick are {data['percentage']}% in love"
        elif endpoint == api_endpoints["roast"]:
            return data["insult"]
        elif endpoint == api_endpoints["chuck-norris-joke"]:
            return data["value"]
        elif endpoint == api_endpoints["riddlie"]:
            return data['riddle'] + " =======> " + data['answer']
        else:
            return data
            
    except TimeoutException as e: # handle differently because it could also be the user's internet
        # handle timeout exception in a specific way
        if endpoint in timedout_endpoints: # if this is the second bad request, ass to faulty ones but also suggest checking internet
            print("connection timed out. Maybe check your internet connection")
            faulty_endpoints.append(endpoint)
        else:
            timedout_endpoints.append(endpoint)
        return get_starter() #try again. Though nested calls are certainly not a great solution
        
    except Exception as e:
        faulty_endpoints.append(endpoint)
        return get_starter() #try again. Though nested calls are certainly not a great solution
    

    

        
#for i in range(9): # test all endpoints in order for debugging
print(get_starter(8)) # todo: put in a try block and just use a different endpoint if there is an error and possibly remember the faulty endpoint
print("\nfaulty endpoints: ")
print(faulty_endpoints)