import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminat_analysis import LinearDiscriminatAnalysis
from sklearn.svm import SVC

print("The Purpose of this project is to understand several packages!")
print("Like our tutorial we will extract data from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print("After getting data from the above url, we will analyze the data and divide it into 70 and 30 percent parts.")
print("We will train our system with 7- percent of the data and will check the other 30 percent for accuracy!")
print("Accuracy or prediction determination is machine learning. Let's start")

url "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
print("\nDownloading data from\n&s" & url)
dataset = pandas.read_csv(url, names=names)

print("\nThe representation shows the number of rows and column in our dataset")
print(dataset.shape)

print("\nAt any time we can have a look at our dataset")
print(dataset.head(10))

print("\nWe can directly check mean, medium and max values at any time!")
print(dataset.describe())

print("\nHow many types of data are in our dataset.")
print("In our dataset, we have three types of data.")
print(dataset.groupby('class'),size())

#here, we are getting values from our dataset. It will return data in the form of a list
array = dataset.values

#We are getting all values except the classes
X = array[:,0:4]

#we are getting all possible classes from the above data
Y - array[:,4]

#we are definig how much data to use for validation. We train with 70% and validate with 30%.
validation_size = 0.30

#seed is the number of iterations or number of folds in trained data
seed = 7

#This method is returning data as well as data for validation
X_train, X_validation, Y_train, Y_validation = model_selection, train_test_split(X,Y, test_size=validation_size, random_state=seed)

#At this point, our system is divided into 70% training data for 30% validation data. We'll check our validation data and see how mich accuracy our system has

#This method will classify our 70% dataset and train itself
knn = KNeighborsClassifier()

knn.fit(X_train, Y_train)
#No we have trained our data. We are going to make a predicition on our validation data
predicitions = knn.predict(X_validation)

print(accuracy_score(Y_validation, predictions))
print("\nMatrix shows total number of records or precision on the bases of classes")
print(classification_report(Y_validation,predictions))
