from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid


app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins': "*"}})

GAMES = [
    {   'id': uuid.uuid4().hex,
        'title': '2k21',
        'genre': 'sports',
        'played': True,
    },
    {   'id': uuid.uuid4().hex,
        'title': 'The Witcher 3: Wild Hunt',
        'genre': 'RPG',
        'played': True,
    },
    {   'id': uuid.uuid4().hex,
        'title': 'Call of Duty: Modern Warfare',
        'genre': 'FPS',
        'played': False,
    },
    {   'id': uuid.uuid4().hex,
        'title': 'Among Us',
        'genre': 'party',
        'played': True,
    },
    {   'id': uuid.uuid4().hex,
        'title': 'Cyberpunk 2077',
        'genre': 'RPG',
        'played': False,
    },
    {   'id': uuid.uuid4().hex,
        'title': 'FIFA 22',
        'genre': 'sports',
        'played': True,
    },
    {   'id': uuid.uuid4().hex,
        'title': 'Minecraft',
        'genre': 'sandbox',
        'played': True,
    },
    {   'id': uuid.uuid4().hex,
        'title': 'Fortnite',
        'genre': 'battle royale',
        'played': False,
    },
    {   'id': uuid.uuid4().hex,
        'title': 'Resident Evil Village',
        'genre': 'horror',
        'played': True,
    },
    {   'id': uuid.uuid4().hex,
        'title': 'League of Legends',
        'genre': 'MOBA',
        'played': False,
    },
    {   'id': uuid.uuid4().hex,
        'title': 'Red Dead Redemption 2',
        'genre': 'action-adventure',
        'played': True,
    },
    {   'id': uuid.uuid4().hex,
        'title': 'Overwatch',
        'genre': 'FPS',
        'played': False,
    },
]


#API GET and POST route handler
@app.route('/games', methods=['GET', 'POST'])
def allGames():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game Added'
        
    else:
        response_object['games'] = GAMES
    return jsonify(response_object)


# PUT and DELETE
@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status': 'success'}
    if request.method=="PUT":
        post_data = request.get_json()
        remove_game(game_id)
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game Updated'
    if request.method == "DELETE":
        remove_game(game_id)
        response_object['message'] = 'Game Removed'
    return jsonify(response_object)
    
def remove_game(game_id):
    for game in GAMES:
        if game['id'] == game_id:
            GAMES.remove(game)
            return True
    return False

if __name__ == "__main__":
    app.run(debug=True)