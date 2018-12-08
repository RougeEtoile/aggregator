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
    this.setState({username: e.target.value})
  }
  changeInput = e =>{
    this.setState({input: e.target.value})
  }

  search = e =>{
    fetch('http://localhost:8000/posts/search/'+this.state.username+'/'+this.state.input+'/')
    .then(response => response.json())
    .then(data =>
        {
          console.log(data)
          this.setState({ posts: data })
        });
  }
  import = () => {
    fetch(api)
      .then(response => response.json())
      .then(data =>
        {
          console.log(data)
          this.setState({ posts: data })
        });
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
        input={this.state.input}
        changeInput={this.changeInput}
        username={this.state.username}
        search={this.search}
        import={this.import}
        />
      </div>
    );
  }
}

export default App;
