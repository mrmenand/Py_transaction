##SSD 
参照作者ReadMe.md文件 https://github.com/weiliu89/caffe/tree/ssd
###安装配置模型 

1. git clone https://github.com/weiliu89/caffe.git 在命令行下生成caffe文件夹
   cd caffe
   git checkout ssd （作者原文下有三个分支）

2. 编译文件，配置Python接口
   拷贝原有Makefile（修改第5行 ：USE_CUDNN,35行的CUDA_ARCH,48行的BLAS：=atlas,89行的PYthon接口
    92,93行改成INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial
               LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/hdf5/serial
    ）
   make all -j8
   添加Python环境变量 gedit ~/.bashrc  添加export PYTHONPATH=/home/guangyixiao/mr_menand/SSD/caffe/python:$PYTHONPATHs  对应
   ssd里面python的路径
   make py
   make test -j8

### 预训练模型和数据准备
1. caffe/models 下新建VGGNet目录，下载空洞卷积VGG预训练caffemodel,下载地址https://gist.github.com/weiliu89/2ed6e13bfd5b57cf81d6，并放在VGGNet目录下

2. 为了方便后面caffe/data/VOC0712下脚本.sh的运行，在hom目录建立data文件夹
   data/data_tools 通过运行intergration_file ,fix_xml，count_xml，选取前10类，
   通过get_sometype获取前10类的图片和label，最后move_pic_xml到data中的HOME/data/VOCDevikit
   通过get_txt 生成train，test,trainval and val.txt

3. 从HOME/data/VOCDevikit 读取数据生成trainval.txt, test.txt, and test_name_size.txt 放在在data/VOC0712/
    在caffe目录下  ./data/VOC0712/create_list.sh  ###删除13行的VOC2012

4. 生成LMDB文件
    在caffe目录下  ./data/VOC0712/create_data.sh

### 训练阶段
修改 examples/ssd/ssd_pascal.py 
86,87 行的resize_width = 512,resize_height = 512
266行num_classes = 11
332行gpus = "0"
337,338行batch_size = 8，accum_batch_size = 8
359,360行num_test_image = 306，test_batch_size = 4#根据自己数据的测试集数量，1080Ti测试的时候batch_size=8 内存溢出，训练是batch_size=8 
375，376配置文件下的snapshot 和display 
