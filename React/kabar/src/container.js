import React from "react";
import ReactDOM from "react-dom/client";
import "./container.css";


class Content extends React.Component{
  constructor(props){
  super(props);
  this.state = {
  news: [],
  }

  this.fetchApi = this.fetchApi.bind(this);
  
  // this.renderGrid = this.renderGrid.bind(this);
  }


  async fetchApi(){
  const response = await fetch('https://raw.githubusercontent.com/crijumubu/NoticiasKabar/artificial-intelligence/news/news.json');
  const data = await response.json();
  this.setState({news: data})



  return data;
  // fetch('https://raw.githubusercontent.com/crijumubu/NoticiasKabar/artificial-intelligence/news/news.json')
  // .then(res => res.json())
  // .then((data) => {
  //     this.setState({news: data})
  //     console.log(this.state.news)
  // } );

  }    

  componentDidMount(){
  this.fetchApi(this.renderGrid);
  }
  

  render(){

  const data = this.state.news.slice(0,20);
  let temp = [];

  console.log(data);
  return(
  <>
  <div className="content">
  {
    data.map((e,ind)=>{
	    temp = data.slice(ind*5,(ind+1)*5)
      try {
        return Grid(temp);
      } catch (error) {
        console.log(error)
        return <></>;
      }
  })
  }
  </div>            
  </>
  )
  }
}
// function Content(props){
  
// }

function New({Url, Image, Title, Descripcion , Category, Fuente, Id}){
  return(
  <a href={Url} className="news" key={Id}>
    <img src={Image} alt="No img"></img>
    <h3>{Category}</h3>
    <h2>{Title}</h2>
    <h4>{Fuente}</h4>
    {/* <p>{Descripcion}</p> */}
    <div className="info"></div>
  </a>
  );
}

function Grid(arr){
  return(
	<>
	  <div className="grid-2">
      <New Url={arr[0].Url} Image={arr[0].Image} Title={arr[0].Title} Descripcion={arr[0].Descripcion} Category={arr[0].Category} Fuente={arr[0].Fuente} Id="0"></New>

      <New Url={arr[1].Url} Image={arr[1].Image} Title={arr[1].Title} Descripcion={arr[1].Descripcion} Category={arr[1].Category} Fuente={arr[1].Fuente} Id="1"></New>
  </div>

  <div className="grid-3">
      <New Url={arr[2].Url} Image={arr[2].Image} Title={arr[2].Title} Descripcion={arr[2].Descripcion} Category={arr[2].Category} Fuente={arr[2].Fuente} Id="2"></New>

      <New Url={arr[3].Url} Image={arr[3].Image} Title={arr[3].Title} Descripcion={arr[3].Descripcion} Category={arr[3].Category} Fuente={arr[3].Fuente} Id="3"></New>

      <New Url={arr[4].Url} Image={arr[4].Image} Title={arr[4].Title} Descripcion={arr[4].Descripcion} Category={arr[4].Category} Fuente={arr[4].Fuente} Id="4"></New>

  </div>

	</>
  )
}



export default Content;