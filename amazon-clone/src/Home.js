import React from 'react';
import "./Home.css";
import Product from './Product';

function Home() {
  return (
    <div className='home'>
      <div className='home__container'>
        <img 
          className='home__image'
          src="https://media.licdn.com/dms/image/v2/C5112AQE9cMJ6jKIZtg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1585711743157?e=2147483647&v=beta&t=I0oxluozH5wiTroJpLP9lSumXZn53jR3RTrYD2HM0ME"
          alt=""
        />
      </div>

      <div className='home__row'>
        <Product/>
      </div>

      <div className='home__row'>
        {/* Product */}
        {/* Product */}
        {/* Product */}
      </div>

      <div className='home__row'>
        {/* Product */}
      </div>
    </div>
  );
}

export default Home
