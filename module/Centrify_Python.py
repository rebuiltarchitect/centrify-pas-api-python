import requests
import json
import sys
import base64


def fetch_oauth_token(**kwargs):
    """
    This method fetches oauth access token by calling /oauth2/token/<app_id> Rest API
    """
    if 'tenant' not in kwargs or \
                    'appid' not in kwargs or \
                    'scope' not in kwargs or \
                    'clientid' not in kwargs or \
                    'clientsecret' not in kwargs:
        print("Some parameters are missing for fetch_oauth_token(). Please check.")
        sys.exit(1)
    try:
        endpoint = 'https://' + kwargs['tenant'] + "/oauth2/token/" + kwargs['appid']
        
        data = {"grant_type": "client_credentials", "scope": kwargs['scope']}
        base64string = base64.b64encode(
                                          (kwargs['clientid'] +
                                           ":" + kwargs['clientsecret']
                                          ).encode()
                                        ).decode()
        header = {"Authorization": "Basic %s" % base64string}
        


        response = requests.post(endpoint,
                                     data = data,
                                     headers = header,
                                     verify = False)
        if not response.status_code == requests.codes['ok']:
            print('Fetching of oauth token failed')
            print('Response status code: ' + str(response.status_code)
                                    +", response.text: "+ response.text)
            sys.exit(1)
        else:
            print('Oauth access token fetched successfully')
        tokens = json.loads(response.text)
        access_token = tokens['access_token']
        return access_token
    except requests.exceptions.RequestException as exc:
        print(exc)
        sys.exit(1)



        

