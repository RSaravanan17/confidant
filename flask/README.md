# Flask API

## Implementation details
The API was written in Python 3 using Flask and Requests.

## Installation instructions
First, create a virtualenv and `source` into it:

```
$ virtualenv virtualenv
$ source virtualenv/bin/activate
```

To install dependencies, use pip3.

```
$ pip3 install -r requirements.txt
```

## Run instructions
This API is written in Flask. To run the Flask app, use the following:

```
$ sudo env FLASK_APP=app.py flask run -h 0.0.0.0 -p 443
```

## Using the API

### `GET /v1/blahblah`

Request:

Send as params.
```
'email': 'email@gmail.com'
'passwordHash': 'xyz'
```

Response:

Sent back as a JSON object in a string.
```
{
  'logintoken': 'blahblah'
}
```
