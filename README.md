https://github.com/HollyCorbin/AI_project2.git

Run project2.py. It will ask for the name of an input file. Input the name of the file you want to use and then the program will run the search. 
It will output the solution as a list of vertex -> color.

The program uses backtracking search to assign each vertex to a color. It uses the minimum remaining values heuristic for choosing the order of vertices traversed and the least constraining value heuristic to choose the colors. It then assigns a color to the vertex and runs AC3 to enforce arc consistency by removing colors from the domains of other vertices.  
