from core.database import Database
from core.transaction import Transaction
from core.block import Block
from core.genesis import Genesis
import json
import time
import pickle
import random
import string
import requests
from crypto.basic import *
genesisBlock = Genesis.genesis()
firstTransaction = genesisBlock['transaction'][0]
#print(firstTransaction["to"], firstTransaction["out"])

db = Database()
db.blockDB.deleteAll()
db.transactionDB.deleteAll()
db.rootDB.deleteAll()
db.balanceDB.deleteAll()
genesisAccount = {"address":'cxa65cfc9af6b7daae5811836e1b49c8d2570c9387', "balance":{"cic":1000,"now":100}, "nonce":0}
db.balanceDB.put('cxa65cfc9af6b7daae5811836e1b49c8d2570c9387'.encode(), pickle.dumps(genesisAccount))
feeAccount = {"address": "cxtest", "balance":{"cic":1000}, "nonce":0}
db.balanceDB.put('cxtest'.encode(), pickle.dumps(feeAccount))
db.createBlock(genesisBlock)
print('block 0:',db.getBlockByID(0))
#key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(38))

key = '97ddae0f3a25b92268175400149d65d6887b9cefaf28ea2c078e05cdc15a3c0a'

#print(key)
t = time.time()
for i in range(10):
	transactions = []
	transaction = {}
	transaction['fee'] = '10'
	transaction['to'] = 'cx' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(38))
	transaction['out'] = {'cic':str(random.randint(10,20)),'now':str(random.randint(5,10))}
	transaction['nonce'] = str(i+1)
	transaction = Transaction.newTransaction(transaction, key)
	print(transaction)
	
	#print(transaction['txid'])
	transactions.append(transaction)
	data = {'method':'sendTransaction', 'param':[transaction]}
	headers = {'Content-Type':'application/json'}
	r = requests.post('http://192.168.51.201:9000', headers = headers, data = json.dumps(data))
	#print(r.text)
print((time.time()-t))
"""
{'privateKey': '8c1eba13a46fd0e18ee22e5e3da7cf139977090040622a83', 'version': '1', 
'address': 'cx6e3d4550ef058740705ebc7fcf392379c72f11fc', 'type': 'cic', 
'publicKey': 'bbc60d5af15a41d01323a22e43bbdcd1b2045b6d931c877cef8dd2153fdf4617b4839ad71e083da8d6dae8b0aff0c058'}
"""