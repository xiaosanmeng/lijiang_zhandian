import pandas as pd
import json
from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt


def get_line_info():
    df = pd.read_csv('01丽江拓扑.csv')
    result_dict = dict()
    for index, row in df.iterrows():
        new_line_name = str(row['new_line_name'])
        if new_line_name not in result_dict.keys():
            result_dict[new_line_name] = list()

        # 在数据中9路外环和9路内环相接的地方会连着添加两个1
        # 从而引入（1，1）这条没必要存在的边
        # 下面两行代码对这种情况进行过滤
        # 我们判断要添加进列表的数字如果和当前列表中最后一个，则跳过
        if len(result_dict[new_line_name]) > 0 and result_dict[new_line_name][-1] == row['new_id']:
            continue
        result_dict[new_line_name].append(row['new_id'])
    print(len(result_dict))
    print(result_dict.keys())
    return result_dict


def get_l_graph(result_dict):
    graph = nx.Graph()
    for key, value in result_dict.items():
        graph.add_path(value)
    return graph


def get_p_graph(result_dict):
    graph = nx.Graph()
    for key, value in result_dict.items():
        edges = combinations(value, 2)
        graph.add_edges_from(edges)
    return graph


if __name__ == '__main__':
    r_dict = get_line_info()
    l_graph = get_l_graph(r_dict)
    p_graph = get_p_graph(r_dict)

    nx.draw(l_graph)
    plt.show()

    l_matrix = nx.to_pandas_adjacency(l_graph)
    l_matrix.to_csv('L_matrix.csv', index=False)
    # print(len(l_graph.edges))
    # print(len(p_graph.edges))
    p_matrix = nx.to_pandas_adjacency(p_graph)
    p_matrix.to_csv('P_matrix.csv', index=False)


