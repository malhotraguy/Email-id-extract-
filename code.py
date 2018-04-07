import re
while True:
    x=input("enter your email id: ")
    # TO extrate the correct email format
    y=re.findall('\S+@\S+[".com"]',x)
    # Or you can use:
    #y=re.findall('\S+@\S+\.com',x)
    #print(y)
    if not y:
            print("Invalid Email id")
            ex=input("Enter 1 to exit OR 2 to continue: ")
            if ex=="1":
                break
            else:
                pass
    else:
        print("your email id is :",y[0] )
        #To to extrate only domain name excluding the "@" and ".com"
        domain=re.findall('@([^  ]*).com',y[0])
        print("And the domain name of your email is:",domain[0])
        break
    
