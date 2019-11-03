import Head from "next/head";

const AudioRecord = () => (
    <div>
        <Head>
            <script src="/audioRecordScript.js"></script>
            <script src="/WebAudioRecorder.js"></script>
            <script src="/wavaudioencoder.js"></script>
        </Head>
        <div className="audioRecord">
            <button id="startButton" >Start</button>
            <button id="stopButton">Stop</button>
        </div>

    </div>
)

export default AudioRecord