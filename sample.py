import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.neighbors.typedefs
import sklearn.neighbors.quad_tree
import sklearn.tree
import sklaern.tree._utils
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from tkinter import *
import sys, os 
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
top = Tk()

top.geometry("400x250")

def print():
    data = pd.read_csv("Mall_Customers.csv")
    X = data.iloc[:,2:3].values
    Y = data.iloc[:,3].values
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)
    regressor = LinearRegression()                     
    regressor.fit(X_train,Y_train)
    Y_pred = regressor.predict(X_test)                 
    #print(regressor.score(X_test,Y_test))             
    plt.scatter(X_test,Y_pred)                                   
    plt.show()

# creating label
uname = Label(top, text="Username").place(x=30, y=50)

# creating label
password = Label(top, text="Password").place(x=30, y=90)
resource_path('Mall_Customers.csv')
sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue",command=print).place(x=30, y=120)

# Entry is for text field
e1 = Entry(top, width=20).place(x=100, y=50)

e2 = Entry(top, width=20).place(x=100, y=90)

top.mainloop()



        

