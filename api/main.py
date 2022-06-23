from flask import Flask, request
from flask import jsonify
import requests
import json



app = Flask(__name__)
api_key = "YOUR_TOKEN"
my_headers = {'Authorization' : f"{api_key}", 'Content-Type' : 'application/json'}

@app.route("/")
def hello_world():
    return jsonify(
        message="Hello, World"
    )

#Status endpont
@app.route("/v1/status")
def status():
    return jsonify(
        State="Ok",
        message="Everithing is working..."
    )

#Short long url
@app.route('/api/v1/generate_url/', methods=['POST'])
def gen_short_url():
    try:
        shortened_url = ""
        json_req = request.get_json(force=True)
        if json_req.get('long_url') is None:
            return jsonify({'message': 'Bad request'}), 400

        long_url = json_req['long_url']
        print(long_url)
        bitly_json = {"long_url": ""+long_url+"","domain": "bit.ly"}
        bitly_res = requests.post('https://api-ssl.bitly.com/v4/shorten' , headers=my_headers,  json=bitly_json)
        bitly_res.raise_for_status()
        long_res = bitly_res.json()
        if long_res.get('link') is None:
            return jsonify({'message': long_res}), 400
        
        shortened_url = long_res['link']
        response = {'message': 'success', 'long_url': long_url, 'short_url': shortened_url}
        return jsonify(response)
    except requests.exceptions.HTTPError as error:
        return jsonify({'error': str(error)}), 500

# Unshort url
@app.route('/api/v1/unshort_url/', methods=['POST'])
def unshort_url():
    json_req = request.get_json(force=True)
    if json_req.get('short_url') is None:
        return jsonify({'message': 'Bad request'}), 400

    session = requests.Session()  # so connections are recycled
    resp = session.head(json_req['short_url'], allow_redirects=True)
    
    response = {'message': 'success', 'short_url': json_req['short_url'], 'long_url': resp.url}
    return jsonify(response)


# run the app.
if __name__ == "__main__":
    app.debug = True
    app.run()
