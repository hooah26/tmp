# tmp

sudo apt-get install git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev cmake



git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense
mkdir build && cd build
cmake ../ -DBUILD_PYTHON_BINDINGS=bool:true -DCMAKE_BUILD_TYPE=release
make -j4
sudo make install



export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.6/pyrealsense2
