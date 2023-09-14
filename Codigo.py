#importamos la herramienta a usar
from ortools.linear_solver import pywraplp

#Creamos el solucionador del problema en cuestión
solucionador = pywraplp.Solver("Maximizar la fuerza de los guerreros", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#variables a optimizar
espadachines = solver.IntVar(0, solver.infinity(),"espadachines")
jinetes = solver.IntVar(0, solver.infinity(),"jinetes")
arqueros = solver.IntVar(0, solver.infinity(),"arqueros")                        

#Restricciones de las variables
solver.Add(60*espadachines + 80* arqueros + 140* jinetes <= 1200)
solver.Add(20*espadachines + 10* arqueros + 0* jinetes <= 800)
solver.Add(0*espadachines + 40* arqueros + 100* jinetes <= 600)



