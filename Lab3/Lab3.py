import random
import copy

# Class for handling clauses
class Clause:
    def __init__(self,p,n):
        self.p = p
        self.n = n
    
    # Function for printing results    
    def __str__(self):
        return "p:(" + str(self.p) + ") and n:(" + str(self.n) + ")"
    
    def __hash__(self):
        return hash((frozenset(self.p), frozenset(self.n)))
    
    def __eq__(self, other):
        return self.p == other.p and self.n == other.n


def resolution(A,B):
    
    Ac = copy.deepcopy(A)
    Bc = copy.deepcopy(B)
    
    # Check if there is any overlap between (Ap and Bn) and (An and Bp)
    if not set(Ac.p).intersection(Bc.n) and not set(Ac.n).intersection(Bc.p):
        return False

    if set(Ac.p).intersection(Bc.n):
        # Pick random element from the intersection of Ap and Bn
        a = random.choice(list(A.p.intersection(B.n)))
        Ac.p.remove(a)
        Bc.n.remove(a)
    else:
        # Pick random element from the intersection of An and Bp
        a = random.choice(list(Ac.n.intersection(Bc.p)))
        Ac.n.remove(a)
        Bc.p.remove(a)
      
    # Create new clause C as union of A and B
    C = Clause(p = set(Ac.p).union(Bc.p), n = set(Ac.n).union(Bc.n))  
    
    # Check if there is overlap between Cp and Cn
    if C.p.intersection(C.n):
        return False
        
    # C does not contain any duplicates since union was used when creating it which automatically removes duplicates
    # There is also no overlap between Cp and Cn from the check above
    
    return C


def solver(KB):
    
    while True:
        S = set()
        tempKB = copy.deepcopy(KB)
        
        for A in KB:
            for B in KB:
                if A == B:
                    continue
                
                C = resolution(A,B)
                
                if C:
                    S = S.union(set({C}))
         
        # Check if S is empty       
        if not S:
            return KB

        KB = incorporate(S, KB)
        
        if tempKB == KB:
            return KB
        
    
  
    
def incorporate(S, KB):
    
    # Incorporate all clauses in S
    for A in copy.deepcopy(S):
        KB = incorporate_clause(A, KB)
    
    return KB


def incorporate_clause(A, KB):
    
    # If we already have a subset of A in KB: do nothing
    for B in copy.deepcopy(KB):
        # Check if B subsumes A
        if set(B.p).issubset(A.p) and set(B.n).issubset(A.n):
            return KB
    
    # If A is a subset of a clause in KB: remove the clause B from KB  
    for B in copy.deepcopy(KB):
        # Check if A subsumes B
        if set(A.p).issubset(B.p) and set(A.n).issubset(B.n):
            KB.remove(B)
        
    # Add A to KB    
    KB = KB.union(set({A}))
    
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


# Bob test

A = Clause(p={"ice"}, n={"sun","money"})
B = Clause(p={"ice","movie"}, n={"money"})
C = Clause(p={"money"}, n={"movie"})
D = Clause(p={}, n={"movie","ice"})
E = Clause(p={"movie"}, n={})
F = Clause(p={"sun","money","cry"}, n={})


KB = set({A,C,D,E,F})

result = solver(KB)
print ("Test Bob: ")

for i in result:
    print(i)