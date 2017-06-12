/*@flow*/

// React
import React, { Component } from 'react';

import { Feed } from 'semantic-ui-react';

const AnnotationList = (props: Object) => {
  let { annotations } = props;
  if (annotations.length === 0) {
    annotations = [{
      timecode: '00:00:00',
      text: 'No annotations',
    }];
  }
  return(
    <div className="annotation-list-container">
      <Feed>
        {annotations.map((annotation, index) =>
          <Feed.Event>
            <Feed.Label>
              {annotation.timecode}
            </Feed.Label>
            <Feed.Content>
              <Feed.Summary>
                {annotation.text}
              </Feed.Summary>
            </Feed.Content>
          </Feed.Event>
        )}
      </Feed>
    </div>
  );
}

export default AnnotationList;
