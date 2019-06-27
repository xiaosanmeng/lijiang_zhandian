import pandas as pd
from tqdm import tqdm
import time

def get_unique_name_list(dataframe):
    name_list = list()
    for row in dataframe.iterrows():
        name = row[1]['name']
        name_list.append(name)
    # 去重
    unique_name_list = sorted(set(name_list), key=name_list.index)
    return unique_name_list


def data_process(dataframe):
    unique_name_list = get_unique_name_list(dataframe)
    new_id_list = list()
    new_line_name_list = list()

    for row in tqdm(dataframe.iterrows()):
        # 获取新id
        time.sleep(1)
        name = row[1]['name']
        new_id = unique_name_list.index(name)
        new_id_list.append(new_id)

        # 获取新lineName
        old_line_name = row[1]['lineName']
        new_line_name = old_line_name.split('路')[0]
        new_line_name_list.append(new_line_name)

    # 添加两列新的
    dataframe['new_id'] = new_id_list
    dataframe['new_line_name'] = new_line_name_list

    dataframe.to_csv('new.csv', index=False)


if __name__ == '__main__':
    df = pd.read_csv('丽江站点.csv')
    data_process(df)
