import Head from 'next/head'
import dynamic from 'next/dynamic'

const HeadView = dynamic(
  () => import('../components/headView'),
  { ssr: false }
)
const AudioRecord = dynamic(
    () => import('../components/audioRecord'),
    { ssr: false }
)
const App = () => (
    <div>
    
        <Head>
            <title>Confidant Application Viewer</title>
            <link rel='icon' href='/favicon.ico' /> 
        </Head>
        <div className="fullscreen">
            <HeadView />
            <AudioRecord />
            
            <div id="reportCard">
                <h3 id="eyeContactScore"></h3>
            </div>
        </div>
        <style jsx>{`
            .fullscreen {
                width: 100vw;
                height: 100vh;
                color: 'black';
                position: fixed;
                overflow: hidden;
                padding-right: 0px;
                padding-left: 0px;
                margin: 0;
                background-color:#f3f3f3ff;
            }
            #reportCard {
                top: 30%;
                height: 70%;
            }

        `}</style>
    </div>
  )
  
  export default App