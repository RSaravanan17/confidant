var recorder; 						//WebAudioRecorder object
var input; 				
var audioContext; //new audio context to help us record
function startRec(){
    var constraints = { audio: true, video:false }
        
    navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
        audioContext = new AudioContext();
        input = audioContext.createMediaStreamSource(stream);
        
        //stop the input from playing back through the speakers
        //input.connect(audioContext.destination)
        recorder = new WebAudioRecorder(input , { workerDir: "workers/", 
            onEncoderLoading: function(rec, encoding) {
                // show "loading encoder..." display
                console.log("Loading encoder...");
            },
            onEncoderLoaded: function(rec, encoding) {
            // hide "loading encoder..." display
                console.log("encoder loaded");
            }, 
            onEncodingProgress: function(re, progress) { 
                console.log("progress: " + progress)
            }
        });
        recorder.setOptions({
            encodeAfterRecord: true
        })
        recorder.onComplete = function(re, blob){
            console.log("complete")
            let fd = new FormData();
            fd.append('fname', 'upload.wav');
            fd.append('data', blob);
            $.post({
                url: 'http://localhost:5000/v1/audioupload',
                data: fd,
                processData: false,
                contentType: false
            });
        }
        recorder.startRecording();
    })   
}

function waitForWebAudio(){
    if(typeof WebAudioRecorder !== "undefined" && typeof $ !== "undefined"){
        document.getElementById("startButton").addEventListener("click", function(){
            startRec();
        });
        document.getElementById("stopButton").addEventListener("click", function(){
            recorder.finishRecording();
            console.log("finish recording")
        });
        
                 
    }
    else{
        setTimeout(waitForWebAudio, 250);
    }
}

waitForWebAudio()   
