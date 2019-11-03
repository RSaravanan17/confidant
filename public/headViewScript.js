
function waitForWebgazer(){
    if(typeof webgazer !== "undefined"){
        var good = 0;  // number of gazes within bounding box
        var total = 0;  // number of gazes total

        webgazer.setGazeListener(function(data, elapsedTime){
            if (data == null) {
                return;
            }

            var xprediction = data.x;  // these x coordinates are relative to the viewport
            var yprediction = data.y;  // these y coordinates are relative to the viewport
            
            total++;

            // bounding box for gaze
            if (xprediction > 350 && xprediction < 600 && yprediction > 25 && yprediction < 625) good++;

        }).begin();
    }
    else{
        setTimeout(waitForWebgazer, 250);
    }
}

waitForWebgazer()