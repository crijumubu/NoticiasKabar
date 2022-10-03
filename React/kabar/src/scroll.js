import React, { useState, useEffect } from "react";
import "./scroll.css";

const Scroll = () => {
    const [showTopBtn, setShowTopBtn] = useState(false);
    useEffect(() => {
        window.addEventListener("scroll", () => {
            if (window.scrollY > 400) {
                setShowTopBtn(true);
            } else {
                setShowTopBtn(false);
            }
        });
    }, []);
    const goToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        });
    };
    return (
        <div className="top-to-btm">
            {" "}
            {showTopBtn && (
                <i className="bi bi-arrow-up-short icon-position icon-style" onClick={goToTop}></i>
            )}{" "}
        </div>
    );
};
export default Scroll;