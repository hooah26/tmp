# tmp

sudo apt-get install git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev cmake



git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense
mkdir build && cd build
cmake ../ -DBUILD_PYTHON_BINDINGS=bool:true -DCMAKE_BUILD_TYPE=release
make -j4
sudo make install



export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.6/pyrealsense2


https://docs.ultralytics.com/yolov5/tutorials/running_on_jetson_nano/#install-pytorch-and-torchvision

https://opencourse.tistory.com/224



wget https://files.pythonhosted.org/packages/5e/3f/5658c38579b41866ba21ee1b5020b8225cec86fe717e4b1c5c972de0a33c/pycuda-2019.1.2.tar.gz

tar xvf pycuda-2019.1.2.tar.gz

cd pycuda-2019.1.2

python3 configure.py --cuda-root=/usr/local/cuda-10.2

python3 setup.py install
https://github.com/prabhakar-sivanesan/OpenCV-rtsp-server/tree/master


 rtsp://180.71.194.224:8554/video_stream

