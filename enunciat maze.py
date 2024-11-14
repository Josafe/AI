import time
import pyamaze as maze
from queue import PriorityQueue

# Que es pymaze?
# Com esta estructurat maze.maze.keys
# PriorityQueue

#dir = [{1,1}], {"E":1,"S":0}
#dir_punt_actual = [{1,3}], [{"S"}]
#---------------------------------------------------
#Prova priorityQueue funcional
#prioritat = PriorityQueue()
#prioritat.put(3, "Prova3")
#prioritat.put(1, "Prova1")
#prioritat.put(2, "Prova2")

#while prioritat:
#    print(prioritat.get())
#---------------------------------------------------


def distancia(cell1, cell2):
    return abs(cell1[0]- cell2[0]) + abs(cell1[1] - cell2[1])
    
def aStar(m):
    start = m.rows, m.cols #Principi del mapa "tamany del tauler"
    goal = (1,1) #Final del mapa
    pq = PriorityQueue()
    pq.put(start, distancia(start, goal)) #Li passem el inici i el final per a que ho guarde a la llista 
    cami = {} #Tots els camins possibles
    cost = {cell:float("inf") for cell in m.grid}
    cost[start] = 0 #Vols cambiar el start que es 20,20
    #print(m.grid) #Printeja les coordenades

    while not pq.empty():
        
        current_cell = pq.get() #Et recull el que esta mes prop per direccio del final "heuristica"
        
        if current_cell == goal:
            cami_eficient = {}

            while current_cell in cami:
                cami_eficient[cami[current_cell]] = current_cell
                current_cell = cami[current_cell]
            
            print(cami_eficient)
            return cami_eficient
        
        #print(m.maze_map)

        for direccio in 'NSEW':
            if m.maze_map[current_cell][direccio] == 1:
                
                if direccio == 'N':
                   next_cell = (current_cell[0]-1, current_cell[1])
                   
                if direccio == 'S':
                   next_cell = (current_cell[0]+1, current_cell[1])

                if direccio == 'E':
                   next_cell = (current_cell[0], current_cell[1]+1)
                  
                if direccio == 'W':
                   next_cell = (current_cell[0], current_cell[1]-1)

                contador_t = cost[current_cell]+1
            
                if contador_t < cost[next_cell]:
                    cami[next_cell] = current_cell
                    cost[next_cell] = contador_t #El substituim per el de la next_cell per a que es vaigue fent mes petit fins arribar al minim
                    pq.put(next_cell, contador_t + distancia(next_cell, goal)) #Distancia ja recorreguda + distancia per recorrer hasta el final per al calcul heuristic

    return {}
                
                   #pq.put(next_cell)
                   #print("S'ha anat en direccio W" + str(next_cell))
                
                
            
            

        #a=maze.agent(m,footprints=True)
        
                
#cami = aStar(maze, start, goal)
#distance(m.rows, m.cols)

ROWS = 50
COLS = 50
m = maze.maze(ROWS,COLS)
m.CreateMaze() #Crear laberinto
pre_Astar = time.time()
path = aStar(m)
post_Astar = time.time()
print(post_Astar - pre_Astar)
a = maze.agent(m, footprints = True)
m.tracePath({a:path},delay=50) 
m.run()