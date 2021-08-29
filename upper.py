def lower_case():
    c=input("write your comment:")
    print(c)
    x=input ("what do you want to do with this ,if you want to convert it to upper write upper or else write lower:")
    if x == "upper":
        print(c.upper())
    else:
        print(c.lower())
lower_case()    