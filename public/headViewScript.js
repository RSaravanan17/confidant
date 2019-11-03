
function waitForWebgazer(){
    if(typeof webgazer !== "undefined" && typeof $ !== "undefined"){
        $.post({
            url: 'http://localhost:5000/v1/firstQ',
        });
        webgazer.setGazeListener(function(data, elapsedTime){
            if (data == null) {
                return;
            }

            var xprediction = data.x;  // these x coordinates are relative to the viewport
            var yprediction = data.y;  // these y coordinates are relative to the viewport
        }).begin();
    }
    else{
        setTimeout(waitForWebgazer, 250);
    }
}

waitForWebgazer()