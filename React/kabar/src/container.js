import React from "react";
import ReactDOM from "react-dom/client";
import "./container.css";

function Content(props){
    return(
        <>
            <div className="content">

            </div>            
        </>
    )
}

function New({goTo, imgSrc, title, descr, category, srcNew}){
    return(
        <a href={goTo} className="news">
            <img src={imgSrc} alt={title}></img>
            <h3>{category}</h3>
            <h2>{title}</h2>
            <h4>{srcNew}</h4>
            <div className="info"></div>
        </a>
    );
}

function Grid2(){
    return(
        <div className="grid-2">
            <New goTo="" imgSrc="" title="" descr="" category="" srcNew="" ></New>
            <New goTo="" imgSrc="" title="" descr="" category="" srcNew="" ></New>
        </div>
    )
}

function Grid3(){
    return(
        <div className="grid-3">
            <New goTo="" imgSrc="" title="" descr="" category="" srcNew="" ></New>
            <New goTo="" imgSrc="" title="" descr="" category="" srcNew="" ></New>
            <New goTo="" imgSrc="" title="" descr="" category="" srcNew="" ></New>
        </div>
    )
}

export default Content;