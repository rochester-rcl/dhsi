/* @flow */

// React
import React, { Component } from 'react';
import PropTypes from 'prop-types';

// Components
import VideoPlayer from '../components/VideoPlayer';
import AnnotationList from '../components/AnnotationList';

class VideoContainer extends Component {
  state = { annotations: [] };
  constructor(props: Object) {
    super(props);
  }
  render() {
    const { src, playerOptions, plugins, isPlaying, setPlayingState, comparativeAnnotations } = this.props;
    let { annotations } = this.state;
    return(
      <div className="video-annotator-container">
        <VideoPlayer
          isPlaying={isPlaying}
          src={src}
          setPlayingState={setPlayingState}
          playerOptions={playerOptions}
          comparativeAnnotations={comparativeAnnotations}
          plugins={plugins}
        />
      </div>
    );
  }
}

// Connect to redux store

export default VideoContainer
