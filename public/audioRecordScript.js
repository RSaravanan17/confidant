
function waitForWebAudio(){
    if(typeof WebAudioRecorder !== "undefined"){
        var constraints = { audio: true, video:true }
        
        navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
    
            audioContext = new AudioContext();
            input = audioContext.createMediaStreamSource(stream);
            
            //stop the input from playing back through the speakers
            //input.connect(audioContext.destination)
            recorder = new WebAudioRecorder(input , { workerDir: "workers/" });

            recorder.setEncoding("wav")    
            recorder.setOptions({
                encodeAfterRecord: true
            })
            document.getElementById("startButton").addEventListener("click", function(){
                    console.log("TEST");
                    recorder.startRecording();
                });
                document.getElementById("stopButton").addEventListener("click", function(){
                    recorder.finishRecording();
                });
    
    
    
            recorder.onComplete = function(recorder, blob) { 
            
            }
        })   
                 
    }
    else{
        setTimeout(waitForWebAudio, 250);
    }
}

waitForWebAudio()