import argparse
from module import Centrify_Python


from configparser import ConfigParser
# reading variables from config file
config = ConfigParser()
config.read('config/config.ini')

# Connect to On-Prem Service Tenant
tenant = config.get('Properties','tenant')
appid = config.get('Properties','appid')
clientid = config.get('Properties', 'clientid')
clientsecret = config.get('Properties', 'clientsecret')
scope = config.get('Properties', 'scope')
tenantId = config.get('Properties','tenantId')
verify = False


print ('****************************************************************')
bearerToken = Centrify_Python.fetch_oauth_token(tenant = tenant,
                                          appid = appid,
                                          scope = scope,
                                          clientid = clientid,
                                          clientsecret = clientsecret)

print ('****************************************************************')
print (bearerToken)
print ('****************************************************************')
#EOF

from module.Logger import BasicClass

 
number = BasicClass()
number.configure_logger()
number.increment_number()
number.increment_number()
print ("Current number: %s" % str(number.current_number))
number.clear_number()
print ("Current number: %s" % str(number.current_number))
