import random

# Class for handling clauses
class Clause:
    def __init__(self,p,n):
        self.p = p
        self.n = n
    
    # Function for printing results    
    def __str__(self):
        return "p:(" + str(self.p) + ") and n:(" + str(self.n) + ")"


def resolution(A,B):
    # Check if there is any overlap between (Ap and Bn) and (An and Bp)
    if not A.p.intersection(B.n) and not A.n.intersection(B.p):
        return False

    if A.p.intersection(B.n):
        # Pick random element from the intersection of Ap and Bn
        a = random.choice(list(A.p.intersection(B.n)))
        A.p.remove(a)
        B.n.remove(a)
    else:
        # Pick random element from the intersection of An and Bp
        a = random.choice(list(A.n.intersection(B.p)))
        A.n.remove(a)
        B.p.remove(a)
      
    # Create new clause C as union of A and B
    C = Clause(p = A.p.union(B.p), n = A.n.union(B.n))  
    
    # Check if there is overlap between Cp and Cn
    if C.p.intersection(C.n):
        return False
        
    # C does not contain any duplicates since union was used when creating it which automatically removes duplicates
    # There is also no overlap between Cp and Cn from the check above
    
    return C


def solver(KB):
    
    return KB
  
    
def incorporate(S, KB):
    
    return KB


def incorporate_clause(A, KB):
    
    # If we already have a subset of A in KB: do nothing
    for B in KB:
        # Check if B subsumes A
        if B.p.issubset(A.p) and B.n.issubset(A.n):
            return KB
    
    # If A is a subset of a clause in KB: remove the clause B from KB  
    for B in KB:
        # Check if A subsumes B
        if A.p.issubset(B.p) and A.n.issubset(B.n):
            KB.remove(B)
        
    # Add A to KB    
    KB = KB.union(A)
    
    return KB
            

# ------------------------------------------------------------------------------------------

# Resolution tests

# Test 1
A1 = Clause(p={"a","b"}, n={"c"})
B1 = Clause(p={"c","b"}, n={})

print ("Test 1: ", resolution(A1,B1))

# Test 2
A2 = Clause(p={"a","b"}, n={"c"})
B2 = Clause(p={"d","b"}, n={"g"})

print ("Test 2: ", resolution(A2,B2))

# Test 3
A3 = Clause(p={"c","t"}, n={"b"})
B3 = Clause(p={"z","b"}, n={"c"})

print ("Test 3: ", resolution(A3,B3))