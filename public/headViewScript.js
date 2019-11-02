
function waitForWebgazer(){
    if(typeof webgazer !== "undefined"){
        webgazer.setGazeListener(function(data, elapsedTime){
            if (data == null) {
                return;
            }
            var xprediction = data.x; //these x coordinates are relative to the viewport
            var yprediction = data.y; //these y coordinates are relative to the viewport
            console.log(elapsedTime); //elapsed time is based on time since begin was called
            console.log("coords are x: " + xprediction + ", y: " + yprediction);
        }).begin();
    }
    else{
        setTimeout(waitForWebgazer, 250);
    }
}

waitForWebgazer()