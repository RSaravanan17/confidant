import React from 'react'
import Head from 'next/head'
import Nav from '../components/nav'
import Link from 'next/link'

const Home = () => (
  <div id = "overallDiv">
    <Head>
      <title>Confidant</title>
      <link rel='icon' href='/favicon.ico' />
    </Head>
    <Nav />

    <div className='hero'>
      <img className = "centerImage" src="./Confidant_Logo_2.png"/>
      <p className='description'>
        
      </p>

      <div className='row'>
        <div className='card'>
          <Link href='/app' >
            <a>
            <h3>Demo &rarr;</h3>
            <p>Learn about Confidant by following an interactive demo!</p>
            </a>
          </Link>

        </div>
      </div>
    </div>

    <style jsx>{`
      #overallDiv{
        height: 100vh;
      }
      .hero {
        width: 100%;
        background-color: #f3f3f3ff;
      }

      .centerImage{
        display: block;
        margin-left: auto;
        margin-right: auto;
      }
      #logoDiv{
        background-size: contain;
        background: #ffffff;

        background-image: url('./Confidant_Logo_2.png');
        min-height: 28.333333333vw;
        width: 100vw;
      }
      .title {
        margin: 0;
        width: 100%;
        padding-top: 80px;
        line-height: 1.15;
        font-size: 48px;
      }
      .title,
      .description {
        text-align: center;
      }
      .row {
        max-width: 880px;
        margin: 30px auto 40px;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
      }
      .card {
        padding: 18px 18px 24px;
        width: 220px;
        text-align: left;
        text-decoration: none;
        color: #434343;
        border: 1px solid #9b9b9b;
      }
      .card:hover {
        border-color: #067df7;
      }
      .card h3 {
        margin: 0;
        color: #067df7;
        font-size: 18px;
      }
      .card p {
        margin: 0;
        padding: 12px 0 0;
        font-size: 13px;
        color: #333;
      }
    `}</style>
  </div>
)

export default Home
