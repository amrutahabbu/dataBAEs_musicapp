## ALL THE CONFIGURATIONS GO HERE

import os
from sqlalchemy import *
from astrapy.db import AstraDB

def connect_AstraDB():
    # Initialize the client
    db = AstraDB(
        token="AstraCS:cJRHkPPfbcQCaJFKxnFjJoUE:d0eb7d0643c1255dd583daac12a86710650813c6f97f407b42399746d77be7a4",
        api_endpoint="https://be61fb62-4f40-45db-8cd0-14c061a597ff-us-east-1.apps.astra.datastax.com")

    print("Connected to Astra DB")
    return db

def getOpenAIKey():

    api_key = "add_your_key"
    return api_key
