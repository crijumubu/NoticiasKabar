import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Content from './container';
import Footer from './footer';

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <>
        <Content></Content>
        <Footer></Footer>
    </>
);
