import cv2
import pytesseract

#连接到tesseract程序
pytesseract.pytesseract.tesseract_cmd='E:\\Tesseract-OCR\\tesseract.exe'

img=cv2.imread('1.png')
#转化为RGB通道
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#进行识别，获取识别结果的文本，img_to_string
print(pytesseract.image_to_string(img))

#进行识别，获取识别结果的文本以及识别出来的位置，用于打框

hImg,wImg,_=img.shape#获取图片的尺寸
#识别字母和数字
# boxes=pytesseract.image_to_boxes(img)#获取框坐标，注意这里给出四个值是左上角坐标和右下角坐标，同时这里的y轴从下向上
# #这里将获取到的boxes按换行符进行分割
# for b in boxes.splitlines():
#     print(b)#获取到的是字符串
#     b=b.split(' ')#字符串分割为列表
#
#     x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])#获取打框信息
#     #绘制框图和识别记过
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
#     cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

#识别单词和数字
cong=r'--oem 3 --psm 6 outputbase digits'#可以通过再img_to_*的函数中的config参数中加这个，表示只识别数字
boxes=pytesseract.image_to_data(img)#获取框坐标，这里按一整个单词进行识别
print(boxes)
for x,b in enumerate(boxes.splitlines()):
    #不要第一行
    if x!=0:
        b=b.split()
        print(b)
        #只有长度为12的列表中才有单词信息，需要过滤
        if len(b)==12:
            x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])#获取打框信息
            #绘制框图和识别记过
            cv2.rectangle(img,(x,y),(w+x,y+h),(0,0,255),2)#这里的坐标输出是正常的
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

cv2.imshow('Result',img)
cv2.waitKey(0)