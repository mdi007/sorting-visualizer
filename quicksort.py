import time

def partition(data,head,tail,drawData,timeT):
    border=head
    pivot=data[tail]
    
    drawData(data,ColorArray(len(data),head,tail,border,border))
    time.sleep(1/(timeT*20))
    
    for j in range(head,tail):
        if(data[j]<pivot):
            drawData(data,ColorArray(len(data),head,tail,border,j,True))
            time.sleep(1/(timeT*20))
            data[border],data[j]=data[j],data[border]
            border+=1
        drawData(data,ColorArray(len(data),head,tail,border,j))
        time.sleep(1/(timeT*20))

    drawData(data,ColorArray(len(data),head,tail,border,tail,True))
    time.sleep(1/(timeT*20))
    data[border],data[tail]=data[tail],data[border]
    return border

def quick_sort(data,head,tail,drawData,timeT):
    if head<tail:
        p=partition(data,head,tail,drawData,timeT)
        quick_sort(data,head,p-1,drawData,timeT)
        quick_sort(data,p+1,tail,drawData,timeT)

def ColorArray(datalen,head,tail,border,currinx,isSwapping=False):
    colorArray=[]
    for i in range(datalen):
        if i>=head and i<=tail:
            colorArray.append("red")
        else:
            colorArray.append("blue")
        # if i==tail:
        #     colorArray[i]=='white'
        # elif i==border:
        #     colorArray[i]=='purple'
        # elif i==currinx:
        #     colorArray[i]=='grey'
        if isSwapping:
            if i== border or i == currinx:
                colorArray[i]='yellow'
    return colorArray
        