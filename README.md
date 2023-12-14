`python3 -m venv venv`

`source venv/bin/activate`

`pip3 install -r requirements.txt`

`export GOOGLE_APPLICATION_CREDENTIALS="credentials.json"`

`flask run`

De outra aba:

`curl http://127.0.0.1:5000 | json_pp`