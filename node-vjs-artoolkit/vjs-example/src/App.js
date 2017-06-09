import React, { Component } from 'react';
import './App.css';

// Containers
import VideoContainer from './containers/VideoContainer';

const playerOptions = {
  controls: true,
  inactivityTimeout: false,
  fluid: true
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <VideoContainer
          src={[{ src: '/bunny.mp4', type: 'video/mp4'}]}
          playerOptions={playerOptions}
          plugins={[]}
        />
      </div>
    );
  }
}

export default App;