from os import path
import pickle
from flask import current_app as app
from flask import Blueprint, request, jsonify, g
from kkbox_developer_sdk.auth_flow import KKBOXOAuth
from kkbox_developer_sdk.api import KKBOXAPI

bp = Blueprint('api', __name__)

TOKEN_FILE = 'token.pkl'

@bp.before_request
def before_request():
    token = None

    if path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as f:
            token = pickle.load(f)
        g.kkbox = KKBOXAPI(token)
        return

    auth = KKBOXOAuth(app.config['CLIENT_ID'], app.config['CLIENT_SECRET'])
    token = auth.fetch_access_token_by_client_credentials()
    g.kkbox = KKBOXAPI(token)

    with open(TOKEN_FILE, 'wb') as f:
        pickle.dump(token, f)

@bp.route('/tracks/<track_id>', methods=['GET'])
def fetchTrack(track_id):
    result = g.kkbox.track_fetcher.fetch_track(
        track_id,
        request.args['territory']
    )

    return jsonify(result)

@bp.route('/albums/<album_id>', methods=['GET'])
def fetchAlbum(album_id):
    result = g.kkbox.album_fetcher.fetch_album(
        album_id,
        request.args['territory']
    )

    return jsonify(result)

@bp.route('/albums/<album_id>/tracks', methods=['GET'])
def fetchAlbumTrack(album_id):
    result = g.kkbox.album_fetcher.fetch_tracks_in_album(
        album_id,
        request.args['territory']
    )

    return jsonify(result)

@bp.route('/search', methods=['GET'])
def fetchSearchData():
    result = g.kkbox.search_fetcher.search(
        request.args['q'],
        request.args['type'].split(","),
        request.args['territory']
    )

    return jsonify(result)
