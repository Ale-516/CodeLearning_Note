#----------------#----------------
#Shortcut keys
#{
    # ctrl+tabs switch from one file to another
    # ctrl+alt+N run the code
    # ctrl+shift+` creat a new terminal
    # ctrl+` change to the terminal
    # multi line comments in python """ context """
#}
#----------------#----------------


#----------------#----------------
#Type of Expressions:
#{
    #01 primitiva expressions: Number of numeral, Name, String
    #02 call expresions: max(2,3) Operator(Operand,Operand) and an Operand can also be called as an expression
#}

#Execution rules for assignment statements
#{
    #01 from left to right
    #02 bindi all names to the left of = to the resulting values in the current frame
#}
#----------------#----------------


#----------------#----------------
#An example
#{
    #f=min
    #f=max
    #g, h = min, max                |g = min, h = max, f = max
    #max = g                        |g = min, h = max, max = min, f = max              
    #max(f(2, g(h(1,5), 3)), 4)     |h(1,5) = 5 => g(h(1, 5), 3) = 3 => f(2, g(h(1, 5))) = 3, max(...) = min(...) = 3 
#}
#----------------#----------------


#----------------#----------------
#Assignment is a simple means of abstraction:                   binds names to values
#Function definition is a more powerful means of abstraction:   binds name to expression
#The way to define a function
#{
    #def <name>(<formal parameters>):
    #return <return expression>
#}
#----------------#----------------


#----------------#----------------
#Calling user-defined function
#Add a local frame, forming a new encirment
#Bind the function's formal parameters to its arguments in that frame
#Execute the body of the function on that new environment
from operator import mul            # Frames                 objects
def square(x):                      #  Global frame        
    return mul(x,x)                 #  mul                   func mul(...)   
print(square(-2))                   #  square                func square(...)
#                                   # square(Local frame)
#                                   #  x -2 => return 4
#---------------#-----------------


#---------------#-----------------
#Looking up names in environments
#An environment is a sequence of frames
#A name evaluates to the value bound to that name in earliest frame of the current environment in which that name is found
#Firstly, look for that name in the local frame
#Secondly, if it is not found, look for it in the global frame
#Here is a example:
from operator import mul            #Frame                      Objects
def square(square):                 #Global frame              func mul(...)
    return mul(square,square)       #   mul                    func square(square)
print (square(4))                   #   square
#print out 16                       #square(Local frame)
#--------------#------------------  #   square 4


#--------------#------------------
#{
    #if <condition 01>:
        # <statements>
    #elif <condition 02>:
        # <statements>
    #elif <condition 03>:
        # <statements>
    #else:
        # <statements>
#}

#{
    # for <iterating_var> in <sequence>
        # <statements(s)>
#}
