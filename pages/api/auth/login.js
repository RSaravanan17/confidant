// import firebase from '../../../components/firebase'
import * as firebase from "firebase/app";
import "firebase/auth";

var firebaseConfig = {
  apiKey: "AIzaSyAvZId9RM9aW5GVt-UZLcUhvUrRgqKyKEw",
  authDomain: "confidant-hacktx.firebaseapp.com",
  databaseURL: "https://confidant-hacktx.firebaseio.com",
  projectId: "confidant-hacktx",
  storageBucket: "confidant-hacktx.appspot.com",
  messagingSenderId: "822951335979",
  appId: "1:822951335979:web:afd9993ca5424bf01a326e"
};

export default (req, res) => {
    json_res = {'error': true}
    res.setHeader('Content-Type', 'application/json')
    res.statusCode(400)

    if (req.method === 'POST' && req.query != {}) {
        firebase.initializeApp(firebaseConfig);

        if (req.query.email != undefined && req.query.password != undefined) {
            firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
                res.statusCode(401)
                json_res.login_status = 'failure'
                json_res.errorMessage = error.message
            })
            if (!json_res.errorLogin) {
                res.setHeader('Content-Type', 'application/json')
                res.statusCode(200)
                json_res.error = false
                json_res.login_status = 'success'
            }
        }
        
    }
    res.end(JSON.stringify(json_res))
}