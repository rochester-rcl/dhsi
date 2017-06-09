/* @flow */

// React
import React, { Component } from 'react';
import PropTypes from 'prop-types';

// VideoJS
import videojs from 'video.js';
// CSS
import videojsCSS from 'video.js/dist/video-js.css';

// Lodash
import lodash from 'lodash';

export default class VideoPlayer extends Component {
  constructor(props: Object) {
    super(props);
  }
  // Lifecycle methods
  componentDidMount(): void{
    this.initPlayer();
  }
  componentWillReceiveProps(nextProps: Object): void{
    let currentSrc: string = this.props.src;
    let newSrc: string = nextProps.src;
    if(!lodash.isEqual(currentSrc, newSrc)) {
      this.setSrc(newSrc);
    }
  }
  componentWillUnmount(): void{
    this.player.dispose();
  }
  render() {
    return(<video ref="videoJSPlayer" className="video-js vjs-default-skin vjs-big-play-centered">{this.props.children}</video>);
  }
  // Player related methods
  initPlayer(): void{
    let src: object = this.props.src;
    let options: Array<Object> = this.props.playerOptions
    this.player = videojs(this.getPlayerElement(), options);
    this.player.src(src);
    this.registerPlugins();
  }
  // Assuming all videojs plugins are written according to https://github.com/videojs/video.js/blob/master/docs/guides/plugins.md
  registerPlugins(): void{
    let plugins = this.props.plugins;
    plugins.forEach((pluginObj) => {
      videojs.plugin(pluginObj.name, pluginObj.plugin);
      this.player[pluginObj.name] = pluginObj.plugin.call(this.player, pluginObj.options);
    });
  }
  getPlayerElement(): HTMLCollection<HTMLElement>{
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
