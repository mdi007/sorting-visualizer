import time
def merge_sort(data,drawData,timeT):
    merge_sort_algo(data,0,len(data),drawData,timeT)
    
def merge_sort_algo(data,left,right,drawData,timeT):
    if left<right:
        mid=(left+right)//2
        merge_sort_algo(data,left,mid,drawData,timeT)
        merge_sort_algo(data,mid+1,right,drawData,timeT)
        merge(data,left,mid,right,drawData,timeT)

def merge(data,left,mid,right,drawData,timeT):
    drawData(data,ColorArray(len(data),left,mid,right))
    time.sleep(1/(timeT*20))
    
    lp=data[left:mid+1]
    rp=data[mid+1:right+1]
    lp.sort()
    rp.sort()
    leftidx=rightidx=0
    
    for i in range(left,right):
        if leftidx<len(lp) and rightidx<len(rp):
            if lp[leftidx]<=rp[rightidx]:
                data[i]=lp[leftidx]
                leftidx+=1
            else:
                data[i]=rp[rightidx]
                rightidx+=1
                
        elif leftidx<len(lp):
            data[i]=lp[leftidx]
            leftidx+=1
        else:
            data[i]=rp[rightidx]
            rightidx+=1

    drawData(data,['green' if x>=left and x<=right else "blue" for x in range(len(data))])
    time.sleep(1/(timeT*20))
def ColorArray(length,left,mid,right):
    colorArray=[]
    for i in range(length):
        if i>=left and i<=right:
            if i>=left and i<=mid:
                colorArray.append("yellow")
            else:
                colorArray.append("red")
        else:
            colorArray.append("blue")
    return colorArray