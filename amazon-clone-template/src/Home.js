import React from 'react';
import "./Home.css";
import Product from './Product';

function Home() {
  return (
    <div className='home'>
      <div className='home__container'>
        <img 
          className='home__image'
          src="https://www.shutterstock.com/image-photo/buenos-aires-argentina-08142023-logo-260nw-2347424263.jpg"
          alt=""
        />
      </div>

      <div className='home__row'>
        <Product/>
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
