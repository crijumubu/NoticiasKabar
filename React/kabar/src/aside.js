import React from "react";
// import ReactDOM from "react-dom/client";
import "./aside.css";

function AsideBar(){
  return(
    <aside className="side-bar">
      <nav>
        <Link icon="bi bi-newspaper" linkText="Kabar"></Link>
        <Link icon="bi bi-person-square" linkText="Kabar" goTo=""></Link> {/*! Link a pagina de inicio de sesion */} 
        <Link icon="bi bi-search" linkText="Kabar" goTo="#search"></Link> {/*! Link a pagina de inicio de sesion */} 
        <Link icon="bi bi-funnel" linkText="Kabar" ></Link> {/*! Abrir filtros */} 

      
      </nav>
    </aside>
  )
}

function Link({icon,linkText, goTo ="#"}){
  return (
    <a href={goTo} className="link-side">
        <i className={`${icon} icon`}>
            <p>{linkText}</p>
        </i>
    </a>
  );
}

export default AsideBar;