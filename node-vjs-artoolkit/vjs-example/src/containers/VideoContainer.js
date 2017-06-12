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
    const { src, playerOptions, plugins } = this.props;
    let { annotations } = this.state;
    return(
      <div className="video-annotator-container">
        <VideoPlayer src={src} playerOptions={playerOptions} plugins={plugins} />
        <AnnotationList annotations={annotations} />
      </div>
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
