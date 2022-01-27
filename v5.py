import os
import glob
import pandas as pd
import re
import statistics
from collections import Counter
current_dir=os.path.dirname(os.path.abspath(__file__))
path = 'test_video.txt'
df = pd.read_csv(os.path.join(current_dir, path), header=None, delim_whitespace=True)
df = df.iloc[:,1:7]
#列名を追加
df.columns=["trackid","class", "xmin", "ymax","w","h"]
#class別集計
df = df[["trackid","class"]]
df = (df.groupby('trackid')['class']
          .apply(list)
          .apply(lambda x:sorted(x))
         ).reset_index()
df.colums = ["trackid","class"]
from collections import Counter
df['class']=df['class'].apply(lambda x: Counter(x).most_common(1)[0][0])
vc = df['class'].value_counts()
print(vc)
