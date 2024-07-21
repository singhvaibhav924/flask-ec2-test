from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
   return """
    	<h2>Welcome to my AI Chess Bot backend...</h2>
    	<p>To see this bot in action visit <a href="https://ai-chess-gd9d.onrender.com/">this URL</a></p>
    	"""

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = 8000)