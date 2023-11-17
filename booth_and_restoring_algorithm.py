# booth algorithim 3x7 = 21
# import module
from prettytable import PrettyTable 

Operation = int(input("please enter 1 for Multiplication (Booth's Algorithim) OR 2 for Division (Restoring Unsigned Binary Division): "))

# initial values
M = int(input("please enter a 4 digit binary number for the Multiplicand/Divisior (M): "), 2)        # Multiplicand 0b0111   
Q = int(input("please enter a 4 digit binary number for the Multiplier/Dividend (Q): "), 2)          # Multiplier Q = 0b0011
A = 0b0000
Q0 = Q & 0b0001
Q4 = Q & 0b1000
Q_1 = 0

# the count equals the bit number
n = 4

# Specify the Column Names while initializing the Table 
myTable = PrettyTable(["cycle", "A", "Q", "Q-1", "M"]) 
myTable.add_row(["initial values", bin(((1 << 4) - 1) & A), bin(Q), bin(Q_1), bin(M)]) 
myTable.add_row(["========", "========", "========", "========", "========"])

def BoothAlgorithim(M, Q):
    
    i = 0
    A = 0b0000
    Q0 = Q & 0b0001
    Q4 = Q & 0b1000
    Q_1 = 0
    # the count equals the bit number
    n = 4

    while n != 0: 
        i = i + 1
        if [Q0, Q_1] == [0, 1]:
            A = A + M
            
            
        elif [Q0, Q_1] == [1, 0]:
            A = A - M            
        
        myTable.add_row([i, bin(((1 << 4) - 1) & A), bin(Q), bin(Q_1), bin(M)])
        
        # shifting Q, A and Q-1 regesters by one digit
        Q0 = Q & 0b0001
        Q_1 = Q0
        Q = Q >> 1
        Q4 = (A & 0b0001)
        Q = Q | Q4 << 3
        A = A >> 1
        Q0 = Q & 0b0001
        
        # Add rows 
        myTable.add_row(["", bin(((1 << 4) - 1) & A), bin(Q), bin(Q_1), bin(M)]) 
        myTable.add_row(["========", "========", "========", "========", "========"])
        
        n = n - 1
        
    # Print the results
    print(myTable)
    result = A << 4 | Q 
    
    print("the result is ", bin(result), "which equals ", result,"in decimals")

#########################################################################################
def RestoringAlgorithim(M, Q):
    i = 0
    A = 0b0000
    Q0 = Q & 0b0001
    Q4 = Q & 0b1000
    Q_1 = 0
    # the count equals the bit number
    n = 4

    while n != 0:
        i = i + 1

        # shifting Q and A regesters by one digit
        Q0 = Q & 0b0001
        Q = Q >> 1
        Q4 = (A & 0b0001)
        Q = Q | Q4 << 3
        A = A >> 1
        Q0 = Q & 0b0001
        
        # adding register values to the table
        myTable.add_row([i, bin(((1 << 4) - 1) & A), bin(Q), "N/A", bin(M)])

        A = A - M
        if A < 0:
            Q = Q & ~(1 << 0)
        else:
            Q = Q & (1 << 0)
        
        myTable.add_row(["", bin(((1 << 4) - 1) & A), bin(Q), "", bin(M)]) 
        myTable.add_row(["========", "========", "========", "========", "========"])
        
        n = n - 1
    
    print(myTable)
    result = Q 
    print("the Quotient is ", bin(result), "which equals ", result,"in decimals")
    print("the remainder is ", bin(A), "which equals ", A,"in decimals")

if Operation == 1 and n != 0:
    BoothAlgorithim(M, Q)
else:
    RestoringAlgorithim(M, Q)
