
function waitForWebAudio(){
    if(typeof WebAudioRecorder !== "undefined"){
        webgazer.setGazeListener(function(data, elapsedTime){
            alert("TE")

            recorder = new WebAudioRecorder("source", { workerDir: "javascripts/" });

            recorder.setEncoding("wav")
            recorder.startRecording()

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
                
        }).begin();
    }
    else{
        setTimeout(waitForWebAudio, 250);
    }
}

waitForWebAudio()