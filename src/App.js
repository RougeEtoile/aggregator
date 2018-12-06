import React, { Component } from 'react';
import AppBar from './AppBar'
import logo from './logo.svg';
import './App.css';

const api = 'http://localhost:8000/posts/Default/posts/'
class App extends Component {
  constructor(){
    super();
    this.state = { 
      posts: [],
      username: 'Default',
      input: '',
    }
  }
  componentDidMount() {
    fetch(api)
      .then(response => response.json())
      .then(data =>
        {
          console.log(data)
          this.setState({ posts: data })
        });
  }


  render() {
    return (
      <div className="App">
        hi
      </div>
    );
  }
}

export default App;
