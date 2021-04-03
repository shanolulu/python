import pandas as pd

member_list = {
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG']
}

transaction_list = {
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]
}

member_df = pd.DataFrame(member_list, columns=['고객번호', '이름'])
member_df = member_df.drop([0,3])
print(member_df)
member_df = member_df.reset_index(drop=True)
print(member_df)
transaction_df = pd.DataFrame(transaction_list, columns=['고객번호', '금액'])
print(transaction_df)

inner_result = pd.merge(member_df, transaction_df)
print(inner_result)
print("-------------")
outer_result = pd.merge(member_df, transaction_df, how='outer')
print(outer_result)
