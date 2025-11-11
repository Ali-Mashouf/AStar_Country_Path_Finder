from queue import PriorityQueue 
# saf olaviat, anasor ra olaviat bandi mikonad 
graph = {
    'Iran': [('Russia', 2), ('China', 7), ('Turkey', 2)],
    'Russia': [('China', 4)],
    'China': [('Russia', 4), ('Turkey', 3), ('Italy', 5)],
    'Turkey': [('Italy', 5)],
    'Italy': [('Spain', 5), ('France', 8)],
    'Spain': [('France', 8), ('Italy', 5), ('Brazil', 10)],
    'France': [('Spain', 8), ('England', 6), ('USA', 15)],
    'England': [('France', 6), ('USA', 12)],
    'Brazil': [('Spain', 10), ('Argentina', 10)],
    'USA': [('Canada', 7), ('England', 12)],
    'Canada': [('USA', 7)],
    'Argentina': [('Brazil', 10)]
}
# takhmin baraye residan be har gere 
heuristic = {
    'Iran'     : 0,
    'Russia'   : 3,
    'China'    : 8,
    'Turkey'   : 4,
    'Italy'    : 8,
    'Spain'    :14,
    'France'   :17,
    'England'  :22,
    'Brazil'   :25,
    'USA'      :29,
    'Canada'   :35,
    'Argentina':35
}


def A_star(graph, heuristic, start, goal): #def func()
    
    saf_olaviat = PriorityQueue() #baraye inke anasor ro ba kamtarin hazine olaviat bandi kone 
    saf_olaviat.put((0, start))   #put() baraye taein olaviat bar asase cost
    
    W_node = {}          #masire bazgashti
    S_cost = {start: 0}  #hazine residan be har node
    
    while not saf_olaviat.empty():   #pardazesh 
        _, node = saf_olaviat.get()  #onsore dovom baraye ma mohem hast(node)
       
        if node == goal:                 #agar ke goal peyda shod 
            path = []                    #baraye zakhire sazi masir az start ta goal
            while node is not None:      #bazsazie masir
                path.append(node)        #gereye hal hazer ro dar path gharar mide
                node = W_node.get(node)  #gereye ghablio migire va dar node mizare
            #return path, S_cost[goal]
            return path[::-1], S_cost[goal] #hazineye nahae va tartibe doroste search  

        for neighbor, cost in graph[node]:                            #hamsaye ha va hazinashon
            new_cost = S_cost[node] + cost                            #hazineye lazem baraye residan be node
            if neighbor not in S_cost or new_cost < S_cost[neighbor]: #agar ke node dide nashode bashe ya hazine bedast amade kamtar az ghabl bashe 
                S_cost[neighbor] = new_cost                           #update hazine
                olaviat = new_cost + heuristic[neighbor]              #olaviat bar asase cost va heuristic
                saf_olaviat.put((olaviat, neighbor))                  #gharar dadan dar safe olaviat
                W_node[neighbor] = node     
    
    return None, None    #agar ke goal peyda nashe 

start = 'Iran'
goal = input('keshvare morede nazar ra az graph entekhab konid :\n')
path, cost = A_star(graph, heuristic, start, goal)

if path:   #agar goal peyd shavad
    print(" masire tey shode :", path)
    print("hazineye koli :", cost)
else:     #agar ke tabe None bargardone
    print("keshvare {} peyda nashod ".format(goal))
