class book:
    def __init__(self,title,author,publisher,price,royalty):
        self.title=title
        self.author=author
        self.publisher=publisher
        self.price=price
        self.royalty=royalty

    def gettitle(self):
        return self.title

    def getauthor(self):
        return self.author


    def getpublisher(self):
        return self.publisher

    def getprice(self):
        return self.price

    def settitle(self,a):
        self.title=a
        return

    def setauthor(self,a):
        self.title=a
        return

    def setpublisher(self,a):
        self.publisher=a
        return
    def setprice(self,a):
        self.price=a
        return
    
    def setroyalty(self,a):
        if a>=500:
            self.royalty+=0.10*a
        elif a>=1500:
            self.royalty+=0.125*(a-500)
        else:
            self.royalty+=0.15*(a-1500)
        
        return

class ebook(book):
    def __init__(self,title,author,publisher,price,royalty,epub,pdf,mobi):
        super().__init__(title,author,publisher,price,royalty)
        self.epub=epub
        self.pdf=pdf
        self.mobi=mobi

        def setroyalty(self,a):
            if a>=500:
                self.royalty+=0.10*a - 0.12*a
            elif a>=1500:
                self.royalty+=0.125*(a-500)-0.12*a
            else:
                self.royalty+=0.15*(a-1500)-0.12*a
            return
        

        
    
