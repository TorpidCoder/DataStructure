__author__ = "ResearchInMotion"

number = int(input("please enter the number : "))

while number!= 1 and number !=4:
    number = sum(list(map(lambda x:int(x)**2,str(number))))
    print(number==1)
