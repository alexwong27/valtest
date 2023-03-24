#Definitions: M=margin, G=growth, R=retention, A=ARR multiple, V=valuation, N=Average MRR

# define the independent variables
M = float(input("Enter the value of M: "))
G = float(input("Enter the value of G: "))
R = float(input("Enter the value of R: "))
N = float(input("Enter the value of N: "))

# define the dependent variable A

#node1 margin < 30%
if M < 0.3 and G < 0.15 and R < 0.9:
    A = 1.6
elif M < 0.3 and G < 0.15 and R < 0.95:
    A = 1.7
elif M < 0.3 and G < 0.15 and R >= 0.95:
    A = 1.8

elif M < 0.3 and G < 0.5 and R < 0.9:
    A = 1.9
elif M < 0.3 and G < 0.5 and R < 0.95:
    A = 2.0
elif M < 0.3 and G < 0.5 and R >= 0.95:
    A = 2.1

elif M < 0.3 and G >= 0.5 and R < 0.9:
    A = 2.2
elif M < 0.3 and G >= 0.5 and R < 0.95:
    A = 2.3
elif M < 0.3 and G >= 0.5 and R >= 0.95:
    A = 2.4

#node2 margin < 60%
elif M < 0.6 and G < 0.15 and R < 0.9:
    A = 2.0
elif M < 0.6 and G < 0.15 and R < 0.95:
    A = 2.21
elif M < 0.6 and G < 0.15 and R >= 0.95:
    A = 2.42

elif M < 0.6 and G < 0.5 and R < 0.9:
    A = 2.63
elif M < 0.6 and G < 0.5 and R < 0.95:
    A = 2.84
elif M < 0.6 and G < 0.5 and R >= 0.95:
    A = 3.05
    
elif M < 0.6 and G >= 0.5 and R < 0.9:
    A = 3.26
elif M < 0.6 and G >= 0.5 and R < 0.95:
    A = 3.47
elif M < 0.6 and G >= 0.5 and R >= 0.95:
    A = 3.68

#node3 margin >= 60%
elif M >= 0.6 and G < 0.15 and R < 0.9:
    A = 2.84
elif M >= 0.6 and G < 0.15 and R < 0.95:
    A = 3.05
elif M >= 0.6 and G < 0.15 and R >= 0.95:
    A = 3.25

elif M >= 0.6 and G < 0.5 and R < 0.9:
    A = 3.45
elif M >= 0.6 and G < 0.5 and R < 0.95:
    A = 3.75
elif M >= 0.6 and G < 0.5 and R >= 0.95:
    A = 4.1

elif M >= 0.6 and G >= 0.5 and R < 0.9:
    A = 3.05
elif M >= 0.6 and G >= 0.5 and R < 0.95:
    A = 4.55
elif M >= 0.6 and G >= 0.5 and R >= 0.95:
    A = 4.85

# calculate V as V = A*N*12
V = A*N*12

print(V)
