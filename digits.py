
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

digits = datasets.load_digits()
df = pd.DataFrame(digits.data, columns=digits.feature_names)
df['target'] = digits.target
print(df.head())

# Display the last digit
# plt.figure(1, figsize=(3, 3))
# plt.imshow(digits.images[3], cmap=plt.cm.gray_r, interpolation="nearest")
# plt.show()
x_train,x_test,y_train,y_test = train_test_split(digits.data,digits.target,test_size=0.2)
# sc = StandardScaler()
# x_train = sc.fit_transform(x_test)
# x_test = sc.transform(x_test)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
print(accuracy)

plt.figure(figsize=(12,4))

for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(x_test[i].reshape(8,8),cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title(f"Прогноз : {y_pred[i]}\nВідповідь:{y_test[i]}")
    plt.axis("off")
plt.show()