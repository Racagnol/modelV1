#
# A Docker image for running mozaik simulations
#
# This image extends the "simulationx" image by adding mozaik dependencies
#
# Usage:
#
# docker build --no-cache -t mozaik .
# docker run -e DISPLAY=$DISPLAY -v `pwd`:`pwd` -w `pwd` -i -t mozaik /bin/bash
# (in the image)# python run_size_closed.py nest 8 param/defaults_mea 'data_size'

FROM neuralensemble/base:py2

MAINTAINER domenico.guarino@cnrs.fr

##########################################################
# Xserver
#CMD export DISPLAY=:0
CMD export DISPLAY=0.0
#CMD export DISPLAY=:0.0
ENV DISPLAY :0

#######################################################

USER root

ENV NEST_VER=2.18.0
ENV NEST=v$NEST_VER


RUN apt-get update -y

RUN apt-get install -y libssl-dev


WORKDIR $HOME/packages
RUN wget https://github.com/nest/nest-simulator/archive/$NEST.tar.gz -O $HOME/packages/$NEST.tar.gz;
RUN tar xzf $NEST.tar.gz; rm $NEST.tar.gz
RUN git clone --depth 1 https://github.com/INCF/libneurosim.git
RUN cd libneurosim; ./autogen.sh

WORKDIR $HOME
RUN wget https://cmake.org/files/v3.17/cmake-3.17.0-rc1.tar.gz
RUN tar -xzvf cmake-3.17.0-rc1.tar.gz
WORKDIR $HOME/cmake-3.17.0-rc1
RUN ./bootstrap
RUN make -j4
RUN make install


RUN mkdir $VENV/build
WORKDIR $VENV/build
RUN mkdir libneurosim; \
    cd libneurosim; \
    PYTHON=$VENV/bin/python $HOME/packages/libneurosim/configure --prefix=$VENV; \
    make; make install; ls $VENV/lib $VENV/include
RUN ln -s /usr/lib/python2.7/config-x86_64-linux-gnu/libpython2.7.so $VENV/lib/
RUN mkdir $NEST;
RUN cd $NEST; \
    cmake -DCMAKE_INSTALL_PREFIX=$VENV \
          -Dwith-mpi=OFF  \
          ###-Dwith-music=ON \
          -Dwith-libneurosim=ON \
          -DPYTHON_LIBRARY=$VENV/lib/libpython2.7.so \
          -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
          -Dwith-optimize='-O3' \ 
	  $HOME/packages/nest-simulator-$NEST_VER; \
    make; make install


RUN PATH=$PATH:$VENV/bin

WORKDIR /home/docker/
RUN echo "source $VENV/bin/activate" >> .bashrc


RUN $VENV/bin/pip install lazyarray pynn=0.9.5 psutil scipy==1.0 numpy==1.14 cython==0.29 pandas==0.21 statsmodels==0.10.0 matplotlib==2.1.1 sciunit==0.2.2.1 interval param==1.5.1 cycler

RUN apt-get autoremove -y && \
    apt-get clean

WORKDIR $HOME
RUN git clone https://github.com/antolikjan/imagen.git
WORKDIR $HOME/imagen
RUN python setup.py install

WORKDIR $HOME/mozaik
RUN git clone https://github.com/antolikjan/mozaik
WORKDIR $HOME/mozaik/mozaik
RUN python setup.py install

WORKDIR $HOME/mozaik
RUN git clone https://github.com/antolikjan/mozaik-contrib

WORKDIR $HOME/mozaik
RUN git clone https://github.com/RCagnol/V1sciunit


# Simple test:
# cd /home/docker/mozaik/examples/VogelsAbbott2005
# python run.py nest 2 param/defaults 'test'
# mpirun -np 2 python run.py nest 2 param/defaults 'test'
