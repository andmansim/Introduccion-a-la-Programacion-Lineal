#importamos la herramienta a usar
from ortools.linear_solver import pywraplp

#Creamos el solucionador del problema en cuestión
solucionador = pywraplp.Solver("Maximizar la fuerza de los guerreros", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#variables a optimizar
espadachines = solucionador .IntVar(0, solucionador .infinity(),"espadachines")
jinetes = solucionador .IntVar(0, solucionador .infinity(),"jinetes")
arqueros = solucionador .IntVar(0, solucionador .infinity(),"arqueros")                        

#Restricciones de las variables
solucionador .Add(60*espadachines + 80* arqueros + 140* jinetes <= 1200)
solucionador .Add(20*espadachines + 10* arqueros + 0* jinetes <= 800)
solucionador .Add(0*espadachines + 40* arqueros + 100* jinetes <= 600)

#Función para maximizar
solucionador .Maximize(70*espadachines + 95*arqueros + 230*jinetes)

#Optimizamos el código
estado = solucionador.Solve()

if estado == pywraplp.Solver.OPTIMAL:
    print("********************************************************")
    print(f'Resuelto en {solucionador.wall_time():.2f} milisegundos en {solucionador.iterations()} iteraciones')
    print(f'Hemos optenido {solucionador.Objective().Value()} poder')
    print(f'Espadachines = {espadachines.solution_value()}')
    print(f'Arqueros = {arqueros.solution_value()}')
    print(f'Jinetes = {jinetes.solution_value()}')

