
import  numpy as np
# num_states = 7
# {"0": "C1", "1":"C2", "2":"C3", "3":"Pass", "4":"Pub", "5":"FB", "6":"Sleep"}
i_to_n = {}
i_to_n["0"] = "C1"
i_to_n["1"] = "C2"
i_to_n["2"] = "C3"
i_to_n["3"] = "Pass"
i_to_n["4"] = "Pub"
i_to_n["5"] = "FB"
i_to_n["6"] = "Sleep"

n_to_i = {}
for i, name in zip(i_to_n.keys(), i_to_n.values()):
    n_to_i[name] = int(i)

#   C1   C2   C3  Pass Pub   FB  Sleep
Pss = [
    [0.0, 0.5, 0.0, 0.0, 0.0, 0.5, 0.0],
    [0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.2],
    [0.0, 0.0, 0.0, 0.6, 0.4, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    [0.2, 0.4, 0.4, 0.0, 0.0, 0.0, 0.0],
    [0.1, 0.0, 0.0, 0.0, 0.0, 0.9, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
]
Pss = np.array(Pss)
rewards = [-2, -2, -2, 10, 1, -1, 0]
gamma = 0.5


chains =[
    ["C1", "C2", "C3", "Pass", "Sleep"],
    ["C1", "FB", "FB", "C1", "C2", "Sleep"],
    ["C1", "C2", "C3", "Pub", "C2", "C3", "Pass", "Sleep"],
    ["C1", "FB", "FB", "C1", "C2", "C3", "Pub", "C1", "FB",\
     "FB", "FB", "C1", "C2", "C3", "Pub", "C2", "Sleep"]
]



def compute_return(start_index = 0,
                   chain = None,
                   gamma = 0.5) -> float:
    '''计算一个马尔科夫奖励过程中某状态的收获值
    Args:
        start_index 要计算的状态在链中的位置
        chain 要计算的马尔科夫过程
        gamma 衰减系数
    Returns：
        retrn 收获值
    '''
    retrn, power, gamma = 0.0, 0, gamma
    for i in range(start_index, len(chain)):
        retrn += np.power(gamma, power) * rewards[n_to_i[chain[i]]]
        power += 1
    return retrn



compute_return(0, chains[3], gamma = 0.5)


compute_return(3,chains[3])



def compute_value(Pss, rewards, gamma = 0.05):
    '''通过求解矩阵方程的形式直接计算状态的价值
    Args：
        P 状态转移概率矩阵 shape(7, 7)
        rewards 即时奖励 list
        gamma 衰减系数
    Return
        values 各状态的价值
    '''
    #assert(gamma >= 0 and gamma < 1.0)
    #assert(len(P.shape) == 2 and P.shape[0] == P.shape[1])
    rewards = np.array(rewards).reshape((-1,1))
    values = np.dot(np.linalg.inv(np.eye(7,7) - gamma * Pss), rewards)
    return values

values = compute_value(Pss, rewards, gamma = 0.999999)
print(values)




'''

以上是知道状态序列s，以及转移矩阵p。 以及R回报
'''




'''

以下是马尔可夫决策过程。
'''

from utils import str_key, display_dict
from utils import set_prob, set_reward, get_prob, get_reward
from utils import set_value, set_pi, get_value, get_pi

# 构建学生马尔科夫决策过程
S = ['浏览手机中','第一节课','第二节课','第三节课','休息中']      #   所有状态
A = ['浏览手机','学习','离开浏览','泡吧','退出学习']             #  移动，也就是动作
R = {}                                                      # 奖励Rsa
P = {}                                                      # 状态转移概率Pss'a
gamma = 1.0   # 衰减因子

set_prob(P, S[0], A[0], S[0]) # 浏览手机中 - 浏览手机 -> 浏览手机中
set_prob(P, S[0], A[2], S[1]) # 浏览手机中 - 离开浏览 -> 第一节课
set_prob(P, S[1], A[0], S[0]) # 第一节课 - 浏览手机 -> 浏览手机中
set_prob(P, S[1], A[1], S[2]) # 第一节课 - 学习 -> 第二节课
set_prob(P, S[2], A[1], S[3]) # 第二节课 - 学习 -> 第三节课
set_prob(P, S[2], A[4], S[4]) # 第二节课 - 退出学习 -> 退出休息
set_prob(P, S[3], A[1], S[4]) # 第三节课 - 学习 -> 退出休息

'''

只有泡吧这里有转移概率的说法
'''
set_prob(P, S[3], A[3], S[1], p = 0.2) # 第三节课 - 泡吧 -> 第一节课

set_prob(P, S[3], A[3], S[2], p = 0.4) # 第三节课 - 泡吧 -> 第一节课
set_prob(P, S[3], A[3], S[3], p = 0.4) # 第三节课 - 泡吧 -> 第一节课

set_reward(R, S[0], A[0], -1) # 浏览手机中 - 浏览手机 -> -1    #状态变更就会有奖励
set_reward(R, S[0], A[2],  0) # 浏览手机中 - 离开浏览 -> 0
set_reward(R, S[1], A[0], -1) # 第一节课 - 浏览手机 -> -1
set_reward(R, S[1], A[1], -2) # 第一节课 - 学习 -> -2
set_reward(R, S[2], A[1], -2) # 第二节课 - 学习 -> -2
set_reward(R, S[2], A[4],  0) # 第二节课 - 退出学习 -> 0
set_reward(R, S[3], A[1], 10) # 第三节课 - 学习 -> 10
set_reward(R, S[3], A[3], +1) # 第三节课 - 泡吧 -> -1

MDP = (S, A, R, P, gamma)

#这里我们知道转移概率p，奖励R，各种状态S，y折扣因子，需要计算的是V价值


print("----没有策略时候的状态转移概率字典（矩阵）信息:----")   #十个转移概率
print(display_dict(P))       #从某个状态到某个状态的概率
print("----奖励字典行为奖励（函数）信息:----")    #
print(display_dict(R))     #做某个行为的奖励，


# S = ['浏览手机中','第一节课','第二节课','第三节课','休息中']
# A = ['继续浏览','学习','离开浏览','泡吧','退出学习']
# 设置行为策略：pi(a|.) = 0.5
Pi = {}
set_pi(Pi, S[0], A[0], 0.5) # 浏览手机中 - 浏览手机
set_pi(Pi, S[0], A[2], 0.5) # 浏览手机中 - 离开浏览
set_pi(Pi, S[1], A[0], 0.5) # 第一节课 - 浏览手机
set_pi(Pi, S[1], A[1], 0.5) # 第一节课 - 学习
set_pi(Pi, S[2], A[1], 0.5) # 第二节课 - 学习
set_pi(Pi, S[2], A[4], 0.5) # 第二节课 - 退出学习
set_pi(Pi, S[3], A[1], 0.5) # 第三节课 - 学习
set_pi(Pi, S[3], A[3], 0.5) # 第三节课 - 泡吧

print("----有策略时候的状态转移概率字典（矩阵）信息:----")
display_dict(Pi)
# 初始时价值为空，访问时会返回0
print("----有策略时候的价值函数计算:----")
V = {}

print('')
print(display_dict(V))


def compute_q(MDP, V, s, a):
    '''根据给定的MDP，价值函数V，计算状态行为对s,a的价值qsa
    '''
    S, A, R, P, gamma = MDP
    q_sa = 0

    print('对当前的行为'+str(a)+'计算它的行为价值计算，对行为，计算其对应所有状态的价值')
    for s_prime in S:
        print('状态'+str(s)+'经过a行为，'+str(a)+'获取转移概率'+str(get_prob(P, s, a, s_prime))+'以及分数'+str(get_value(V, s_prime)))
        q_sa += get_prob(P, s, a, s_prime) * get_value(V, s_prime)
        print('状态' + str(s) + '经过a行为，' + str(a) + str(q_sa))
    q_sa = get_reward(R, s, a) + gamma * q_sa

    print('算出这个行为价值为'+str(q_sa))
    return q_sa


def compute_v(MDP, V, Pi, s):
    '''给定MDP下依据某一策略Pi和当前状态价值函数V计算某状态s的价值
    '''
    S, A, R, P, gamma = MDP
    v_s = 0

    print('对当前状态'+str(s)+'，进行一个（找到策略*计算行为价值）的值，不断的加起来。计算某一个状态所有的行为价值，都加起来，')
    for a in A:
        print('-------------------------------')
        print(str(s)+'状态到行为   '+str(a)+'   的策略和相应的q'+str(get_pi(Pi, s, a)))
        print('那么表示是状态'+str(s)+'，经过策略到行为  '+str(a)+'  所计算的行为价值')
        v_s += get_pi(Pi, s, a) * compute_q(MDP, V, s, a)
        print(str(s) + '状态到行为   ' + str(a) + '   的策略计算相应的v-s' +str(v_s))

    print('计算出来的v_s '+str(v_s))
    return v_s


# 根据当前策略使用回溯法来更新状态价值，本章不做要求
def update_V(MDP, V, Pi):
    '''给定一个MDP和一个策略，更新该策略下的价值函数V
    '''
    S, _, _, _, _ = MDP
    V_prime = V.copy()
    print('对所有的状态，计算其V，需要计算状态，有5个状态')
    for s in S:    #对所有状态，
        # set_value(V_prime, s, V_S(MDP, V_prime, Pi, s))
        V_prime[str_key(s)] = compute_v(MDP, V_prime, Pi, s)
    return V_prime


# 策略评估，得到该策略下最终的状态价值。本章不做要求
def policy_evaluate(MDP, V, Pi, n):
    '''使用n次迭代计算来评估一个MDP在给定策略Pi下的状态价值，初始时价值为V
    '''
    for i in range(n):
        V = update_V(MDP, V, Pi)
        # display_dict(V)
    return V



#需要参数MDP，还有Pi（行为策略）比如随机和确定性策略。，我们都是随机的，迭代100次看看


print("MDP初始话，看看"+str(MDP))

  #   所有状态
  #  移动，也就是动作
  # 奖励Rsa
  # 状态转移概率Pss'a



#   策略估计。
V = policy_evaluate(MDP, V, Pi, 1)


display_dict(V)
# 验证状态在某策略下的价值
v = compute_v(MDP, V, Pi, "第三节课")
print("第三节课在当前策略下的价值为:{:.2f}".format(v))
