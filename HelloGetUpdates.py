import requests
#expcount 
token = ""
baseUrl = "https://api.telegram.org/bot" + token + "/"



def get_updates():
    authUrl = baseUrl + "getMe"
    authUrl = "https://api.telegram.org/"
    responce = requests.get(authUrl)
    print(responce)
    

get_updates()
    
