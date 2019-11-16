import tkinter
import os
from datetime import datetime

path = '/Users/pragnya/Documents/GitHub/'

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

b1 = tkinter.Frame(body,bg='#bdbdbd',width = 150,height=20)
b1.pack(side=tkinter.LEFT)
b2 = tkinter.Frame(body,bg='#bdbdbd',width = 150,height=20)
b2.pack(side=tkinter.LEFT)
b3 = tkinter.Frame(body,bg='#bdbdbd',width = 150,height=20)
b3.pack(side=tkinter.LEFT)
b4 = tkinter.Frame(body,bg='#bdbdbd',width = 150,height=20)
b4.pack(side=tkinter.LEFT)

output1 = tkinter.Frame(frame,bg='#bdbdbd',width = 150)
output1.pack(side=tkinter.LEFT)
output2 = tkinter.Frame(frame,bg='#bdbdbd',width = 150)
output2.pack(side=tkinter.LEFT)
output3 = tkinter.Frame(frame,bg='#bdbdbd',width = 150)
output3.pack(side=tkinter.LEFT)
output4 = tkinter.Frame(frame,bg='#bdbdbd',width = 150)
output4.pack(side=tkinter.LEFT)

def run_backprop():
    os.system('python3 '+path+'Metaheuristic-NN/DNNEye.py > result1.txt')
    f = path+'Metaheuristic-NN/result1.txt'
    file = open(f,'r')
    lines = file.readlines()
    file.close()
    metrics = lines[-11]
    metrics = metrics.split(" - ")
    accuracy = metrics[3]
    loss = metrics[2]
    val_loss = metrics[4]
    val_loss = val_loss.split(":")
    val_loss = "Test loss:"+val_loss[1]

    val_accuracy = metrics[5]
    val_accuracy = val_accuracy.split(":")
    val_accuracy = "Test accuracy:"+val_accuracy[1]
    time = lines[-1]

    r=[]
    # for i in range(2,101,2):
    #     metrics=lines[i].split(" - ")
    #     r.append((metrics[2],metrics[3],metrics[4],metrics[5]))
    results.update({1:r})


    # print(time)
    tkinter.Label(output1, text = "With Backpropogation:",  font =('Roboto', 16,'bold'),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    tkinter.Label(output1, text = time,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    # tkinter.Label(output1, text = accuracy,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    # tkinter.Label(output1, text = loss,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    tkinter.Label(output1, text = val_accuracy,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    tkinter.Label(output1, text = val_loss,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 

def SA_iters():
    global pop1
    pop1 = tkinter.Tk()
    pop1.title("ES+SA")
    tkinter.Label(pop1,text = "Enter no of iterations:",font=('Roboto',14),bg = '#bdbdbd',fg='#4e342e').pack()
    global iterations
    iterations = tkinter.Entry(pop1,width=5)
    iterations.pack()
    button5 = tkinter.Button(pop1, text='OK' , command=run_SA,width=6,pady=5,bg = '#B2EBF2',font = ('Roboto',14,'bold'),fg='#4e342e')
    button5.pack()
    pop1.mainloop()

def GA_iters():
    global pop2
    pop2 = tkinter.Tk()
    pop2.title("ES+GA")
    tkinter.Label(pop2,text = "Enter no of iterations:",font=('Roboto',14),bg = '#bdbdbd',fg='#4e342e').pack()
    global iterations2
    iterations2 = tkinter.Entry(pop2,width=5)
    iterations2.pack()
    button5 = tkinter.Button(pop2, text='OK' , command=run_GA,width=6,pady=5,bg = '#B2EBF2',font = ('Roboto',14,'bold'),fg='#4e342e')
    button5.pack()
    pop2.mainloop()

def SAGA_iters():
    global pop3
    pop3 = tkinter.Tk()
    pop3.title("ES+(GA+SA)")
    tkinter.Label(pop3,text = "Enter no of iterations:",font=('Roboto',14),bg = '#bdbdbd',fg='#4e342e').pack()
    global iterations3
    iterations3 = tkinter.Entry(pop3,width=5)
    iterations3.pack()
    button6 = tkinter.Button(pop3, text='OK' , command=run_both,width=6,pady=5,bg = '#B2EBF2',font = ('Roboto',14,'bold'),fg='#4e342e')
    button6.pack()
    pop3.mainloop()


def run_SA():
    i = iterations.get()
    pop1.destroy()

    
    run_cmd = 'python3 '+path+'Metaheuristic-NN/Genetic/genetic.py 1 '+i+ ' > result2.txt'
    start = datetime.now()
    os.system(run_cmd)
    end = datetime.now()
    time = end-start

    file = open(path+'Metaheuristic-NN/result2.txt','r')
    lines = file.readlines()
    file.close()
    # test_loss = lines[-2]
    # test_acc = lines[-3]
    acc = lines[-2]
    loss = lines[-1]
    time = 'Execution Time:'+str(time)
    # acc = 'Test Accuracy:'+str(acc)
    tkinter.Label(output2, text = "With Eagle Strategy\nUsing Simulated Annealing:",  font =('Roboto', 16,'bold'),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    tkinter.Label(output2, text = time,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    # tkinter.Label(output2, text = accuracy,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    # tkinter.Label(output2, text = loss,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    tkinter.Label(output2, text = acc,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    tkinter.Label(output2, text = loss,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 



def run_GA():
    i = iterations2.get()
    pop2.destroy()

    run_cmd = 'python3 '+path+'Metaheuristic-NN/Genetic/genetic.py 2 '+i+ ' > result3.txt'
    start = datetime.now()
    os.system(run_cmd)
    end = datetime.now()
    time = end-start

    file = open(path+'Metaheuristic-NN/result3.txt','r')
    lines = file.readlines()
    file.close()
    
    # test_acc = lines[-3]
    acc = lines[-2]
    loss = lines[-1]
    # print(loss)
    # acc=lines[acc]
    # acc = acc[0]
    time = 'Execution Time:'+str(time)
    # acc = 'Test Accuracy:'+str(acc)
    tkinter.Label(output3, text = "With Eagle Strategy\nUsing Genetic Algorithm:",  font =('Roboto', 16,'bold'),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=40) 
    tkinter.Label(output3, text = time,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=40) 
    # tkinter.Label(output2, text = accuracy,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    # tkinter.Label(output2, text = loss,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    tkinter.Label(output3, text = acc,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=40) 
    tkinter.Label(output3, text = loss,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 


def run_both():
    i = iterations3.get()
    pop3.destroy()

    run_cmd = 'python3 '+path+'Metaheuristic-NN/Genetic/genetic.py 3 '+i+ ' > result4.txt'
    start = datetime.now()
    os.system(run_cmd)
    end = datetime.now()
    time = end-start

    file = open(path+'Metaheuristic-NN/result4.txt','r')
    lines = file.readlines()
    file.close()

    ind = lines.index('#\n')
    acc = lines[-2]
    loss = lines[-1]

    time = 'Execution Time:'+str(time)
    # acc = 'Test Accuracy:'+str(acc)
    tkinter.Label(output4, text = "With Eagle Strategy\nUsing Genetic Algorithm\nAnd Simulated Annealing:",  font =('Roboto', 16,'bold'),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=40) 
    tkinter.Label(output4, text = time,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=40) 
    # # tkinter.Label(output2, text = accuracy,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    tkinter.Label(output4, text = acc,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=10) 
    tkinter.Label(output4, text = loss,  font =('Roboto', 12),bg = '#bdbdbd',fg="#4e342e").pack(side=tkinter.TOP,padx=40) 

def gen_graph():
    pass

tkinter.Label(title, text = 'Eagle Strategy Demonstration',  font =('Roboto', 56),bg='#4e342e',fg='#bdbdbd').pack(padx=100,pady = 1) 
tkinter.Label(title, text = 'Artificial Intelligence Project',  font =('Roboto', 32),bg = '#4e342e',fg="#bdbdbd").pack(pady = 1) 
tkinter.Label(title, text = 'Course code: UE17CS325',  font =('Roboto', 20),bg = '#4e342e',fg="#bdbdbd").pack(pady=1) 
tkinter.Label(title, text = '',  font =('Roboto', 14),bg = '#4e342e',fg="#bdbdbd").pack(pady=5) 
tkinter.Label(title, text = 'Sneha Nemadi       Sarang Ravindra       Pragnya Sridhar',  font =('Roboto', 16),bg = '#4e342e',fg="#bdbdbd").pack(pady=1) 

results = dict()



button1 = tkinter.Button(b1, text='Backpropogation', command=run_backprop,width=20,height=3,pady= 5,bg = '#B2EBF2',font = ('Roboto',14),fg='#4e342e')
button1.pack(padx = 50,pady = 30,side=tkinter.TOP) 
# button1.configure(background = "#B2EBF2")

button2 = tkinter.Button(b2, text='Run Eagle Strategy\nwith Simulated Annealing', command=SA_iters,width=20,height=3,pady=5,bg = '#B2EBF2',font = ('Roboto',14),fg='#4e342e')
button2.pack(padx = 50,pady = 30, side = tkinter.TOP) 
# button2.configure(background = "#B2EBF2")

button3 = tkinter.Button(b3, text='Run Eagle Strategy \nwith Genetic Algorithm' , command=GA_iters,width=20,height=3,pady=5,bg = '#B2EBF2',font = ('Roboto',14),fg='#4e342e')
button3.pack(padx = 50,pady = 30, side = tkinter.TOP)

button4 = tkinter.Button(b4, text='Run Eagle Strategy \nwith Genetic Algorithm \nand Simulated Annealing' , command=SAGA_iters,width=20,height=3,pady=5,bg = '#B2EBF2',font = ('Roboto',14),fg='#4e342e')
button4.pack(padx = 50,pady = 30, side = tkinter.TOP)

# button4 = tkinter.Button(b5, text='Generate graphs' , command=gen_graph,width=26,pady=5,bg = '#B2EBF2',font = ('Roboto',14),fg='#4e342e')
# button4.pack(padx = 90,pady = 60, side = tkinter.TOP)

tkinter.mainloop() 
