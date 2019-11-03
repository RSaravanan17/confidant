import Head from "next/head"
import buttonInstance from "./calibration"

class HeadView extends React.Component {
    constructor(props){
        super(props);
        this.state = {number: 1, left:'350px', top:'25px'};
        this.counter = 5;
        this.leftDists = ['350px', '600px', '150px', '800px', '350px', '600px'];
        this.topDists = ['25px', '325px', '625px'];
    }

    onClick = () => {
        if (this.counter > 1) {
            this.counter--;
        } else {
            this.counter = 5;
            var curNumber = this.state.number;
            this.setState({number: curNumber + 1, left: this.leftDists[curNumber], top: this.topDists[Math.floor(curNumber / 2)]});
        }
    }

    render() {
        return (
            <div className="headViewer">
                <Head>
                    <script type="text/javascript" src="/headViewScript.js"></script>
                    <script type="text/javascript" src="/webgazer.js"></script>
                </Head>
                Test

                <button onClick={this.onClick} style={{height:'50px', width:'50px', background:'#1c4587', color:'white', position:'absolute', left:this.state.left, top:this.state.top}}>
                    {this.state.number}
                </button>

                <style jsx>{`
                    .headViewer {
                        width: 100%;
                        height: 90%;
                        color: 'yellow';
                    }
                `}</style>
            </div>
        );
        
    }

}

export default HeadView