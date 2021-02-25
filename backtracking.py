from heuristics import select_var, order_values, AC3
from copy import deepcopy

# Returns solution as assignment dictionary
def backtracking_search(csp):
    return backtrack(csp, {})

def backtrack(csp, assignment):
    if len(assignment) == len(csp.variables):
        return assignment
    
    var = select_var(csp, assignment)
    for value in order_values(csp, var):
        if csp.consistent(var, value, assignment):
            assignment[var] = value
            
            # make copy of csp so that domains of original are
            # not changed by AC3 if backtracking happens
            csp_copy = deepcopy(csp)
            csp_copy.domains[var] = [value]
            AC3(csp_copy) # enforces arc consistency
            
            result = backtrack(csp_copy, assignment)
            if result:
                return result
            
            #if no solution with var = value, remove and backtrack
            assignment.pop(var)
    return None

