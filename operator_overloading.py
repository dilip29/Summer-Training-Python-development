class distance:
    def __init__(self,x,y):
        self.inches=y
        self.feet=x
    def __add__(self,other):
        finalfeet=self.feet+other.feet
        finalinches=self.inches+other.inches
        print(other.inches)
        if finalinches >=12:
            finalfeet+=1
            finalinches-=12
            
        return distance(finalfeet,finalinches)

    def __str__(self):
        return "the feet="+str(self.feet)+"and inches ="+str(self.inches)



d1=distance(8,10)
d2=distance(9,6)
d3=d1+d2
print(d3)



