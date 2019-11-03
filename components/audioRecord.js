import Head from "next/head";

const AudioRecord = () => (
    <div>
        <Head>
        <script
			  src="https://code.jquery.com/jquery-3.4.1.js"
			  integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU="
			  crossorigin="anonymous"></script>
            <script src="/audioRecordScript.js"></script>
            <script src="/WebAudioRecorder.js"></script>
            
        </Head>
        <div className="audioRecord">
            <button id="startButton" >Start</button>
            <button id="stopButton">Stop</button>
        </div>
        
    </div>
)

export default AudioRecord