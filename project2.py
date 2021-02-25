from csp import CSP
from backtracking import backtracking_search

# read in graph from input file
f = input("file name: ")
with open(f, 'r') as file:
    line = file.readline()
    
    # Everything that starts with # is a comment
    while line.startswith('#'):
        line = file.readline()
        
    # First non comment line is of form Colors = n
    num_colors = int(line[9])
    domain = [i for i in range(1, num_colors+1)]
    
    # Read graph into CSP
    colors = CSP()
    line = file.readline()
    while line:
        if line.startswith('#'):    # skip comments
            line = file.readline()
            continue
        if len(line) == 0: break    # EOF
        
        # Add constraints (edges)
        edge = line.strip().split(',')
        colors.add_constraint(edge[0], edge[1], domain)
        
        line = file.readline()
        
# solve CSP
solution = backtracking_search(colors)
if solution == None:
    print('Failure')
else:
    for key in solution.keys():
        print(str(key) + " -> color " + str(solution[key]))