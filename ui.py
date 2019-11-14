import tkinter
import os

top = tkinter.Tk()
top.title("Eagle strategy demo")
top.minsize(400,600)
top.configure(background = '#bdbdbd')

frame = tkinter.Frame(top,bg = "#bdbdbd")
frame.pack()
title = tkinter.Frame(frame,bg = "#4e342e")
title.pack(fill=tkinter.X)
body = tkinter.Frame(frame,bg='#bdbdbd')
body.pack(fill=tkinter.X)

b1 = tkinter.Frame(body,bg='#bdbdbd',width = 200)
b1.pack(side=tkinter.LEFT)
b2 = tkinter.Frame(body,bg='#bdbdbd',width = 200)
b2.pack(side=tkinter.LEFT)
b3 = tkinter.Frame(body,bg='#bdbdbd',width = 200)
b3.pack(side=tkinter.LEFT)

output1 = tkinter.Frame(frame,bg='#bdbdbd',width = 200)
output1.pack(side=tkinter.LEFT)
output2 = tkinter.Frame(frame,bg='#bdbdbd',width = 200)
output2.pack(side=tkinter.LEFT)
output3 = tkinter.Frame(frame,bg='#bdbdbd',width = 200)
output3.pack(side=tkinter.LEFT)

def run_backprop():
    os.system('python3 /Users/pragnya/Documents/GitHub/Metaheuristic-NN/DNNEye.py > result1.txt')
    file = open('/Users/pragnya/Documents/GitHub/Metaheuristic-NN/result1.txt','r')
    lines = file.readlines()
    metrics = lines[-11]
    metrics = metrics.split(" - ")
    accuracy = metrics[3]
    loss = metrics[2]
    time = lines[-1]
    # print(time)
    tkinter.Label(output1, text = "With Backpropogation:",  font =('Roboto', 20,'bold'),bg = '#bdbdbd',fg="#4e342e").pack(padx=40,pady=5) 
    tkinter.Label(output1, text = time,  font =('Roboto', 16),bg = '#bdbdbd',fg="#4e342e").pack(padx=40,pady=1) 
    tkinter.Label(output1, text = accuracy,  font =('Roboto', 16),bg = '#bdbdbd',fg="#4e342e").pack(padx=40,pady=1) 
    tkinter.Label(output1, text = loss,  font =('Roboto', 16),bg = '#bdbdbd',fg="#4e342e").pack(padx=40,pady=1) 
    

def run_eagle():
    os.system('python3 /Users/pragnya/Documents/GitHub/Metaheuristic-NN/try.py > result2.txt')

tkinter.Label(title, text = 'Eagle Strategy Demonstration',  font =('Roboto', 56),bg='#4e342e',fg='#bdbdbd').pack(padx=100,pady = 1) 
tkinter.Label(title, text = 'Artificial Intelligence Project',  font =('Roboto', 32),bg = '#4e342e',fg="#bdbdbd").pack(pady = 1) 
tkinter.Label(title, text = 'Course code: UE17CS325',  font =('Roboto', 20),bg = '#4e342e',fg="#bdbdbd").pack(pady=1) 
tkinter.Label(title, text = '',  font =('Roboto', 14),bg = '#4e342e',fg="#bdbdbd").pack(pady=5) 
tkinter.Label(title, text = 'Sneha Nemadi       Sarang Ravindra       Pragnya Sridhar',  font =('Roboto', 16),bg = '#4e342e',fg="#bdbdbd").pack(pady=1) 





button1 = tkinter.Button(b1, text='Backpropogation', command=run_backprop,width=26,pady= 5,bg = '#B2EBF2',font = ('Roboto',14),fg='#4e342e')
button1.pack(padx = 90,pady = 60,side=tkinter.TOP) 
# button1.configure(background = "#B2EBF2")

button2 = tkinter.Button(b2, text='Eagle Strategy+Simulated Annealing', command=run_eagle,width=26,pady=5,bg = '#B2EBF2',font = ('Roboto',14),fg='#4e342e')
button2.pack(padx = 90,pady = 60, side = tkinter.TOP) 
# button2.configure(background = "#B2EBF2")

button3 = tkinter.Button(b3, text='Eagle Strategy+Genetic Algorithm' , command=run_eagle,width=26,pady=5,bg = '#B2EBF2',font = ('Roboto',14),fg='#4e342e')
button3.pack(padx = 90,pady = 60, side = tkinter.TOP)


tkinter.mainloop() 
