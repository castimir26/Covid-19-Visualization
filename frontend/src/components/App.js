import React, { Component } from "react";
import { render } from "react-dom";



class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }
  componentDidMount() {
    fetch("api/survived")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <ul>

        {this.state.data.map(Survived => {
          let page;
          if(Survived.country=="US"){
            page = <div><h2>{Survived.country} - {Survived.province}</h2><br/><h3>Recovered {Survived.recovered} - Confirmed {Survived.confirmed}</h3><br/>Deaths {Survived.deaths}</div>

          }
          else {
            page = <div><h2>{Survived.country}</h2><br/><h3>Recovered {Survived.recovered} - Confirmed {Survived.confirmed}</h3><br/>Deaths {Survived.deaths}</div>
          }
          /*
          Country -> {Survived.country}, Province -> {Survived.province}
          <br/>
          Recovered -> {Survived.recovered} - Confirmed -> {Survived.confirmed}
          */
          return (

            <li key={Survived.id}>
               {page}

            </li>




          )}
        )}

      </ul>

    );
  }
}

export default App;


const container = document.getElementById("app");
render(<App />, container);
