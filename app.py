import random
import re
from flask import Flask, request, Response, json
app = Flask(__name__, static_url_path='')

app.config['DEBUG'] = True

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/query', methods=['POST'])
def query():
    body = request.get_json()
    query = body.get('query')
    data = json.dumps(autocomplete(query))
    return Response(data, status=200, mimetype='application/json')

input_features = [
    'code snippet',
    'availability',
    'table',
    'Email tracking',
    'Giphy',
    'PDF Slideshow',
    'Article',
    'SMS Me',
    'Secret Message',
    'Encryption',
    'Poll',
    'Public Poll',
    'Send Later',
    'Send Later with tracking',
    'Link Preview',
    'Yes/No',
    'Question and Answer',
    'Forms in Email',
    'Forms in pages',
    'Email templates',
    'Gists',
    'Google Maps integration'
];

def autocomplete(query):
    query = query.lower()
    result = []
    if (not query):
        return input_features
    for i in input_features:
        temp = str(i.lower())
        temp = temp.split(' ')
        for j in temp:
            if re.match(query, j):
                result.append(i)

    return result

if __name__ == '__main__':
    app.run()
