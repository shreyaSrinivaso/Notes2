#while loop
'''
While is based on condition / boolean output 
difference between while and for : while
while : will execute based on condition 
for : will execute based on number of times 
'''
a=10

while a>5: # checks true/false 
    print(f"the value of a is : {a}") => 10,9,8,7,6
    a-=1  # we need to have a condition for while loop to end , else we'll end up with infinite loop .

a=10

while a>5:
    if a%6 == 0:
        break
    print(f"the value of a is : {a}") => 10,9,8,7
    a-=1
    
while a>5:
    if a%7 == 0:  
        continue
    print(f"the value of a is : {a}") => 10,9,8,(7>5),(7>5),(7>5).......................
    a-=1

while a>5:
    a-=1
    if a%7 == 0:  
        continue
    print(f"the value of a is : {a}") => 9,8,6,5.......................

a=10
L1=[3,4,56,7,10,11,12]
i=0

while(a in L1):
    print("a=",L1[i]) =>3,4,56,7
    i=i+1
    if(a== L1[i]):
        break  


i=0
while True:
    print("hello world")
    i=i+1
    if i==10:
        break
        
a= True
i=0

while a:
    print("hello world")
    i=i+1
    if(i == 5):
        a=False

val=1000
i=0
while val:
    print("hello world")
    i=i+1
    if(i == 5):
        break
        
        
FUNCTIONS:

def addmarks(x,y):
    return x+y

print(addmarks(10,8))

#In-Built function : function def is already available inside the installed package , we need to call the function
#used-defined  : we need to write the function definition and function call 
#function call
#function definition 

def <function_name>(args):
    <code1>
    <code2>
    return (default None)