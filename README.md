
https://www.a:ihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=145

https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=145


https://www.aihub.or.kr/web-nas/aihub21/files/public/%EC%9D%B4%EB%85%B8%EB%A6%AD%EC%8A%A4%20%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C/INNORIX-EX-Ubuntu%EC%9A%A9_%EA%B0%84%EB%8B%A8_%EC%82%AC%EC%9A%A9%EC%84%A4%EB%AA%85%EC%84%9C_18.04.pdf


https://chat.openai.com/share/a791febf-efe2-4652-b0be-6f3ca7610333


Traceback (most recent call last):
  File "test.py", line 12, in <module>
    model = YoloTRT(library="./libmyplugins.so", engine="./yolov7-tiny.engine", conf=0.5, yolo_ver="v7")
  File "/home/xavier/websocket_user/yoloDet.py", line 38, in __init__
    ctypes.CDLL(library)
  File "/usr/lib/python3.8/ctypes/__init__.py", line 373, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libcudart.so.10.2: cannot open shared object file: No such file or directory
\


https://www.youtube.com/watch?v=NPCJF8YL2Gc
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.2/lib64
