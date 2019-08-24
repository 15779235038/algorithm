

#冗余连接

'''
1  思路
遍历边，如果有边构成了环。删除这条边，就是答案。按照顺序放入，返回倒数第一个。


先在图中删除这条边，然后这个边有两个点。如果从某个点出发，能够走到另一个点。就是答案。


'''

from  collections import  *
import  copy
class Solution:
    def findRedundantConnection(self, edges):

        degree_list = defaultdict(list)
        #邻接表,构造邻接表。
        for edge in edges:
            degree_list[edge[0]].append(edge[1])
            degree_list[edge[1]].append(edge[0])
        result = []
        temp = None
        #遍历每一条边。
        for edge in edges:
             #在邻接表中删除该边。
             temp = copy.deepcopy(degree_list)
             temp[edge[0]].remove(edge[1])
             temp[edge[1]].remove(edge[0])
             # print('移除后的图是'+str(temp))
             #从某个点出发看是否有路径。
             path = []
             ans = []
             self.DFS(edge[0],edge[1],temp,path,ans)
             # print('看下path'+str(path))
             if len(ans) > 1 or len(ans) == 1:
                 # print('添加进去啊')
                 result.append(edge)
        # print('结果为'+str(result))
        if len(result) > 1:
            return result[-1]
        else:
            return result[0]



    def  DFS(self,begin, end,graph,nu_list,ans):
        # visited[begin] = 1
        nu_list.append(begin)
        # print('每次查看路径' + str(nu_list))
        # ans.append(begin)
        if begin == end:
            ans.append(nu_list.copy())
            # flag = 1
            # print('可以到那个点'+str(begin))
            nu_list.pop()
        else:
            temp = graph[begin]
            for index in temp:
                # 访问每一个一个后置结点，但是都会弹出。
                if index not in nu_list:  # 只有不在path里面的东西才会继续找下去。
                    # print('该点没有被访问' + str(index[0]))
                    self.DFS(index,end,graph,nu_list,ans)
            nu_list.pop()  # 找不到该点，一点点回退







class Solution1:
    def findRedundantConnection(self, edges):
        p = [*range(len(edges) + 1)]      #并查集元素初始化
        print('p是多少'+str(p))

        #更新数组
        def f(x):
            if p[x] != x:       #递归修改所属集合
                p[x] = f(p[x])
            return p[x]


        for x, y in edges:      #遍历边
            print(x,y)
            px, py = f(x), f(y) #让它们两做朋友，就是找两个兄弟。
            print(' #寻找两者上级')
            print(px,py)
            if px != py:        #检查集合，如果集合不同就合并
                #px做了py的上级。
                p[py] = px

            else:
                print('掌门一样的，就是px和py有共同的出发节点')
                return [x, y]   #集合相同就返回答案






test = Solution1()
print(test.findRedundantConnection([[1,2], [1,3], [2,3]]))