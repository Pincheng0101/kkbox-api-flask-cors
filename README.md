# KKBOX API Flask CORS

KKBOX API Flask CORS for handling Cross Origin Resource Sharing, making cross-origin AJAX possible.

This is a simple demo at https://kk-search.herokuapp.com/search?q=Mayday&type=track&territory=TW.

> Demo only provide search api.

## Setting config value

1. Change `setting.cfg` value
```shell
CLIENT_ID='<CLIENT_ID>'
CLIENT_SECRET='<CLIENT_SECRET>'
ALLOW_CORS_DOMAIN='http://example.com'
```

2. Set environment variable
```shell
export CLIENT_ID='<CLIENT_ID>'
export CLIENT_SECRET='<CLIENT_SECRET>'
export ALLOW_CORS_DOMAIN='http://example.com'
```

3. Set environment variable before run server command
```shell
CLIENT_ID='<CLIENT_ID>' CLEINT_SECRET='<CLIENT_SECRET>' ALLOW_CORS_DOMAIN='http://example.com' python server.py
```

## Usage

1. Simple run server
```shell
python server.py
```

2. Use gunicorn run server
```shell
# default address:port = 0.0.0.0:8000
gunicorn kkbox_api:app

# specify address:port
gunicorn kkbox_api:app -b 127.0.0.1:6666
```

3. Deploy to HeroKu
