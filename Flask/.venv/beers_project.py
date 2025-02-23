# filepath: /home/adi/Python-Projects/Flask/.venv/beers_project.py
from flask import Flask, jsonify, abort

beers = {
"1": {'id': 1, "name": "Goldstar", "country": "Israel"},
"2": {'id': 2, "name": "Carlsberg", "country": "Denmark"}
}

app = Flask("beers")

@app.route('/beers')
def get_all_beers():
    all_beers = list(beers.values())
    return jsonify(all_beers)

@app.route('/beers/<beerid>')
def get_a_single_beer(beerid):
    if beerid not in beers:
        abort(404, description="Beer not found")
    this_beer = beers[beerid]
    return jsonify(this_beer)



if __name__ == '__main__':
    app.run()