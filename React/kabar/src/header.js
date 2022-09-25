import React from "react";
import ReactDOM from "react-dom/client";
import "./header.css";

function Header () {
    return (
      <header className="search">
        <form>
          <SearchBar holdTxt="¿Que desea buscar?" />
          <SubmitBtn />
        </form>
      </header>
    );  
}

function SearchBar({holdTxt}) {
  return <input type="search" className="search-inp" placeholder={holdTxt}></input>;
}

function SubmitBtn(){
    return(
        <button type="submit" className="search-btn">
            <i className="bi bi-search icon-search"></i>
        </button>
    )
}

export default Header;
