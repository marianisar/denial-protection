#############################################################################
#                                                                           #
#                       Copyright 2019 MARIA NISAR.                         #
#                           All Rights Reserved.                            #
#                                                                           #
#                                                                           #
#############################################################################
'''
Created on SEP 16, 2019

@author: Maria Nisar
'''

import requests
import sys


if __name__=="__main__":
    user_id=input('Enter the number of HTTP clients to simulate :')
    data={'user_id':user_id}
    url='http://localhost:8080'

    req=requests.post(url,data=data)

    sys.stdout.write((req.content)+'\n')
