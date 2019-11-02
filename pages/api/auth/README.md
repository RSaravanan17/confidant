Use `signup.js` for signing users up and `login.js` for logging them in.

Send in a query string:
```
{
    'email': '...',
    'password': '...'
}
```

You get back a JSON string.

```
{
    error: false,
    login_status: 'success'
}
```

`error` is false unless there is an error. `login_status` is either `success` or `failure` on successful/failed user creation/login.


To check if a user is signed in:
```
var user = firebase.auth().currentUser;

if (user) {
  // User is signed in.
} else {
  // No user is signed in.
}
```

Get profile info of a user:
```
var user = firebase.auth().currentUser;
var name, email, photoUrl, uid, emailVerified;

if (user != null) {
  name = user.displayName;
  email = user.email;
  photoUrl = user.photoURL;
  emailVerified = user.emailVerified;
  uid = user.uid;  // The user's ID, unique to the Firebase project. Do NOT use
                   // this value to authenticate with your backend server, if
                   // you have one. Use User.getToken() instead.
}
```