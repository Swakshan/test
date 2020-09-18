import requests
from flask import Flask

app = Flask(__name__)

#url = "https://www.cricbuzz.com/api/cricket-match/commentary/30119"
url="https://www.cricbuzz.com/live-cricket-scores/30119/lancs-vs-yorks-north-group-t20-blast-2020"
req = requests.get(url)
#pkjson = req.json()

@app.route('/')
def index():
    s=req.text

    return s

@app.route('/t')
def test():
    return 'test'


# def team1short():
#     name = pkjson['matchHeader']['team1']['shortName']
#     return name

if __name__ == '__main__':
    app.run(debug=True)
