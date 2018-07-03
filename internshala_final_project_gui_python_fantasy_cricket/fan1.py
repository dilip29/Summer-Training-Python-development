# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fantasy_cricket.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(True)
        font.setPointSize(12)
        self.label.setFont(font)
        
        
 
        

        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)



       

        
        self.label_2.setFont(font)
        
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setObjectName("t1")
        self.horizontalLayout_2.addWidget(self.t1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_3.setFont(font)
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setObjectName("t2")
        self.horizontalLayout_2.addWidget(self.t2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_4.setFont(font)
        self.t3 = QtWidgets.QLineEdit(self.centralwidget)
        self.t3.setObjectName("t3")
        self.horizontalLayout_2.addWidget(self.t3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_5.setFont(font)
        self.t4 = QtWidgets.QLineEdit(self.centralwidget)
        self.t4.setObjectName("t4")
        self.horizontalLayout_2.addWidget(self.t4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_7.setFont(font)
        self.t5 = QtWidgets.QLineEdit(self.centralwidget)
        self.t5.setObjectName("t5")
        self.horizontalLayout_3.addWidget(self.t5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_6.setFont(font)
        self.t6 = QtWidgets.QLineEdit(self.centralwidget)
        self.t6.setObjectName("t6")
        self.horizontalLayout_3.addWidget(self.t6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rbtn1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn1.setObjectName("rbtn1")
        self.horizontalLayout_4.addWidget(self.rbtn1)

        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setBold(True)
        font.setPointSize(10)
        self.rbtn1.setFont(font)
        
        self.rbtn2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn2.setObjectName("rbtn2")
        self.rbtn2.setFont(font)
        self.horizontalLayout_4.addWidget(self.rbtn2)
        self.rbtn3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn3.setObjectName("rbtn3")
        self.rbtn3.setFont(font)
        self.horizontalLayout_4.addWidget(self.rbtn3)
        self.rbtn4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn4.setObjectName("rbtn4")
        self.horizontalLayout_4.addWidget(self.rbtn4)
        self.rbtn4.setFont(font)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)

        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(True)
        font.setPointSize(12)
        self.label_8.setFont(font)
        
        self.t7 = QtWidgets.QLineEdit(self.centralwidget)
        self.t7.setObjectName("t7")
        self.horizontalLayout_4.addWidget(self.t7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setObjectName("list1")
        self.horizontalLayout_5.addWidget(self.list1)

        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.list1.setFont(font)
        self.t1.setFont(font)
        self.t2.setFont(font)
        self.t3.setFont(font)
        self.t4.setFont(font)
        self.t5.setFont(font)
        self.t6.setFont(font)
        self.t7.setFont(font)
        
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setObjectName("list2")
        self.horizontalLayout_5.addWidget(self.list2)
        self.list2.setFont(font)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)

        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(True)
        font.setPointSize(12)
        self.pushButton.setFont(font)

        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")

        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setBold(True)
        font.setPointSize(10)
        self.menuManage_Teams.setFont(font)
        self.menubar.setFont(font)
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.addSeparator()
        self.menubar.addAction(self.menuManage_Teams.menuAction())


        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)


        self.rbtn1.toggled.connect(self.ctg)
        self.rbtn2.toggled.connect(self.ctg)
        self.rbtn3.toggled.connect(self.ctg)
        self.rbtn4.toggled.connect(self.ctg) 


        

        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu)
        self.pushButton.clicked.connect(self.exit)
        
        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.avl=1000
        self.used=0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_2.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.label_3.setText(_translate("MainWindow", "Bowler (BOW)"))
        self.label_4.setText(_translate("MainWindow", "Wicketkeeper (WK)"))
        self.label_5.setText(_translate("MainWindow", "All-Rounders (AR)"))
        self.label_7.setText(_translate("MainWindow", "Points Available"))
        self.label_6.setText(_translate("MainWindow", "Points Used"))
        self.rbtn1.setText(_translate("MainWindow", "BAT"))
        self.rbtn2.setText(_translate("MainWindow", "BOW"))
        self.rbtn3.setText(_translate("MainWindow", "AR"))
        self.rbtn4.setText(_translate("MainWindow", "WK"))
        self.label_8.setText(_translate("MainWindow", "Team Name"))
        self.pushButton.setText(_translate("MainWindow", "EXIT Application"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))



    def exit(self):
        import sys
        self.showdlg("Thank YOU for Visiting....Hope you enjoyed !!")
        sys.exit()





    def menu(self,action):
        txt=(action.text())
    
        if txt=='NEW Team':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.list1.clear()
            self.list2.clear()
            #self.t7.setText("???")
            
            #self.dial()
            text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter name of team:")
            if ok:
                self.t7.setText(str(text))

            self.show()


        if txt=='SAVE Team':
            count=self.list2.count()
            selected=""
            for i in range(count):
                selected+=self.list2.item(i).text()
                if i<count:
                    selected+=","
            self.saveteam(self.t7.text(),selected,self.used)

        if txt=='OPEN Team':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.list1.clear()
            self.list2.clear()
            self.show()
            #print("rgr")
            self.openteam()


        if txt=='EVALUATE Team':
            from dlgscore import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            #print("effieh")
            ret=Dialog.exec()
            
            


        


    def show(self):
        #print("vvrv")
        self.t1.setText(str(self.bat))
        self.t2.setText(str(self.bwl))
        self.t3.setText(str(self.wk))
        self.t4.setText(str(self.ar))
        #print("rrrr")
        self.t5.setText(str(self.avl))
        self.t6.setText(str(self.used))
        #print("efef")



    def criteria(self,ctgr,item):
        msg=''
        if ctgr=="BAT" and self.bat>=5:msg="Batsmen not more than 5"
        if ctgr=="BWL" and self.bwl>=5:msg="bowlers not more than 5"
        if ctgr=="AR" and self.ar>=3:msg="Allrounders not more than 3"
        if ctgr=="WK" and self.wk>=1:msg="Wicketkeepers not more than 1"
        if msg!='':
            #msg="You Have Exhausted your Points"
            self.showdlg(msg)
            return False
        
        if self.avl<=0:
            msg="You Have Exhausted your Points"
            self.showdlg(msg)
            return False
        
        if ctgr=="BAT":self.bat+=1
        if ctgr=="BWL":self.bwl+=1
        if ctgr=="AR":self.ar+=1
        if ctgr=="WK":self.wk+=1

        
        sql="SELECT value from stats where player='"+item.text()+"'"
        cur=conn.execute(sql)
        row=cur.fetchone()
        self.avl-=int(row[0])
        self.used+=int(row[0])
        return True

    
    


    def removelist1(self,item):
        
        ctgr=''
        if self.rbtn1.isChecked()==True:ctgr='BAT'
        if self.rbtn2.isChecked()==True:ctgr='BWL'
        if self.rbtn3.isChecked()==True:ctgr='AR'
        if self.rbtn4.isChecked()==True:ctgr='WK'
        ret=self.criteria(ctgr,item)
        
        if ret==True:
            self.list1.takeItem(self.list1.row(item))
            
            self.list2.addItem(item.text())
            self.show()
            


    def ctg(self):
        ctgr=''
        if self.rbtn1.isChecked()==True:ctgr='BAT'
        if self.rbtn2.isChecked()==True:ctgr='BWL'
        if self.rbtn3.isChecked()==True:ctgr='AR'
        if self.rbtn4.isChecked()==True:ctgr='WK'
       	
        self.fillList(ctgr)


    def removelist2(self,item):
        self.list2.takeItem(self.list2.row(item))
        
        cursor = conn.execute("SELECT player,value, ctg from stats where player='"+item.text()+"'")
        row=cursor.fetchone()
        self.avl=self.avl+int(row[1])
        self.used=self.used-int(row[1])
        ctgr=row[2]
        if ctgr=="BAT":
            self.bat-=1
            if self.rbtn1.isChecked()==True:self.list1.addItem(item.text())
        if ctgr=="BWL":
            self.bwl-=1
            if self.rbtn2.isChecked()==True:self.list1.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.rbtn3.isChecked()==True:self.list1.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.rbtn4.isChecked()==True:self.list1.addItem(item.text())
        self.show()


    def fillList(self,ctgr):
        if self.t7.text()=='':
            self.showdlg("Enter name of team")
            return
        
        self.list1.clear()
        sql="SELECT player from players where ctg='"+ctgr+"';"
        cur=conn.execute(sql)
        for row in cur:
            selected=[]
            for i in range(self.list2.count()):
                selected.append(self.list2.item(i).text())
            if row[0] not in selected:self.list1.addItem(row[0])
            
        

    def openteam(self):
        #print("rvrjbv")
        #import sqlite3
        #mycon = sqlite3.connect('fantasy.db')
        
        #mycur=mycon.cursor()
       
        sql="select name from teams;"
        #print("efef")
        cur=conn.execute(sql)
        #print("vebjb")
        teams=[]
        #print("rrr")
        #cur=mycur.fetchall()
        for row in cur:
            teams.append(row[0])
        
        team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Dream","Choose A Team",teams,0,False)
        if ok and team:
            self.t7.setText(team)
        
        sql1="SELECT players,value from teams where name='"+team+"';"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        #print("ooo")
        selected=row[0].split(',')
        #print(selected)
        self.list2.addItems(selected)
        self.used=row[1]
        
        self.avl=1000-row[1]
        count=self.list2.count()

        ##iterate to count no. of specific players

        for i in range(count-1):
            ply=self.list2.item(i).text()
            #print(ply)
            sql="select ctg from stats where player='"+ply+"';"
            
            cur=conn.execute(sql)
            
            row=cur.fetchone()
            #print(row)
            ctgr=row[0]
            #print("ej")
            if ctgr=="BAT":self.bat+=1
            if ctgr=="BWL":self.bwl+=1
            if ctgr=="AR":self.ar+=1
            if ctgr=="WK":self.wk+=1  

        #print("vdkn")
        self.show()
        #print("fece")
        



        

    def saveteam(self,nm,ply,val):
        #print("rvrv")
        
        if self.bat+self.bwl+self.ar+self.wk!=11:
            self.showdlg("Insufficient players")
            return
        
        #print("frbfj")
        sql="INSERT INTO teams (name,players,value) VALUES ('"+nm+"','"+ply+"','"+str(val)+"');"
        #print("f3f4")
        try:
            #print("bjr")
            cur=conn.execute(sql)
            #print("dehe")
            self.showdlg("Team Saved Succesfully")
            conn.commit()
        except:
            self.showdlg("Error in Operation")
            conn.rollback()   
        
        
    def showdlg(self,msg):
        #print("ecb")
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Dream Team selector")
        ret=Dialog.exec()
    



        


    
if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect('fantasy.db')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

