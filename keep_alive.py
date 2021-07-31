# this part of code is only to keep the bot running 7/7 24

from flask import Flask
from threading import Thread 

app = Flask ('')

@app.route('/')
def home():
  return "Hello. I am alive!" 

def run(): 
  app.run(host='0.0.0.0', port=8080)
def keep_alive():
  t = Thread(target=run)
  t.start()