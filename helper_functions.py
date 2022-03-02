def mu(edge, relations):
    if edge in relations:
        return 1
    else:
        return 0


def computeCS(G1, G2, relationsG1, relationsG2):
    totalSumMu = 0
    globalSize = min(len(G1), len(G2))
    for i in relationsG1:
        totalSumMu += mu(i, relationsG2)
    vMin = min(len(G1), len(G2))
    return totalSumMu/vMin


def commonNodes(G1, G2):
    percentages = []
    total = 0
    for i in G1:
        total = 0
        for k in G2:
            if i == k:
                total += 1
            else:
                total += 0
        percentages.append(total/len(G2))
 
    return percentages
    

def commonNode(node_lists, graph_class_list):
    belongs_list = []
    for i in node_lists:
        if i in graph_class_list:
            belongs_list.append(1)
            
        else:
            
            belongs_list.append(0)
            
    return belongs_list


def commonEdges(relationsG1, relationsG2):
    percentages = []
    total = 0
    for i in relationsG1:
        total = 0
        for k in relationsG2:
            if str(i) == str(k):
                total += 1
            else:
                total += 0
        percentages.append(total/len(relationsG2))
 
    return percentages


def MCS(G1, G2): #Maximum Common Subgraph
    return commonNodes(G1, G2)/min(len(G1), len(G2))


def MCSUES(G1, G2): #Total number of edges contained in the MCS
    return commonEdges(G1, G2)/min(len(G1), len(G2))


def percentageOfNode(node, listOfNodes):
    percentage = 0
    for i in listOfNodes:
        
        if i == node:
            percentage += percentage
    return percentage/len(listOfNodes)

    