'''here,this code is to check the word in variable p'''

def myClass():
    p=input("write what you want")
    #this is going to ask user to write any thing user want

    x=input("which word you want to check")# this will ask user for which variable you want to check
    if x in p:#this will check is there x(variable) in p() 
        print("this is in this line")# if there is x then it will print"this is not in line
    elif x not in p:#if not then it will print "this is not in the clss"
        print("this is not in this sentence")
    
myClass() 