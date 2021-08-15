import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn import preprocessing
from sklearn import svm
from sklearn import neighbors
import mysql.connector as connection
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import random
from tkinter import messagebox
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from veza import Konekcija

 
class GuestPrediction:
    def __init__(self,root):
        self.root=root
        self.root.title("Mašinsko učenje")
        self.root.geometry("510x500+300+350")

        self.var_gender=IntVar()
        self.var_reservation=IntVar()
        self.var_points=IntVar()
        self.var_rezident=IntVar()

        self.var_klas=IntVar()
        self.var_klas2=IntVar()
        self.var_vip=IntVar()
        self.var_vip2=IntVar()
        
        frame=Frame(self.root,bg="cyan")
        frame.place(x=0,y=0,width=510,height=500)


        genderLbl=Label(frame,text="Gender",bg="cyan",font=("times new roman",14,"bold"),padx=2,pady=6)
        genderLbl.grid(row=0,column=0,sticky=W)

        genderEntry=ttk.Entry(frame,textvariable=self.var_gender, font=("times new roman",14,"bold"),width=10)
        genderEntry.grid(row=0,column=1)

        reservationLbl=Label(frame,text="Reservation number",bg="cyan",font=("times new roman",14,"bold"),padx=2,pady=6)
        reservationLbl.grid(row=1,column=0,sticky=W)

        reservationEntry=ttk.Entry(frame,textvariable=self.var_reservation, font=("times new roman",14,"bold"),width=10)
        reservationEntry.grid(row=1,column=1)

        pointsLbl=Label(frame,text="Points",bg="cyan",font=("times new roman",14,"bold"),padx=2,pady=6)
        pointsLbl.grid(row=2,column=0,sticky=W)

        pointsEntry=ttk.Entry(frame,textvariable=self.var_points, font=("times new roman",14,"bold"),width=10)
        pointsEntry.grid(row=2,column=1)

        rezidentLbl=Label(frame,text="Rezident",bg="cyan",font=("times new roman",14,"bold"),padx=2,pady=6)
        rezidentLbl.grid(row=3,column=0,sticky=W)

        rezidentEntry=ttk.Entry(frame,textvariable=self.var_rezident, font=("times new roman",14,"bold"),width=10)
        rezidentEntry.grid(row=3,column=1)


        btnModel1=Button(frame,text="Model1",command=self.prediction, font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnModel1.grid(row=4,column=0,padx=1,sticky=W)

        classification1Lbl=Label(frame,text="Classification1",bg="cyan",font=("times new roman",14,"bold"),padx=2,pady=6)
        classification1Lbl.grid(row=4,column=1,sticky=W)

        classification1Entry=ttk.Entry(frame,textvariable=self.var_klas, font=("times new roman",14,"bold"),width=7)
        classification1Entry.grid(row=4,column=2)

        prediction1Lbl=Label(frame,text="Prediction1",bg="cyan",font=("times new roman",14,"bold"),padx=2,pady=6)
        prediction1Lbl.grid(row=4,column=3,sticky=W)

        prediction1Entry=ttk.Entry(frame,textvariable=self.var_vip, font=("times new roman",14,"bold"),width=7)
        prediction1Entry.grid(row=4,column=4)

        btnModel2=Button(frame,text="Model2",command=self.prediction2, font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnModel2.grid(row=5,column=0,padx=1,sticky=W)

        classification2Lbl=Label(frame,text="classification2",bg="cyan",font=("times new roman",14,"bold"),padx=2,pady=6)
        classification2Lbl.grid(row=5,column=1,sticky=W)

        classification2Entry=ttk.Entry(frame,textvariable=self.var_klas2, font=("times new roman",14,"bold"),width=7)
        classification2Entry.grid(row=5,column=2)

        prediction2Lbl=Label(frame,text="Prediction2",bg="cyan",font=("times new roman",14,"bold"),padx=2,pady=6)
        prediction2Lbl.grid(row=5,column=3,sticky=W)

        prediction2Entry=ttk.Entry(frame,textvariable=self.var_vip2, font=("times new roman",14,"bold"),width=7)
        prediction2Entry.grid(row=5,column=4)

        btnStablo=Button(frame,text="Tree",command=self.decisionTree , font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnStablo.grid(row=6,column=0,padx=1,sticky=W)

        btnPlot=Button(frame,text="Plot",command=self.plot, font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnPlot.grid(row=7,column=0,padx=1,sticky=W)


    def prediction(self):
        db = connection.connect(user='root', password='stevica011',host='127.0.0.1',database='hotel',use_pure=True)
        query = "SELECT * FROM gosti"
        df = pd.read_sql(query,db)
        db.close() 

        df=df.drop(['idgosti','ime','prezime','godine','telefon','email','broj dokumenta','iddokument'], axis = 1)
        labels = df[['pol','rezident']]
        label_encoders={}
        df_encoded = pd.DataFrame()
        for column in df:
            if column in labels:
                label_encoders[column] = preprocessing.LabelEncoder()
                label_encoders[column].fit(labels[column]) 
                df_encoded[column] = label_encoders[column].transform(
                    df[column])
            else:
                df_encoded[column] = df[column]
        df_encoded.to_csv("guests.csv",encoding="utf-8")
        features = np.array(df_encoded.drop(['počasnigost'], 1))
        label = np.array(df_encoded['počasnigost'])
        scaled_features = preprocessing.MinMaxScaler(
            feature_range=(0, 1)).fit_transform(features)

        features_train, features_test, label_train, label_test = model_selection.train_test_split(
            scaled_features,
            label,
            test_size=0.2
        )
        classifier1 = neighbors.KNeighborsClassifier()
        classifier1.fit(features_train, label_train)
        classifier1.score(features_test, label_test)
        k1=classifier1.score(features_test, label_test)
        self.var_klas.set(k1)
        
        data1 = [self.var_gender.get(),self.var_reservation.get(),self.var_points.get(),self.var_rezident.get()]
        data1 = np.array(data1)
        data1 = data1.reshape(1, -1)
        p1=classifier1.predict(data1)
        self.var_vip.set(p1)


    def prediction2(self):
        db = connection.connect(user='root', password='stevica011',host='127.0.0.1',database='hotel',use_pure=True)
        query = "SELECT * FROM gosti"
        df = pd.read_sql(query,db)
        db.close() 

        df=df.drop(['idgosti','ime','prezime','godine','telefon','email','broj dokumenta','iddokument'], axis = 1)
        labels = df[['pol','rezident']]
        label_encoders={}
        df_encoded = pd.DataFrame()
        
        for column in df:
            if column in labels:
                label_encoders[column] = preprocessing.LabelEncoder()
                label_encoders[column].fit(labels[column]) 
                df_encoded[column] = label_encoders[column].transform(
                    df[column])
            else:
                df_encoded[column] = df[column]
        df_encoded.to_csv("guests2.csv",encoding="utf-8")

        features = np.array(df_encoded.drop(['počasnigost'], 1))
        label = np.array(df_encoded['počasnigost'])

        scaled_features = preprocessing.MinMaxScaler(
            feature_range=(0, 1)).fit_transform(features)
        features_train,features_test,label_train,label_test = model_selection.train_test_split(
            scaled_features,
            label,
            test_size = 0.33
        )

        classifier2 = svm.SVC()
        classifier2.fit(features_train,label_train)
        k2=classifier2.score(features_test, label_test)
        self.var_klas2.set(k2)

        data2 = [self.var_gender.get(),self.var_reservation.get(),self.var_points.get(),self.var_rezident.get()]
        data2 = np.array(data2)
        data2 = data2.reshape(1, -1)
        p2=classifier2.predict(data2)
        self.var_vip2.set(p2)


    def decisionTree(self):
        db = connection.connect(user='root', password='stevica011',host='127.0.0.1',database='hotel',use_pure=True)
        query = "SELECT * FROM gosti"
        df = pd.read_sql(query,db)
        db.close() 

        df=df.drop(['idgosti','ime','prezime','telefon','email','broj dokumenta','iddokument'], axis = 1)
        labels = df[['pol','rezident']]
        label_encoders={}
        df_encoded = pd.DataFrame()

        for column in df:
            if column in labels:
                label_encoders[column] = preprocessing.LabelEncoder()
                label_encoders[column].fit(labels[column]) 
                df_encoded[column] = label_encoders[column].transform(
                    df[column])
            else:
                df_encoded[column] = df[column]
        
        df_encoded.to_csv("guests3.csv",encoding="utf-8")

        features = np.array(df_encoded.drop(['počasnigost'], 1))
        label = np.array(df_encoded['počasnigost'])
    
        ostalo = ['pol','godine','brojrezervacija','bodovi','rezident']
 
        X = df_encoded[ostalo] 
        y = df_encoded['počasnigost']

        dtree = DecisionTreeClassifier()
        dtree = dtree.fit(X, y)
    
        dtree = DecisionTreeClassifier()
        dtree = dtree.fit(features,label)

        data = tree.export_graphviz(dtree, out_file=None, feature_names=ostalo)
        graph = pydotplus.graph_from_dot_data(data)
        graph.write_png('mydecisiontree.png')

        img=pltimg.imread('mydecisiontree.png')
        imgplot = plt.imshow(img)
        plt.show()

    def plot(self):
        db = connection.connect(user='root', password='stevica011',host='127.0.0.1',database='hotel',use_pure=True)
        query = "SELECT * FROM gosti"
        df = pd.read_sql(query,db)
        db.close() 
        x = np.array(df['ime'].head(30))
        y = np.array(df['počasnigost'].head(30))
        plt.bar(x, y)
        plt.show()



'''root=Tk()
object=GuestPrediction(root)
mainloop()'''