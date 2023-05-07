#Imports
from manifoldpy import api
import requests
import numpy as np
import scipy as sp
from time import sleep, time
from collections import namedtuple
from traceback import print_exception
from requests.exceptions import ConnectionError
import random
from sys import argv
from time import time

#Bot account details
YOUR_API_KEY = ""
USER_ID = ""
USERNAME = ""
GODNAME = "firstuserhere"
wrapper = api.APIWrapper(YOUR_API_KEY)

def make_market():
    key = YOUR_API_KEY
    wrapper = api.APIWrapper(key)
    close = int(time()) * 1000 + 10000
    resp = wrapper.create_market(
        "BINARY",
        "QUESTIONS",
        "This is basically a DESCRIPTION!",
        close,
        ["test", "api"],
        initialProb= 50,
    )
    print(resp.text)



#place bet aka exploit
def exploit(market):
    outcome = "NO" if market.probability<= 0.4 else "YES" #define the strategy
    amount = 4
    id = market.id
    wrapper.make_bet(amount, id, outcome)

#Target name ;)
# target = "firstuserhere"
# def should_exploit(market):
#     if market.creatorName != GODNAME:
#         return False
#     #skip markets if not binary
#     if market.outcomeType != 'BINARY' or market.mechanism != 'cpmm-1':
#         return False
    
#     #Don't bet if the market is resolved
#     if market.isResolved:
#         return False
#     return True

# def exploit_target():
#     user = api.get_user_by_name(target)
#     markets = api.get_markets(1000)
#     for m in markets:
#         if should_exploit(m):
#             exploit(m)
    
if __name__ == "__main__":
#call functions whatever
    make_market()
    market = api.get_market("")
    exploit(market)
