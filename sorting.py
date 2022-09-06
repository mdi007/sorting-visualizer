from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
root=Tk()
root.title('Sorting Visualizer')
root.geometry('900x600+200+80')
root.config(bg='#546E7A')
data=[]

def drawData(data,colorArray):
    canvas.delete("all")
    canvas_height=450
    canvas_width=900
    x_width=canvas_width //(len(data)+1)
    offset=1
    spacing=0
    
    normalised_data=[i/max(data) for i in data]
    
    for i,height in enumerate(normalised_data):
        x0=i*x_width+offset+spacing
        y0=canvas_height-height*400
        x1=(i+1)*x_width
        y1=canvas_height
        
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
    root.update_idletasks()
def StartAlgo():
    global data
    if not data:
        return
    if algo_menu.get()=='QuickSort':
        quick_sort(data,0,len(data)-1,drawData,speedscale.get())
        drawData(data,['green' for x in range(len(data))])
    elif algo_menu.get()=='Bubble sort':
        bubble_sort(data,drawData,int(speedscale.get()))
    elif algo_menu.get()=='Merge Sort':
        merge_sort(data,drawData,speedscale.get())
        drawData(data,['green' for x in range(len(data))])


def Generate():
    global data
    print('Selected Algo :'+ selected_algorithm.get())
    # _minvalue=int(minvalue.get())
    # _maxvalue=int(maxvalue.get())
    _sizevalue=int(sizevalue.get())
    data=[]
    for _ in range(_sizevalue):
        data.append(random.randrange(100,10000))
    drawData(data,['red' for x in range(len(data))])
    

selected_algorithm=StringVar()
mainlabel=Label(root,text="Alogorithm : ",font=("new roman",16,"italic bold"),bg="#05897A",
                width=10,fg="black",relief=GROOVE,bd=5)
mainlabel.place(x=20,y=20)


algo_menu=ttk.Combobox(root,width=15,font=("new roman",19,"italic bold"),textvariable=selected_algorithm,values=['Bubble sort','Merge Sort','QuickSort'],state='readonly')
algo_menu.place(x=165,y=20)
algo_menu.current(0)

random_generate=Button(root,text="Generate",bg="#2DAE9A",font=("new roman",12,"italic bold"),relief=SUNKEN,activebackground="#05945B",activeforeground="white",width=10,command=Generate)
random_generate.place(x=750,y=80)

sizevaluelabel=Label(root,text="Size : ",font=("new roman",12,"italic bold"),bg="#0E6DA5",
                width=10,fg="black",height=2,relief=GROOVE,bd=5)
sizevaluelabel.place(x=20,y=60)

sizevalue=Scale(root,from_=15,to=100,resolution=1,orient=HORIZONTAL,font=("new roman",14,"italic bold"),relief=GROOVE,bd=2,width=10)
sizevalue.place(x=140,y=60)
# -----
speedlabel=Label(root,text="Speed : ",font=("new roman",12,"italic bold"),bg="#0E6DA5",
                width=10,fg="black",height=2,relief=GROOVE,bd=5)
speedlabel.place(x=340,y=60)

speedscale=Scale(root,from_=1,to=5,resolution=1,orient=HORIZONTAL,font=("new roman",14,"italic bold"),bd=2,width=10)
speedscale.place(x=460,y=60)

start=Button(root,text="Start",bg="#C45B09",font=("new roman",12,"italic bold"),relief=SUNKEN,activebackground="#05945B",activeforeground="white",width=10,command=StartAlgo)
start.place(x=750,y=20)
# ---------

canvas=Canvas(root,width=870,height=450,bg="black")
canvas.place(x=10,y=130)


root.mainloop()