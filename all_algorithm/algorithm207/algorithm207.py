


from collections import defaultdict,OrderedDict

#课程表，解法1，通过拓扑排序，代码能力太差了
def class_table(numCourses, prerequisites ):
    if len(prerequisites) == 0:    #边为0，肯定可以拓扑的。
        return  1
    #收集拓扑序列

    # Topological_list = []
    #实现队列
    queue = [None] * numCourses   #队列可以无限大。
    front = 0
    rear = 0
      #关于存储num_list 这是图中所有结点的list
   #寻找所有入度为0的点
    dict_degree = defaultdict(int)
    for i in prerequisites:
        #记录某个元素的入度
        dict_degree[i[0]] += 0
        dict_degree[i[1]] += 1
    #print(' #计算所有结点的入度，')
    #print(dict_degree)
    num_list = []
    for k in dict_degree.keys():
        num_list.append(k)
        if dict_degree[k] == 0:   #入度为0，将其放入队列中
            #print(rear)
            queue[rear] = k
            rear += 1
            dict_degree[k] = -99  #相当于删除了
    #print('看下最开始队列是多少')
    #print(queue)

    if len(queue) == 0: #第一个找不到度为0的点，ok搞定。
        return 0
    while front != rear  :  #队列不为空，取出第一个
        temp = queue[front] #取出第一个，对其所指向的结点删除边，也就是lists要删除从这个点出发的边了。
        queue[front] = None  #队列该位置置空。
        # Topological_list.append(temp) #收集从队列取出的元素，就是拓扑序列
        front += 1
        #print('取出元素的queue是多少'+str(queue))
        num_list.remove(temp)
        #print('取出点的图还有什么？'+str(num_list))
        #print('   取出第一个temp'+str(temp))
        # temp_list =   #找到它的邻居结点，看看会不会因为这一步而入度为0
        # #print('找到temp邻居结点，'+str(temp_list))
        for j in [x for x in prerequisites if temp == x[0]]:
            dict_degree[j[1]] -= 1 #将该邻居结点的入度-1
            if dict_degree[j[1]] == 0:   #如果减完后变成0了，然后就把加入队列中。
                #print('加入到队列中' + str(j[1]))
                queue[rear] = j[1]
                rear += 1
                dict_degree[j[1]] = -99  # 相当于删去该结点了。
        #print('添加完的队列是'+str(queue))
        #print('再次找到的dict_degree'+str(dict_degree))
        if len(num_list) == 0 and front == rear:  #图中没有点，并且队列走完了。
            return    1  #返回拓扑序列

    if len(num_list) != 0:
        #print('图里面还有点')
        return 0


            # #print('图没点了')
            # flag = 1


        #当队列走完，并且原图没有结点了。











