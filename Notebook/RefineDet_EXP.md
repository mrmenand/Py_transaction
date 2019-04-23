##RefineDet 
具体参照作者https://github.com/sfzhang15/RefineDet   下ReadMe.md
###  数据准备
1. 为了方便后面RefineDet/data/VOC0712下脚本.sh的运行，在hom目录建立data文件夹
   data/data_tools 通过运行intergration_file ,fix_xml，count_xml，选取前10类，
   通过get_sometype获取前10类的图片和label，最后move_pic_xml到data中的HOME/data/VOCDevikit
   通过get_txt 生成train，test,trainval and val.txt文件 

2. 从HOME/data/VOCDevikit 读取数据生成trainval.txt, test.txt, and test_name_size.txt 放在在data/VOC0712/
        cd $RefineDet_ROOT
        ./data/VOC0712/create_list.sh ####删除13行的VOC2012
        需要更改权限

3. 生成LMDB file
    cd $RefineDet_ROOT
    ./data/VOC0712/create_data.sh  ###27 行 path的路径改成/data/VOCdevkit
        ## 需要修改RefineDet/test/lib/datasets/pascal_voc.py 29行中self._classes = ('__background__', # always index 0
                         '9999','0203','0403','0000','0404',
                         '0401','0405','0805','0303','0704') 
                         与RefineDet/data/VOC0712/labelmap_voc.prototxt文件中的类别（修改后，自己数据集）中的一致
        


### 训练阶段
1. $RefineDet_ROOT 创建modules/VGGNet/  ,下载Fully convolutional reduced VGGNet，放在VGGNet目录下

2. 修改python examples/refinedet/VGG16_VOC2007_512.py 中 334行 gpus =，340 行 batch_size , 365 solver配置参数，277 行 num_classes,
会自动在models/VGGNet/ 生成VOC2007的训练，测试，配置 prototxt


### 测试阶段
1.  refinedet_demo.py
    86，87行修改deploy ，caffe model的路径  102,103 的测试图片

2. refinedet_test.py #测试mAP
   12行路径。