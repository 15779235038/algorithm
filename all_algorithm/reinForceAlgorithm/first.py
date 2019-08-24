import numpy as np

# num_states = 7
# {"0": "C1", "1":"C2", "2":"C3", "3":"Pass", "4":"Pub", "5":"FB", "6":"Sleep"}
i_to_n = {}
i_to_n["0"] = "0"
i_to_n["1"] = "14"
i_to_n["2"] = "15"
i_to_n["3"] = "16"
i_to_n["4"] = "17"

n_to_i = {}
for i, name in zip(i_to_n.keys(), i_to_n.values()):
    n_to_i[name] = int(i)

#   0 ,14,15, 16,17
Pss = [
    [0.657847, 0.022, 0.077815, 0.258, 0.033],
    [0.622397835963354, 0.377602164036646, 0.0, 0.0, 0],
    [0.50299500098446, 0, 0.497004999015537, 0.0, 0.0, ],
    [0.361175033079268, 0, 0, 0.638824966920732, 0.0, ],
    [0.222613558766387, 0, 0, 0, 0.777386441233613],
]



Pss = np.array(Pss)
rewards = [0, 15.3556, 19.7641, 24.4194, 28.8609]  # 每个状态的rewards
gamma = 0.9


def compute_return(start_index=0,
                   chain=None,
                   gamma=0.5) -> float:
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


def compute_value(Pss, rewards, gamma=0.05):
    '''通过求解矩阵方程的形式直接计算状态的价值
    Args：
        P 状态转移概率矩阵 shape(7, 7)
        rewards 即时奖励 list
        gamma 衰减系数
    Return
        values 各状态的价值
    '''
    # assert(gamma >= 0 and gamma < 1.0)
    # assert(len(P.shape) == 2 and P.shape[0] == P.shape[1])
    rewards = np.array(rewards).reshape((-1, 1))
    values = np.dot(np.linalg.inv(np.eye(5, 5) - gamma * Pss), rewards)
    return values


values = compute_value(Pss, rewards, gamma=0.95)
print(values)



'''
以上是知道状态序列s，以及转移矩阵p。 以及R回报
'''
