# Q7. Create a DataFrame using multiple Series. Explain with an example.
import panda as pd
Name=pd.Series(["deepak","dilip","vicky"])
age=pd.Series([24,23,25])
sallary=pd.Series([23000,2300,1200])
df=pd.DataFrame({"names":Name,"age":age,"sallary":sallary})
df