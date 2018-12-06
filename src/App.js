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
      username: 'default',
      input: '',
    }
  }

  changeName = e =>{
    this.setState({name: e.target.value})
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
        <AppBar
        posts={this.state.posts} 
        changeName={this.changeName}
        username={this.state.username}
        />
      </div>
    );
  }
}

export default App;
