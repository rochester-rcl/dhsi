# using docker baseimage
FROM phusion/baseimage:0.9.22

CMD ["/sbin/my_init"]

RUN apt-get update \
  && apt-get install --no-install-recommends -y wget \
  unzip \
  python3.5-dev \
  build-essential \
  cmake \
  pkg-config \
  libjpeg8-dev \
  libtiff5-dev \
  libjasper-dev \
  libpng12-dev \
  libgtk-3-dev \
  libatlas-base-dev \
  gfortran \
  libavcodec-dev \
  libavformat-dev \
  libswscale-dev \
  libavresample-dev \
  libv4l-dev \
  libxvidcore-dev \
  libx264-dev \
  mediainfo \
  sox \
  ffmpeg \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && mkdir /home/opencv/ \
  && curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
  && python3 get-pip.py \
  && pip3 install numpy \
  && rm get-pip.py

WORKDIR /home/opencv

RUN wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.2.0.zip \
  && wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.2.0.zip \
  && unzip opencv.zip \
  && unzip opencv_contrib.zip \
  && cd opencv-3.2.0 \
  && mkdir build \
  && cd build \
  && cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D INSTALL_C_EXAMPLES=OFF \
    -D BUILD_opencv_java=OFF \
    -D WITH_CUDA=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=/home/opencv/opencv_contrib-3.2.0/modules \
    -D PYTHON_EXECUTABLE=/usr/bin/python3 \
    -D BUILD_EXAMPLES=OFF .. \
    && make -j4 \
    && make install \
    && ldconfig \
    && cd /home/opencv \
    && rm -rf opencv-3.2.0 \
    && rm opencv.zip \
    && rm -rf opencv_contrib-3.2.0 \
    && rm opencv_contrib.zip

COPY opencv-examples/ /home/opencv-examples
WORKDIR /home/opencv-examples/video_io
RUN python3 setup.py sdist \
    && pip3 install -e .

WORKDIR /home/opencv-examples/spectrogram_generator
RUN python3 setup.py sdist \
    && pip3 install -e .


WORKDIR /home
