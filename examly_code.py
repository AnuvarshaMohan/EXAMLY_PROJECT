# import pandas
import pandas as pd

# read the dataset
df = pd.read_csv('/dataset_examly_2.csv', error_bad_lines=False) # uploading and path of the file

df.head() # returns the first five rows of the dataframe

print(df.shape)

num_of_classes = len(df.Difficulty.unique())
print(num_of_classes)

df.describe()

# split train input and output data
X = df.drop(axis=0, columns=['Difficulty']) #Eliminating Difficulty column and storing the else in input variable
Y = df.Difficulty #Having only the Difficulty column in the output variable

#Print the shape of X and Y
print(X.shape)
print(Y.shape)

from sklearn.model_selection import train_test_split

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# training a DescisionTreeClassifier 
from sklearn.tree import DecisionTreeClassifier # importing decision tree classifier
from sklearn.metrics import confusion_matrix  # importing matrix
dtree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, y_train) 
#X_test=[[0,65874,5864,895,0,0,0,0,32985.0,32889.0,0.0,5]]
dtree_predictions = dtree_model.predict(X_test) # predicting the output for the testing dataset
print(dtree_predictions)
#creating a confusion matrix 
cm = confusion_matrix(y_test, dtree_predictions) 
print(cm)