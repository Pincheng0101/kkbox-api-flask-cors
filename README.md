# KKBOX API Flask CORS

KKBOX API Flask CORS for handling Cross Origin Resource Sharing, making cross-origin AJAX possible.

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
