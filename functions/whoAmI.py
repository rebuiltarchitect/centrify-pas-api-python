# Copyright 2016 Centrify Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import json
import ConfigParser
import sys

# This Python script connects to Centrify 's Identity Service
#/Security/WhoAmI #Attempts to request user info for current session.

# reading variables from config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Connect to On-Prem Service Tenant
tenant = config.get('Properties','tenant')
appid = config.get('Properties','appid')
clientid = config.get('Properties', 'clientid')
clientsecret = config.get('Properties', 'clientsecret')
scope = config.get('Properties', 'scope')
tenantId = config.get('Properties','tenantId')
bearerToken = Centrify_Python.fetch_oauth_token(tenant = tenant,
                                          appid = appid,
                                          scope = scope,
                                          clientid = clientid,
                                          clientsecret = clientsecret)

verify = False

url = 'https://%s/security/WhoAmI/' % tenant

headers = {
  'X-CENTRIFY-NATIVE-CLIENT': '1',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer %s' % bearer_token
}

r = requests.get(url, headers = headers, verify = verify)# print('response URL: ' + response.url)

r.raise_for_status
responseObject = r.json()

print '****************************************************************'
print ' '
print url
print ' '
print '****************************************************************'
print ' '
print 'Sending HTTPS POST Request for /Security/WhoAmI'
print ' '
print '****************************************************************'
print ' '
print 'JSON Response: '
print ' '
print responseObject

print ' '
print ' '
print ' '
print ' '

#EOF