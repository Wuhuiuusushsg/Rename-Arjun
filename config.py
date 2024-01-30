#Arjun


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20054245")

API_HASH = os.environ.get("API_HASH", "431f22f320ed5d69225d3b3fc253fc0d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6860503221:AAEG6n_b9I9wUredGVageZTwmy92pfApRpI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "apni_kaksha_live") 

  
            

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://arpanh980:MVDM6mJXHLndnV0z@cluster0.rshyyjt.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5034929962').split()]

PORT = os.environ.get("PORT", "8080")

# Arjun
