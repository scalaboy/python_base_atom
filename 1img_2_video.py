import cv2
import glob
import cv2
import glob

#根据自己的实际情况更改目录。
#要转换的图片的保存地址，按顺序排好，后面会一张一张按顺序读取。
convert_image_path = '/home/deeplp/mainspace/software/OrbbecViewer/output/IR/jpg'

#帧率(fps)，尺寸(size)，此处设置的fps为24，size为图片的大小，本文转换的图片大小为400×1080，
#即宽为400，高为1080，要根据自己的情况修改图片大小。
fps = 24
size = (640,480)

videoWriter = cv2.VideoWriter('/deeplp/mainspace//TestVideo.avi',cv2.VideoWriter_fourcc('I','4','2','0'),
                              fps,size)

for img in glob.glob(convert_image_path + "/*.jpg") :
    print(img)
    read_img = cv2.imread(img)
    videoWriter.write(read_img)
videoWriter.release()
