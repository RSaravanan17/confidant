import Head from "next/head"

const HeadView = () => (
<div className="headViewer">
    <Head>
        <script type="text/javascript" src="/headViewScript.js"></script>
        <script type="text/javascript" src="/webgazer.js"></script>
    </Head>
    Test

    <style jsx>{`
        .headViewer {
            width: 100%;
            height: 90%;
            color: 'yellow';
        }
    `}</style>

</div>
)

export default HeadView