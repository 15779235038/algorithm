from collections import defaultdict


# from itertools import zip
class Solution:
    '''

 思路：
    1 构建有向图，
    2 找到queries每两个点路径，然后将路径上的值相乘即可

    '''

    def calcEquation(self, equations, values, queries):

        # 一些判断

        # 用邻接表吧

        degree_list = defaultdict(list)
        # 构建这个图出来，然后每两个边之间都有数字，和反向数字。
        for index in range(0, len(equations)):
            degree_list[equations[index][0]].append([equations[index][1], values[index]])
            degree_list[equations[index][1]].append([equations[index][0], 1 / values[index]])

        print(degree_list)

        # 对每一个方程式进行DFS，
        result = []
        visited = defaultdict(int)

        result = []
        for query in queries:
            if query[0] not in degree_list.keys() or query[1] not in degree_list.keys():
                # 图中不存在这些点
                result.append(-1.0)
            elif query[0] == query[1]:
                result.append(1)
            else:

                for k, v in degree_list.items():  # 每两个点之间都要求出来，所以visited每次都要置0。
                    visited[k] = 0
                # self.DFS(degree_list, query[0], query[1], visited,ans)
                temp_ans = []
                # temp_ans.append(query[0])

                print()
                print('开始找把')
                nu_lsit =[]  #记录找到时候的路径。
                self.DFS(degree_list, query[0], query[1], visited, temp_ans,nu_lsit)
                print('结果为'+str(temp_ans))
                if len (temp_ans)==0:
                    result.append(-1.0)
                else:
                    result.append(self.getResult(temp_ans[0], degree_list))
                # result.append(temp_ans)
        return result

    #
    # #构建一个函数，将输入的list输出相乘结果
    # def pairwise(self,iterables):
    #     "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    #     a = iter(iterables)
    #     return zip(a, a)
    #

    # def grouped(iterable, n):
    #     "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    #     return zip(*[iter(iterable)] * n)
    def getResult(self, lists, degree_dict):
        print(lists)
        # print(self.grouped(lists,2))
        temp = [lists[i:i + 2] for i in range(0, len(lists) - 1, 1)]  # 两个两个一组
        print('我们的temp是' + str(temp))
        print('我们的degreelist是' + str(degree_dict))
        divide_result = 1
        for every2 in temp:
            for i in degree_dict[every2[0]]:
                if i[0] == every2[1]:
                    print('输出每次匹配的值' + str(i[0] + str(every2[1])))
                    print(i[0], every2[1])
                    # print('没找到？')
                    divide_result *= i[1]

        return divide_result


#有问题，我们应该用DFS找路径就行了，一路记录下来就ok。找任意两点多条路径。

    '''
    用一个nu_list存储找到结尾点的时走过的路，找到了就存起来。没找到就一起DFS下去。但是记得弹出，表示此路不通。
    '''
    def DFS(self, graph, begin, end, visited, ans,nu_lsit):  # 图  s指的是开始结点
        # visited[begin] = 1
        nu_lsit.append(begin)
        print('每次查看路径'+str(nu_lsit))
        # ans.append(begin)
        if begin == end:
            ans.append(nu_lsit.copy())
            nu_lsit.pop()
            print('找到了，哈啊'+str(ans))
            # ans.append(begin)
        else:
            temp = graph[begin]
            for index in temp:
                     #访问每一个一个后置结点，但是都会弹出。
                    if  index[0] not in nu_lsit:  #只有不在path里面的东西才会继续找下去。
                        print('该点没有被访问'+str(index[0]))
                        self.DFS(graph, index[0], end, visited, ans, nu_lsit)
            nu_lsit.pop()   #找不到该点，一点点回退


# 可以用DFS随便找这个点。

# [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]

values = [3.0,4.0,5.0,6.0]

queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]


test = Solution()
print(test.calcEquation(equations, values, queries))
