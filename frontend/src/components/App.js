import React, { useState, useEffect, useRef, Component } from "react";
import { Form, ListGroup, Jumbotron } from 'react-bootstrap';
import { render } from "react-dom";
import {Line} from 'react-chartjs-2';


function Search() {
  const [query, setQuery] = useState('')
  const [countries, setCountries] = useState([])
  const focusSearch = useRef(null)

  useEffect(() => {focusSearch.current.focus()}, [])

  const getCountries = async (query) => {
    const results = await fetch(`/api/survived/?search=${query}`, {
      headers: {'accept': 'application/json'}
    })

    const countriesData = await results.json()

    return countriesData

  }
  const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms))
  }
  useEffect(() => {
    let currentQuery = true
    const controller = new AbortController()
    const loadCountries = async () => {
      if (!query)  return setCountries([])

      await sleep(350)
      if (currentQuery) {
        const countries = await getCountries(query, controller)

        setCountries(countries);


      }
    }
    loadCountries()

    return () => {
      currentQuery = false
      controller.abort()
    }
  }, [query]
)
let countryComponents = countries && countries.map((country, index) => {
  return (
    <ListGroup.Item key={index} action variant="secondary">
       Currently showing information for: {country.country}
       <br />
       Recovered {country.recovered} - Deaths {country.deaths}
       Confirmed {country.confirmed} - Active {country.active}
    </ListGroup.Item>
  )
})
return (
        <>
        <Jumbotron fluid>
            <Form id="search-form">

                <Form.Control
                    type="text"
                    placeholder="Search for a Country..."
                    ref={focusSearch}
                    onChange={(e) => setQuery(e.target.value)}
                    value={query}
                />
            </Form>

            <ListGroup>

                {countryComponents}

            </ListGroup>
        </Jumbotron>
        </>
    )
}


class Cards extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }


  componentDidMount() {
    fetch("api/world")
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

                 <div class="col-xl-3 col-md-12 mb-4">
                    <div class="card border-left-primary shadow h-100 py-2">
                       <div class="card-body">
                          <div class="row no-gutters align-items-center">
                             <div class="col mr-3">
                             <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">{this.props.name}</div>
                                <div class="h5 mb-0 font-weight-bold text-gray-800">
                                   <div>
                                      {this.state.data.map(world => {
                                      return (

                                      <div>
                                         {world[this.props.name.toLowerCase()]}
                                      </div>
                                      );
                                      })}
                                   </div>
                                </div>
                             </div>
                          </div>
                       </div>
                    </div>
                 </div>



    );
  }
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }


  render() {
    return (
         <div class="container">


         <div class="row">
         <Cards name="recovered" />
         <Cards name="confirmed"/>
         <Cards name="deaths"/>
         <Cards name="active"/>

         </div>

         <div class="row">
         <Search />

         </div>

      </div>

    );
  }
}


export default App;

const container = document.getElementById("app");
render(<App />, container);
