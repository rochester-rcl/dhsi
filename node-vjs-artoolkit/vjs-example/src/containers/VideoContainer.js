/* @flow */

// React
import React, { Component } from 'react';
import PropTypes from 'prop-types';

// Containers
import VideoPlayer from '../components/VideoPlayer';

class VideoContainer extends Component {
  constructor(props: Object) {
    super(props);
  }
  render(){
    const { src, playerOptions, plugins } = this.props;
    return(
      <VideoPlayer src={src} playerOptions={playerOptions} plugins={plugins}/>
    );
  }
}

VideoContainer.propTypes = {
  src: PropTypes.array.isRequired,
  playerOptions: PropTypes.object,
  plugins: PropTypes.array,
  store: PropTypes.object // option to connect to store or take props in index (must be wrapped in <Provider/>)
}

// Connect to redux store

export default VideoContainer
