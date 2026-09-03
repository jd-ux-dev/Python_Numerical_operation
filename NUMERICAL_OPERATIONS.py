#inputs a number from user prints whether the number is prime or not

def idprime():
    history=open("history.txt","a+")
    a=True
    while a:
        n=int(input("Enter a positive integer to check if it is prime or composite:"))
        if n<1:
            print("The no. is not a positive integer.\nTRY AGAIN!")
        else:
            break
    if n==1:
        print("1 is neither prime nor composite.")
    else:
        for i in range(2,n):
            if n%i==0:
                print(n,"is a COMPOSITE number")
                his="{} is a Composite number\n".format(n)
                break
        else:
            print(n,"is a PRIME number")
            his="{} is a Prime number\n".format(n)
    history.write(his)
    history.close()

#inputs a range from user and prints onlythe prime numbers fom the range
def prime_range():
    history=open("history.txt","a+")
    a=True
    while a:
        m=int(input("Enter a positive integer as first no. of the range :"))
        n=int(input("Enter a positive integer as last no. of the range :"))
        if m>n:
            m,n=n,m
        if n<1 and n<1:
            print("The no.s are not  positive integers.\nTRY AGAIN!")
        else:
            break
    if m==1:
        x=2
    else:
        x=m
    l=[]
    for i in range (x,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
    print(l, "are the prime no.s between",m,"to",n)
    history.write(str(l))
    history.write(": are the prime no.s between {} and {}".format(m,n))
    history.close()
#inputs a no. from a user checks if it is  perfect square or not
def perfect_square():
    history=open("history.txt","a+")
    a=True
    while a:
        n=int(input("Enter a positive integer to check if it is perfect square:"))
        if n<1:
            print("The no. is not a positive integer.\nTRY AGAIN!")
        else:
            break
    for i in range(1,n):
            if n%i==0:
                if i*i==n:
                    print(n,"is a perfect square")
                    history.write("{} is a perfect square\n".format(n))
                    break
    else:
           print(n,"is not a perfect square")
           history.write("{} is not a perfect square\n".format(n))
    history.close()
#inputs a no. from a user checks if it is  perfect cube or not
def perfect_cube():
    history=open("history.txt","a+")
    a=True
    n=int(input("Enter a  integer to check if it is perfect cube:"))
    if n<1:
        x=-n
    else:
        x=n
    for i in range(1,x):
            if x%i==0:
                if i*i*i==x:
                    print(n,"is a perfect cube")
                    history.write("{} is a perfect cube\n".format(n))
                    break
    else:
           print(n,"is not a perfect cube")
           history.write("{} is not a perfect cube\n".format(n))
    history.close()
#inputs a no. from user and finds its prime factors
def prime_factor():
    history=open("history.txt","a+")
    a=True
    while a:
        n = int(input("Enter a positive integer: "))
        if n<1:
            print("The no. is not a positive integer.\nTRY AGAIN!")
        else:
            break
    
    org = n
    factors = "1"
    
    i = 2
    while i <= n:
        if n % i == 0:
            factors+="x"+str(i)
            n //= i   # integer division keeps n an integer
        else:
            i += 1
    
    print("The prime factorization of", org, "=", factors)
    history.write("The prime factorization of {} =".format(org))
    history.write(factors)
    history.write("\n")
    history.close()
#Shows the history
def show_history():
    print('----------------HISTORY-----------')
    history=open("history.txt","r")
    print(history.read())
    history.close()
#Deletes history
def del_history():
    history=open("history.txt","w")
    history.write("")
    history.close() 
####################START OF CODE####################################
print('''Welcome to the Calculator''')
a="y"
while a=="y":
    print('''To Proceed choose an operation by typing the number listed alongside it:
•1)To check if a no. is prime or composite
•2)To print the no.s that are prime in a range
•3)To check if a number is a perect square or not
•4)To check if a number is a perfect cube or not
•5)Prime Factorisation
•6)Show calculator history
•7)Delete Calculator history''')
    n=int(input("Choose the operation you favour:"))
    if n==1:
        print("CHOSEN:1)To check if a no. is prime or composite")
        idprime()
    elif n==2:
        print("CHOSEN:2)To print the no.s that are prime in a range")
        prime_range()
    elif n==3:
        print("CHOSEN:3)To check if a number is a perect square or not")
        perfect_square()
    elif n==4:
        print("CHOSEN:4)To check if a number is a perfect cube or not")
        perfect_cube()
    elif n==5:
        print("CHOSEN:5)Prime Factorisation")
        prime_factor()
    elif n==6:
        print("CHOSEN:6)Show calculator history")
        show_history()
    elif n==7:
        print("CHOSEN:7)Delete Calculator history")
        sure=input("Are you sure you want to delete history(y/n):")
        if sure in "Yy":
            del_history()  
            show_history()
    else:
        print("ONLY CHOOSE NO.S BETWEEN 1-7")
    a=input("Want to try again?(y/n):")
    a=a.lower()
print("END OF CODE")        
        






