
#定义一个图的结构
graph={
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E','F'],
    'E':['C','D'],
    'F':['D']
}

'''
利用DFS以及回溯法，每次走到一个节点并且该节点没有返回路径，就逆序加入结果中。每访问一个边就删除

'''

from  collections  import  defaultdict
def  first(tickets):
    #构建graph的邻接链表
    neighbor_dict = defaultdict(list)
    for edge in tickets:
        neighbor_dict[edge[0]].append(edge[1])
    print(neighbor_dict)

    #对节点排序
    for k , v in neighbor_dict.items():
        neighbor_dict[k]= sorted(neighbor_dict[k])
    print(neighbor_dict)


    ans = []
    DFS(neighbor_dict,'JFK',ans)
    return ans




def DFS(graph, s,ans):  # 图  s指的是开始结点
    temp = graph[s]
    print('查看temp'+str(temp))
    while len(temp) > 0:
        #从邻接链表弹出
        visited_node = temp.pop(0)
        DFS(graph, visited_node, ans)
    ans.insert(0,s)







data =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(first(data))
