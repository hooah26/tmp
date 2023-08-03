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


        self.categories = ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light",
            "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
            "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
            "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
            "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
            "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch",
            "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone",
            "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
            "hair drier", "toothbrush"]
