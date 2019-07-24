import requests
import os
#expcount 




def get_updates():
    token = (os.environ.get('TG_TOKEN', None))
    print("token = ",  token)
    tokenStr = str(token)
    #if token is None:
        #return
    baseUrl = "https://api.telegram.org/bot" + tokenStr + "/"
    print("baseUrl = ",  baseUrl)
    authUrl = baseUrl + "getMe"
    authUrl = "https://api.telegram.org/"
    try:
        responce = requests.get(authUrl)
        print(responce)
    except  Exception as e:
        print(str(e))
        return
    
    
if __name__ == "__main__":
    
    get_updates()
    
    
