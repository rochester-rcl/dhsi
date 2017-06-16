/* @flow */

// React
import React, { Component } from 'react';
import PropTypes from 'prop-types';

// VideoJS
import videojs from 'video.js';
// CSS
import 'video.js/dist/video-js.css';

// Lodash
import lodash from 'lodash';

export default class VideoPlayer extends Component {
  state = { currentAnnotation: null }
  constructor(props: Object) {
    super(props);
  }
  // Lifecycle methods
  componentDidMount(): void {
    this.initPlayer();
  }
  componentWillReceiveProps(nextProps: Object): void{
    let currentSrc: string = this.props.src;
    let newSrc: string = nextProps.src;
    if(!lodash.isEqual(currentSrc, newSrc)) {
      this.setSrc(newSrc);
    }
    console.log(nextProps.isPlaying);
    if (nextProps.isPlaying === true) {
      this.player.play();
    } else {
      this.player.pause();
    }
  }
  componentWillUnmount(): void {
    this.player.dispose();
  }
  render() {
    const { currentAnnotation } = this.state;
    return(
      <div className="annotation-container">
        <div className={currentAnnotation ? "annotation-display-show" : "annotation-display-hidden"}>
          {currentAnnotation ? currentAnnotation : ''}
        </div>
        <video
          ref="videoJSPlayer"
          className="video-js vjs-default-skin vjs-big-play-centered">
          {this.props.children}
        </video>
      </div>
    );
  }
  // Player related methods
  initPlayer(): void {
    let src: object = this.props.src;
    let options: Array<Object> = this.props.playerOptions
    this.player = videojs(this.getPlayerElement(), options);
    this.player.src(src);
    this.registerPlugins();
    this.player.on('play', () => {
      this.props.setPlayingState(true);
    });
    this.player.on('pause', () => {
      this.props.setPlayingState(false);
    });
    this.player.on('timeupdate', () => {
      let timestamp = parseInt(this.player.currentTime(), 10);
      console.log(timestamp);
      this.searchAnnotations(timestamp);
    });

  }
  searchAnnotations(timestamp) {
    let result = this.props.comparativeAnnotations.find((annotation) => { return annotation.time === timestamp });
    if (result) {
      console.log(result.note);
      this.setState({ currentAnnotation: result.note });
      this.sleep(result.duration * 1000).then(() => this.setState({ currentAnnotation: null }));
    }
  }
  sleep(duration) {
    return new Promise((resolve, reject) => {
        setTimeout(() => { resolve() }, duration);
    });
  }
  // Assuming all videojs plugins are written according to https://github.com/videojs/video.js/blob/master/docs/guides/plugins.md
  registerPlugins(): void {
    let plugins = this.props.plugins;
    plugins.forEach((pluginObj) => {
      videojs.plugin(pluginObj.name, pluginObj.plugin);
      this.player[pluginObj.name] = pluginObj.plugin.call(this.player, pluginObj.options);
    });
  }
  getPlayerElement(): HTMLCollection<HTMLElement> {
    return this.refs.videoJSPlayer;
  }
  setSrc(src: string) {
    this.player.src(src);
  }
}

VideoPlayer.propTypes = {
    src: PropTypes.array.isRequired,
    playerOptions: PropTypes.object,
    plugins: PropTypes.array,
}
