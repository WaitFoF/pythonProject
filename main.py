import cv2 as cv
import matplotlib.pyplot as plt
"""
实现对于特定标志下的视频图像的变换显示以及存储（cv2.VideoWriter）
    标志1：图像ROI区域的选取以及另一个窗口的显示
    标志2：灰度图像的显示（在另一个窗口显示）
    标志3：图像直方图绘制
    标志4：图像直方图均衡
"""
def imgProcess():
    # 读取本地视频
    cap=cv.VideoCapture("D:/test/test.mp4")
    # 判断视频是否打开成功
    if not cap.isOpened():
        print("Open the Video failed")
        exit()
    # 获取视频的宽和高,帧率
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height= int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps=cap.get(cv.CAP_PROP_FPS)
    print(width)
    print(height)
    print(fps)
    """
    fourcc 本身是一个 32 位的无符号数值，用 4 个字母表示采用的编码器。 
    opencv3支持的avi格式有:
       I420:  未压缩YUV颜色编码
       PIMI:  MPEG-1编码
       XVID: MPEG-4编码 
       fourcc=cv.VideoWriter_fourcc('I', '4', '2', '0'),该参数是YUV编码类型，文件名后缀为.avi
       fourcc=cv.VideoWriter_fourcc('P', 'I', 'M', 'I'),该参数是MPEG-1编码类型，文件名后缀为.avi
       fourcc=cv.VideoWriter_fourcc('X', 'V', 'I', 'D'),该参数是MPEG-4编码类型，文件名后缀为.avi
       fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # avi格式
     MP4格式:
       fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
       fourcc = cv.VideoWriter_fourcc('M', 'P', '4', 'V')
       fourcc = cv.VideoWriter_fourcc(*'MP4V')
       fourcc = cv.VideoWriter_fourcc(*'mp4v')
     其他：  
       cv.VideoWriter_fourcc('T', 'H', 'E', 'O'),该参数是Ogg Vorbis,文件名后缀为.ogv
       cv.VideoWriter_fourcc('F', 'L', 'V', '1'),该参数是Flash视频，文件名后缀为.flv
    """
    fourcc = cv.VideoWriter_fourcc(*'MP4V')
    # fourcc = cv.VideoWriter_fourcc(*'MJPG')  # avi格式
    # 成功读取视频文件后，用户输入标志
    print("特定标志下的视频图像的变换规则如下：\n"
          "1: 图像ROI区域的选取以及另一个窗口的显示\n"
          "2: 灰度图像的显示（在另一个窗口显示）\n"
          "3: 图像直方图绘制\n"
          "4: 图像直方图均衡")
    flag = int(input("请输入您要进行视频操作的标志数字(请直接输入：1/2/3/4)："))
    # 循环等待用户输入1-4的数字，若不在此范围，请求继续输入
    while True:
        # input()函数的输入值，永远会被强制性地转换为字符串类型。（Python3固定规则）
        if flag not in range(1,5):
            flag = int(input("您输入的内容操作有误，请重新输入："))
        else:
            break

    # 获取到flag后，根据flag进行对应的操作
    if flag==1:
        # 1: 图像ROI区域的选取以及另一个窗口的显示
        # 设置ROI区域的开始和结束范围
        # if width>=400 and height>=400:
        #     widthB = int(width / 2) - 200
        #     widthE = int(width / 2) + 200
        #     heightB = int(height / 2) - 200
        #     heightE = int(height / 2) + 200
        # else:
        widthB = 0
        widthE = int(width/2)
        heightB = 0
        heightE = int(height/2)
        """
           VideoWriter(filename, fourcc, fps, frameSize[, isColor])
           filename 要保存的文件的路径
           fourcc 指定编码器
           fps 要保存的视频的帧率
           frameSize 要保存的文件的画面尺寸
           isColor 指示是黑白画面还是彩色的画面,isColor如果非零，编码器将希望得到彩色帧并进行编码；
                 否则，是灰度帧（只有在Windows下支持这个标志）。
        """
        print(widthE-widthB)
        print(heightE-heightB)
        out = cv.VideoWriter("Flag1_ROI.mp4", fourcc, fps, (heightE-heightB,widthE-widthB))
        while True:
            # 第一个参数ret 为True 或者False,代表有没有读取到图片
            # 第二个参数frame表示截取到一帧的图片
            ret, frame = cap.read()
            if not ret:
                break
            ## 截取区域300*400的区域
            # roiImg = frame[0:400, 0:300,:]
            roiImg = frame[widthB:widthE, heightB:heightE,:]
            print(roiImg.shape[0])
            print(roiImg.shape[1])
            cv.imshow("Src", frame)
            cv.imshow("ROI", roiImg)
            # 保存视频文件
            out.write(roiImg)
            if cv.waitKey(30) == ord('q'):
                break
        cap.release()
        out.release()
    elif flag==2:
        # 2: 灰度图像的显示（在另一个窗口显示）
        """
           VideoWriter(filename, fourcc, fps, frameSize[, isColor])
           filename 要保存的文件的路径
           fourcc 指定编码器
           fps 要保存的视频的帧率
           frameSize 要保存的文件的画面尺寸
           isColor 指示是黑白画面还是彩色的画面,isColor如果非零，编码器将希望得到彩色帧并进行编码；
                 否则，是灰度帧（只有在Windows下支持这个标志）。
        """
        out = cv.VideoWriter("Flag2_GRAY.mp4", fourcc, fps, (width, height),0)
        while True:
            # 第一个参数ret 为True 或者False,代表有没有读取到图片
            # 第二个参数frame表示截取到一帧的图片
            ret, frame = cap.read()
            if not ret:
                break
            # 灰度转化
            gray=cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
            cv.imshow("Src", frame)
            cv.imshow("Gray", gray)
            if cv.waitKey(30) == ord('q'):
                 break
            out.write(gray)
        cap.release()
        out.release()
    elif flag==3:
        # 3: 图像直方图绘制
        plt.figure()
        plt.title("hist")
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # 查询当前图像通道数
            imgInfo = frame.shape
            channel =imgInfo[2]
            # 若为单通道：
            if channel==1:
                hist=cv.calcHist([frame],[0],None,[256],[0,256])
                plt.plot(hist)
                plt.xlim([0, 256])
            # 3通道图像：
            else:
                # 分离R,G,B 3通道
                channels=cv.split(frame)
                colors=("b","g","r")
                # 绘制3通道的图像直方图
                for (ch,co) in zip(channels,colors):
                    hist = cv.calcHist([ch], [0], None, [256], [0, 256])
                    plt.plot(hist,color=co)
                    plt.xlim([0, 256])
            # 显示直方图的绘制
            plt.ion()
            plt.pause(0.0001)  # 显示秒数
            cv.imshow("Src", frame)
        cap.release()
    else:
        # 4:图像直方图均衡
        out = cv.VideoWriter("Flag4_EqualizeHist.mp4", fourcc, fps, (width, height), 0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
            equalizeHistImg = cv.equalizeHist(gray)
            cv.imshow("Src", frame)
            cv.imshow("EqualizeHistImg", equalizeHistImg)
            out.write(equalizeHistImg)
            if cv.waitKey(30) == ord('q'):
                break
        cap.release()
        out.release()
    cv.destroyAllWindows()

def DataSetsIncrease():
    """
    1. 制作101张数据集
       从视频中保存101帧的图像，命令规则：D:/test/homework/imageX.jpg
    """
    # 从本地加载视频文件
    cap=cv.VideoCapture("D:/test/test.mp4")
    # 判断视频文件是否打开成功，若失败，则函数退出，不再向下执行
    if not cap.isOpened():
        print("Open the Video failed")
        exit()
    # num标识：图片命名中的序号
    num=0
    # 循环【0,100】，每次循环，num加一
    while num<=100:
            # 第一个参数ret 为True 或者False,代表有没有读取到图片
            # 第二个参数frame表示截取到一帧的图片
            ret, frame = cap.read()
            # 若未读到图像，则终止循环
            if not ret:
                break
            # 原数据集的命名并打印
            name="D:/test/homework/image"+str(num)+".jpg"
            print(name)
            # 将视频的前101帧图像保存到指定位置
            cv.imwrite(name,frame)
            num+=1
    """
    2. 实现批量图像的数据扩增（9倍），扩增后名字D:/test/homework/image_bianhuan_X_Y.jpg
        2.1 图像左右翻转
            扩增后名字D:/test/homework/image_bianhuan_X_1.jpg 
        2.2 图像大小变换（放大和缩小一倍，分别利用线性插值以及最近邻插值）
            扩增后名字D:/test/homework/image_bianhuan_X_2~3.jpg
        2.3 0-15°每隔5°的顺时针以及逆时针的旋转
            扩增后名字D:/test/homework/image_bianhuan_X_4~9.jpg
    """
    # 实现101张图像的批量数据扩增，使用for循环[0,101)
    for i in range(0,101):
        # 每次读取一张原图像
        name = "D:/test/homework/image" + str(i) + ".jpg"
        img = cv.imread(name)
        # 判断是否读取成功，若不成功，终止本次循环，继续下次的循环
        if img is None:
            print("读取失败！")
            continue
        # 2.1 左右翻转并保存图像--
        # flip的第二个参数大于0，表示Y轴翻转
        imgY=cv.flip(img,1)# y翻转
        nameimgY = "D:/test/homework/image_bianhuan_" + str(i) + "_1.jpg"
        cv.imwrite(nameimgY, imgY)
        # 2.2 数据的缩放：缩放到原来的一半
        # 第三个参数决定插值的方式：cv.INTER_NEAREST——最邻近插值
        imgSINTER_NEAREST = cv.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)), cv.INTER_NEAREST)
        # 数据的扩增：扩大到原来的2倍
        imgBINTER_LINEAR = cv.resize(img, (img.shape[1] * 2, img.shape[0] * 2), cv.INTER_LINEAR)
        # 保存图像
        nameImgSINTER_NEAREST = "D:/test/homework/image_bianhuan_" + str(i) + "_2.jpg"
        cv.imwrite(nameImgSINTER_NEAREST, imgSINTER_NEAREST)
        nameImgBINTER_LINEAR = "D:/test/homework/image_bianhuan_" + str(i) + "_3.jpg"
        cv.imwrite(nameImgBINTER_LINEAR, imgBINTER_LINEAR)
        # 2.3 0-15°每隔5°的顺时针以及逆时针的旋转
        # rows,cols表示图像的中心
        rows = int(img.shape[0]/2)
        cols = int(img.shape[1]/2)
        # k标志数据库扩增的下标
        k=4
        # 负数表示顺时针旋转的度数，正数表示逆时针旋转的度数
        for j in [-15,-10,-5,5,10,15]:
            # getRotationMatrix2D(Point2f center, double angle, double scale)
            # 功能：主要用于获得图像绕着某一点的旋转矩阵
            # 第一个参数：表示旋转的中心点
            # 第二个参数: double angle：表示旋转的角度
            # 第三个参数：double scale：图像缩放因子
            rotate = cv.getRotationMatrix2D((cols,rows), j, 1)
            # warpAffine(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None)
            # 功能：实现一些简单的重映射
            # src: 输入图像
            # M: 变换矩阵
            # dsize: 指定图像输出尺寸
            rotateImg = cv.warpAffine(img, rotate, (img.shape[1], img.shape[0]))
            # 图像保存
            name = "D:/test/homework/image_bianhuan_" + str(i) + "_"+ str(k)+".jpg"
            cv.imwrite(name,rotateImg)
            k+=1


if __name__ == '__main__':
    ## 1 视频处理
    imgProcess()
    ## 2 数据扩增
    DataSetsIncrease()