# Fantasy Cricket Application

![fanatsy_cricket](https://user-images.githubusercontent.com/40792388/48671048-56b9f400-eb48-11e8-9a7a-ce62e3c40a58.png)

----

> This is a Fantasy cricket Desktop application build in python that allows user to build their own dream cricket team , analyse it and play !!!....Isn't it exciting.....

---


## Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [Use of Badges](#use-of-badges)
- [Features](#features)
- [Installation](#installation)
- [Code Snippet](#code-snippet)
- [Getting Started](#getting-started)
- [Tools](#tools)



---

## Description
> Fanatsy cricket is build in python using `Pyqt5` library specifically `QtCore`  `QtGui`  `QtWidgets` for **GUI** development and `SqliteStudio` for **Back end database connectivity**.


---

### Use of Badges

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![Github Issues](http://githubbadges.herokuapp.com/badges/badgerbadgerbadger/issues.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger/issues)  [![Badges](http://img.shields.io/:badges-9/9-ff6799.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger)

- For more on these wonderful `badges`, refer to <a href="http://badges.github.io/badgerbadgerbadger/" target="_blank">`badgerbadgerbadger`</a>.



![open_team](https://user-images.githubusercontent.com/40792388/48671417-d5656000-eb4d-11e8-8213-22cf1dfe20e2.gif)



## Features
  * Create your own dream team in Auction
  * Save your team and evaluate it later as per **Match**
  * Initially a Owner will be provided with `1000 Points` to purchase there players
  * Team selection follows basic cricketing rules 
  * Not more than 5 batsman/bowler
  * Only a Single Wicket Keeper





## Installation
* install `PyQt5` python library using pip
```python
pip install PyQt5

```
or
```python
pip3 install PyQt5

```
* Install SqliteStudio for creating database for the `teams` , `players` , `stats`

- Download Sqlite Studio - [Sqlitestudio](https://sqlitestudio.pl/index.rvt)



![code](https://user-images.githubusercontent.com/40792388/48670940-042c0800-eb47-11e8-806a-5f8d76b803a9.gif)



## Code Snippet

```python
  self.horizontalLayout.addWidget(self.label)
  spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
  
   self.actionNEW_Team = QtWidgets.QAction(MainWindow)
   self.actionNEW_Team.setObjectName("actionNEW_Team")
   self.horizontalLayout_2.addWidget(self.lw1)
   spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
```






---
## Getting Started
```
git clone https://github.com/dilip29/Summer-Training-Python-development/
```
* install the required tools 

* fork or download the repo 

* run the following command in terminal

```
python3 fantasy.py
```


![evaluate_team](https://user-images.githubusercontent.com/40792388/48671631-6c7fe700-eb51-11e8-9244-50fa02df77ea.gif)




## Tools
### References
* [Atom](https://atom.io/)
* [SqliteStudio](https://sqlitestudio.pl/index.rvt)
* [Internshala-Summer-Trainings](https://trainings.internshala.com/python-training)
* [Python](https://www.python.org/)



---



## License
---
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)


[Back To The Top](#Fantasy-Cricket-Application)
