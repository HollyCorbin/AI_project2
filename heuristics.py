# select variable with MRV heuristic
def select_var(csp, assignment):
    vars = {} #  dictionary of var : # of constraints
    for var in csp.variables:
        if var not in assignment:
            # num constraints = num neighbors in constraint graph
            vars[var] = len(csp.constraints[var])
            
    # order variables by decreasing # of costraints to break ties
    vars = sorted(vars, key=vars.get, reverse=True)
        
    # select variable with minimum remaining values in domain
    min_var = vars[0]
    for var in vars:
        if len(csp.domains[var]) < len(csp.domains[min_var]):
            min_var = var
    return min_var


# order choice of values based on least constraining value
def order_values(csp, var):
    order = {} #  dictionary of value : # of constraints
    
    # for each value check if it constrains other variables
    for value in csp.domains[var]:
        num_constraining = 0
        for neighbor in csp.constraints[var]:
            # if value is in neighbor's domain, will add constraint
            if value in csp.domains[neighbor]:
                num_constraining += 1
        order[value] = num_constraining
        
    return sorted(order, key=order.get)


# AC3 modifies all domains for arc consistency
def AC3(csp):
    # get queue of arcs in graph from neighbors dictionary
    # every conststraint is represented twice
    # beacuse arcs are bidirectional in this problem
    queue = []
    for var in csp.variables:
        for neighbor in csp.constraints[var]:
            queue.append((var, neighbor))
            
    while queue:
        (v1, v2) = queue.pop(0)
        if remove_inconsistent(csp, v1, v2):
            # constraint propogation
            for neighbor in csp.constraints[v1]:
                queue.append((neighbor, v1))
               
# returns True if inconsistent values were removed from domain
def remove_inconsistent(csp, v1, v2):
    removed = False
    for x in csp.domains[v1]:
        v2_domain = csp.domains[v2]
        # value is inconsistent if it is equal to the only
        # value in domain of v2
        if len(v2_domain) == 1 and v2_domain[0] == x:
            domain = []
            for i in csp.domains[v1]:
                if i != x: domain.append(i)
            csp.domains[v1] = domain
            removed = True            
    return removed
