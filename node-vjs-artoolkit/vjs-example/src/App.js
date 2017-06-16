import React, { Component } from 'react';
import './App.css';
import 'semantic-ui-css/semantic.min.css';

// Containers
import VideoContainer from './containers/VideoContainer';

const playerOptions = {
  controls: true,
  inactivityTimeout: false,
  fluid: true,
  loop: true,
}

const comparativeAnnotations = {
  video1: [
    { time: 10, note: 'This is an annotation', duration: 5 },
    { time: 15, note: 'This is another annotation', duration: 5 },
  ],
  video2: [
    { time: 2, note: 'This is a different annotation', duration: 1 },
    { time: 5, note: 'This is another different annotation', duration: 1 },
  ],
}

class App extends Component {
  state = { isPlaying: false,  }
  constructor(props) {
    super(props);
    this.setPlayingState = this.setPlayingState.bind(this);
  }
  setPlayingState(playingState) {
    this.setState({ isPlaying: playingState });
  }
  render() {
    return (
      <div className="App">
        <h1 className="videotitle">Video 1</h1>
        <div className="video-player-container">
          <VideoContainer
            src={[{ src: '/bunny.mp4', type: 'video/mp4'}]}
            isPlaying={this.state.isPlaying}
            setPlayingState={this.setPlayingState}
            playerOptions={playerOptions}
            comparativeAnnotations={comparativeAnnotations.video1}
            plugins={[]}
          />
          <VideoContainer
            src={[{ src: '/keaton.mp4', type: 'video/mp4'}]}
            isPlaying={this.state.isPlaying}
            setPlayingState={this.setPlayingState}
            comparativeAnnotations={comparativeAnnotations.video2}
            playerOptions={playerOptions}
            plugins={[]}
          />
        </div>
      </div>
    );
  }
}

export default App;
