import panda as pd
import csv
data_frame=[["name","age","gender"],
           ["alice",25,"female"],
           ["bob",30,"male"],
           ["clair",30,"female"]]
with open("df.csv","w") as f:
    write=csv.writer(f)
    for i in data_frame:
        write.writerow(i)
data=pd.read_csv("df.csv")
print(data)