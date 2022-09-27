#1. Εισαγωγή Βιβλίου

class bookstore:
    
    def __init__(self,ISBN, Author, Title, Type, Price):
        self.ISBN=ISBN
        self.Author=Author
        self.Title=Title
        self.Type=Type
        self.Price=Price
        
        
    def setISBN(self,x): 
        self.ISBN=x
    def getISBN(self):
        return self.ISBN
        
    def setAuthor(self,x): 
        self.Author=x
    def getAuthor(self):
        return self.Author
        
    def setTitle(self,x): 
        self.Title=x   
    def getTitle(self):
        return self.Title
        
    def setType(self,x): 
        self.Type=x   
    def getType(self):
        return self.Type
        
    def setPrice(self,x): 
        self.Price=x  
    def getPrice(self):
        return self.Price    
    
 #Check this!!!
    def accounts(self):
        customer[self.Title]=self.Price
        return customer


customer={}    
answer=''
print("Καταχώρηση")
print("----------")
while(answer!='q'):
    ISBN=input  ("Write the ISBN             : ")
    Author=input("Fill in the author's name  : ")
    Title=input ("Book title                 : ")
    Type=input  ("Category                   : ")
    Price=input ("Price                      : ")
    break
    
while True: 

    a=input("Would you like to add another book?" " Y/N: ") 
    if a=="N": 
        print("Please write your username and exit: ") 
        username=input() 
        break 

    elif a=="Y": 
        ISBN=input  ("Write the ISBN             : ")
        Author=input("Fill in the author's name  : ")
        Title=input ("Book title                 : ")
        Type=input  ("Category                   : ")
        Price=input ("Price                      : ")

bookexample=bookstore("978-960-512-718-3", "ΝΤΕΙΤΕΛ ΠΑΟΥΛ,ΝΤΕΙΤΕΛ ΧΕΡΒΙ", "PYTHON ΓΙΑ ΠΡΟΓΡΑΜΜΑΤΙΣΤΕΣ", "Computer Programming", "55")        
bookexample2=bookstore("978-960-512-744-2", "ΝΤΕΙΤΕΛ ΤΖ. ΠΟΛ, ΝΤΕΙΤΕΛ Μ. ΧΑΡΒΕΙ", "ΕΙΣΑΓΩΓΗ ΣΤΗΝ PYTHON ΓΙΑ ΤΙΣ ΕΠΙΣΤΗΜΕΣ ΥΠΟΛΟΓΙΣΤΩΝ ΚΑΙ ΔΕΔΟΜΕΝΩΝ", "Computer Programming", "65" )

books=bookexample.accounts()

    
    
    

