from flask import Flask

app = Flask(__name__)

@app.roude('/')
def home():
  return "Flask heroku app"

if __name__ == '__main__':
  app.run()
