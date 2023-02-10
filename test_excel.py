import pandas
import pprint
from collections import defaultdict

def excel_to_dict_wines(template)->defaultdict:
    excel_data_df=pandas.read_excel(template,keep_default_na=False,na_values='',na_filter=False)
    list_to=excel_data_df.to_dict(orient="records",)
    dict_out=defaultdict(list)
    for dict_drink in list_to:
        dict_out[dict_drink["Категория"]].append(dict_drink)
    return dict_out
a=excel_to_dict_wines("wine3.xlsx")
for k,v in a.items():
    print(k,v)
    
    


