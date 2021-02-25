# Class for Conststaint Satisfaction Problems
# Built for graph coloring problem but could easily be modified
# to be used with other problems
class CSP:
    def __init__(self):
        self.variables = []
        self.constraints = {} # dictionary of variable: neighbors
        self.domains = {}     # dictionary of variable: domains
        
    # assumes binary constraints
    def add_constraint(self, v1, v2, domain=None):
        if v1 not in self.variables:
            self.variables.append(v1)
            self.constraints[v1] = [v2]
            self.domains[v1] = domain
        else:
            self.constraints[v1].append(v2)
            
        if v2 not in self.variables:
            self.variables.append(v2)
            self.constraints[v2] = [v1]
            self.domains[v2] = domain
        else:
            self.constraints[v2].append(v1)

    
    # Check consistency i.e. check that no nieghbors have already
    # been assigned the same value
    # Returns True if consistent
    def consistent(self, var, value, assignment):
        for n in self.constraints[var]:
            if n in assignment and assignment[n] == value:
                return False
        return True
    
    

