import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Content from './container';
import Header from './header';
import AsideBar from './aside';

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <>
        <Header></Header>
        {/* <AsideBar></AsideBar> */}
        <Content></Content>
    </>
);
