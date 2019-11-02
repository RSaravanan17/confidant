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
        </div>
        <style jsx>{`
            .fullscreen {
                width: 100vw;
                height: 100vh;
                color: 'black';
                position: absolute;
                overflow: hidden;
                padding-right: 0px;
                padding-left: 0px;
                margin: 0;
            }
        `}</style>
    </div>
  )
  
  export default App