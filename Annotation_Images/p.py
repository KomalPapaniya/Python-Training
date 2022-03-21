import pandas as pd
df = pd.read_csv("C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\Annotation_Images\\lable_part_3.csv")
df1 = pd.DataFrame(df)
print(df1)
df1 = df1.dropna(axis=0, subset=['Names'])
print(df1.sample(10))
df1.to_csv(r'C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\Annotation_Images\\lable_3.csv', index = False)