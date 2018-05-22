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

@bp.route('/artists/<artist_id>', methods=['GET'])
def fetchArtist(artist_id):
    result = g.kkbox.artist_fetcher.fetch_artist(
        artist_id,
        request.args['territory']
    )

    return jsonify(result)

@bp.route('/artists/<artist_id>/albums', methods=['GET'])
def fetchArtistAlbum(artist_id):
    result = g.kkbox.artist_fetcher.fetch_albums_of_artist(
        artist_id,
        request.args['territory']
    )

    return jsonify(result)

@bp.route('/artists/<artist_id>/top-tracks', methods=['GET'])
def fetchArtistTopTrack(artist_id):
    result = g.kkbox.artist_fetcher.fetch_top_tracks_of_artist(
        artist_id,
        request.args['territory']
    )

    return jsonify(result)

@bp.route('/artists/<artist_id>/related-artists', methods=['GET'])
def fetchArtistRelated(artist_id):
    result = g.kkbox.artist_fetcher.fetch_related_artists(
        artist_id,
        request.args['territory']
    )

    return jsonify(result)

@bp.route('/shared-playlists/<playlist_id>', methods=['GET'])
def fetchSharedPlayList(playlist_id):
    result = g.kkbox.shared_playlist_fetcher.fetch_shared_playlist(
        playlist_id,
        request.args['territory']
    )

    return jsonify(result)

@bp.route('/shared-playlists/<playlist_id>/tracks', methods=['GET'])
def fetchSharedPlayList(playlist_id):
    result = g.kkbox.shared_playlist_fetcher.fetch_shared_playlist(
        playlist_id,
        request.args['territory']
    )

    return jsonify(result)

@bp.route('/featured-playlist-categories', methods=['GET'])
def fetchFeaturedCategory():
    result = g.kkbox.feature_playlist_category_fetcher.fetch_categories_of_feature_playlist(
        request.args['territory']
    )

    return jsonify(result)

@bp.route('/featured-playlist-categories/<category_id>', methods=['GET'])
def fetchSingleFeaturedCategory(category_id):
    result = g.kkbox.feature_playlist_category_fetcher.fetch_feature_playlist_by_category(
        category_id,
        request.args['territory']
    )

    return jsonify(result)

@bp.route('/featured-playlist-categories/<category_id>/playlists', methods=['GET'])
def fetchFeaturedCategoryPlayList(category_id):
    result = g.kkbox.feature_playlist_category_fetcher.fetch_playlists_of_feature_playlist_category(
        category_id,
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
