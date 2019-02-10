import opencv2
int minh,maxh,mins,maxs,minv,maxv
def helptext():
{
	print('black')
	print('grey')
	print('red')
	print('orange')
	print('yellow')
	print('green')
	print('blue')
	print('purple')
	print('Input the color you want to detect')
}
def deal(char color):
	switch(color)
		case 'black':
			minh=0
			maxh maxh = 180
            mins = 0
            maxs = 255
            minv = 0
            maxv = 46
            break
        case 'H':
            minh = 0
            maxh = 180
            mins = 0
            maxs = 43
            minv = 46
            maxv = 220
            break
        case 'W':
            minh = 0
            maxh = 180
            mins = 0
            maxs = 30
            minv = 221
            maxv = 255
            break
        case 'R':
            minh = 0
            maxh = 10
            mins = 43
            maxs = 255
            minv = 46
            maxv = 255
            break
        case 'O':
            minh = 11
            maxh = 25
            mins = 43
            maxs = 255
            minv = 46
            maxv = 255
            break
        case 'Y':
            minh = 26
            maxh = 25
            mins = 43
            maxs = 255
            minv = 46
            maxv = 255
            break
        case 'G':
            minh = 35
            maxh = 77
            mins = 43
            maxs = 255
            minv = 46
            maxv = 255
            break
        case 'L':
            minh = 100
            maxh = 124
            mins = 43
            maxs = 255
            minv = 46
            maxv = 255
            break
        case 'P':
            minh = 125
            maxh = 155
            mins = 43
            maxs = 255
            minv = 46
            maxv = 255
            break
        default:
            print('bad input,reenter')
            exit(0)
    

def main():
	 VideoCapture cap(0) //调用摄像头，0为计算机摄像头，1为外接USB摄像头
    
    Mat special
    
    helptext()
    
    char color
    cin >> color
    deal(color)
    
    
    while(true)
        
        Mat frame              //存储每一帧的图像
        
        cap >> frame        //读取当前帧
        
        Mat fhsv
        
        cvtColor(frame,fhsv,COLOR_BGR2HSV)   //将图像转换为HSV模型
        
        inRange(fhsv,Scalar(minh,mins,minv),Scalar(maxh,maxs,maxv),special)          //找寻在要求区间内的颜色
        
        imshow("[pic]",special)
        
        imshow("Original", frame) //show the original image
        
        if(waitKey(30) >= 0)
            break
    return 0
    




