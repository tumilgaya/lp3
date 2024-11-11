
import numpy as np
import pandas as pd

df = pd.read_csv('diabetes.csv')

df.head()

zero_not_accepted = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin']

for i in zero_not_accepted:
    df[i] = df[i].replace(0,np.NaN)
    mean = int(df[i].mean(skipna=True))
    df[i] =df[i].replace(np.NaN,mean)

df.head()

x = df.iloc[ : , :-1]
y = df.iloc[ : , -1]

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x = sc.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=10)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(y_test,y_pred)

