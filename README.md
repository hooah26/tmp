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

[TensorRT] INFO: [MemUsageChange] Init CUDA: CPU +198, GPU +0, now: CPU 255, GPU 2938 (MiB)
[TensorRT] INFO: Loaded engine size: 23 MB
[TensorRT] INFO: [MemUsageSnapshot] deserializeCudaEngine begin: CPU 255 MiB, GPU 2938 MiB
[TensorRT] WARNING: Using an engine plan file across different models of devices is not recommended and is likely to affect performance or even cause errors.
[TensorRT] INFO: [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +158, GPU +159, now: CPU 419, GPU 3102 (MiB)
[TensorRT] INFO: [MemUsageChange] Init cuDNN: CPU +240, GPU +234, now: CPU 659, GPU 3336 (MiB)
[TensorRT] INFO: [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 659, GPU 3336 (MiB)
[TensorRT] INFO: [MemUsageSnapshot] deserializeCudaEngine end: CPU 659 MiB, GPU 3336 MiB
[ WARN:0] global /home/nano/opencv/modules/videoio/src/cap_gstreamer.cpp (933) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
[TensorRT] INFO: [MemUsageSnapshot] ExecutionContext creation begin: CPU 645 MiB, GPU 3333 MiB
[TensorRT] INFO: [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 645, GPU 3333 (MiB)
[TensorRT] INFO: [MemUsageChange] Init cuDNN: CPU +0, GPU +0, now: CPU 645, GPU 3333 (MiB)
[TensorRT] INFO: [MemUsageSnapshot] ExecutionContext creation end: CPU 646 MiB, GPU 3333 MiB
Traceback (most recent call last):
  File "app.py", line 28, in <module>
    cv2.putText(frame, "Person: {:.2f}".format(conf), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
TypeError: integer argument expected, got float
[TensorRT] INFO: [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +0, now: CPU 1243, GPU 3477 (MiB)
