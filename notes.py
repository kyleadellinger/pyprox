from dotenv import load_dotenv
import requests, os, json
import urllib3 

urllib3.disable_warnings()

load_dotenv()

# any write POST/PUT/DELETE must include CSRF prevention token in header.
# tickets have a lifetime of 2 hours

userkey = os.environ["SECRET_TOKEN"]
baseUrl = os.environ["BEE_URL"]
tokenId = os.environ["TOKEN_ID"]

# access ticket
# POST /access/ticket
def proxLogin():
    '''initial login call to retrieve CSRF token, returns token'''
    at = baseUrl + "/access/ticket"
    username = os.environ["PROX_USER_FULL"]
    password = os.environ["PROX_PASS"]
    data = {
        "username": username,
        "password": password
    }
    r = requests.post(url=at, json=data, verify=False)
    try:
        r.raise_for_status()
    except:
        print(f"Error in login call. Error: {r.status_code}")
    #with open("access-response.json", "w") as ofile:
    #    ofile.write(r.text)
    response = r.json()
    return response["data"]["ticket"]


if __name__ == "__main__":
    ticket = proxLogin()




