import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 32, 18, 47],
        'country': ['USA', 'Canada', 'UK', 'USA']}
df = pd.DataFrame(data)
print(df)