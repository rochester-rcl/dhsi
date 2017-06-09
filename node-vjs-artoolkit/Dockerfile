# using docker baseimage
FROM phusion/baseimage:0.9.22

CMD ["/sbin/my_init"]

RUN apt-get update \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV NVM_DIR=/usr/local/nvm

RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | NVM_DIR=$NVM_DIR bash \
    && source $NVM_DIR/nvm.sh \
    && nvm install stable \
    && nvm use stable
