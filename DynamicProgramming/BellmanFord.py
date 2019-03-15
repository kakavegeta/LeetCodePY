'''
Graph: dict
Graph method:
    G[u][v]: weight of edge (u, v)
'''
#Relaxation
def BellmanFord(G, s):
    d, p = initialize(G, s)
    k = count_edge(G)
    print(k)
    for _ in range(k-1):
        pre_d, pre_p = d, p
        for u in G:
            for v in G[u]:
                relax(u, v, G, d, p)
        # if d, p no longer change, then just break out
        print(pre_d,d)
        print(pre_p, p)
        #if pre_d==d and pre_p==p:
        #    break
                
    #check negative-weight cycle
    for u in G:
        for v in G[u]:
            if d[v] > d[u] + G[u][v]:
                print(u,v)
                return None, None
    return p, d


def count_edge(G):
    count = 0
    for v in G:
        count+=len(G[v])
    return count


def initialize(G, s):
    '''
    d: distance
    p: predecessor
    '''
    d, p = {}, {}
    for node in G:
        d[node] = float("inf")
        p[node] = None
    d[s] = 0
    return d, p

def relax(u, v, G, d, p):
    '''
    u, v: node in G
    it aims to relax node v
    '''
    if d[v] > d[u] + G[u][v]:
        d[v] = d[u] + G[u][v]
        p[v] = u




def test():
    G ={'s':{'t':6, 'y':7},
        't':{'x':5, 'z':-4, 'y':8},
        'x':{'t':-2},
        'z':{'x':7, 's':2},
        'y':{'x':-3, 'z':9}}
    p, d = BellmanFord(G, 's')
    print(p, d)

if __name__ == "__main__":
    test()

