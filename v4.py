#YOLOv4-DeepSORT用
import os
import glob
import pandas as pd
import re
import statistics
current_dir=os.path.dirname(os.path.abspath(__file__))
path = 'test_info.txt'
df = pd.read_csv(os.path.join(current_dir, path), header=None)
#列名を追加
df.columns=["trackid","class", "xmin", "ymin","xmax","ymax"]
#class別集計
df = df[["trackid","class"]]
df = (df.groupby('trackid')['class']
          .apply(list)
          .apply(lambda x:sorted(x))
         ).reset_index()
df.colums = ["trackid","class"]
df.to_csv(os.path.join(current_dir,'test_info.csv'),encoding='utf_8',index=False)
df['class']=df['class'].apply(statistics.mode)
vc = df['class'].value_counts()
print(vc)
