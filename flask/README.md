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

Next, ensure you have credentials stored in the `/etc/confidant/` directory.

There should be these files in the directory:

- `firebase-service-account.json`

## Run instructions
This API is written in Flask. To run the Flask app, use the following:

```
$ chmod u+x runflask.sh
$ ./runflask.sh
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
