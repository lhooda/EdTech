#from src.data_collection.collect_oulad import load_oulad_dataset

#datasets = load_oulad_dataset()

#for name, df in datasets.items():
#    print(name, df.shape)




# # # from src.data_collection.collect_oulad import load_oulad_dataset
# from src.data_preprocessing.clean_oulad import preprocess_oulad

# datasets = load_oulad_dataset()
# df = preprocess_oulad(datasets)

# print(df.head())
# print(df.shape)

# # # 

import pandas as pd
pd.set_option('display.max_columns', None)

from src.data_collection.collect_oulad import load_oulad_dataset
from src.data_preprocessing.clean_oulad import preprocess_oulad

datasets = load_oulad_dataset()
df = preprocess_oulad(datasets)

print(df.head())
print(df.shape)
