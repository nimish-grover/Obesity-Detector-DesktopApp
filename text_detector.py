import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
import sklearn.preprocessing as preprocessing


df= pd.read_csv("obesitydataset.csv")
le=preprocessing.LabelEncoder()

df['gender']=le.fit_transform(df['Gender'].astype(str))
df['famhistory']=le.fit_transform(df['family_history_with_overweight'].astype(str))
df['smoke']=le.fit_transform(df['SMOKE'].astype(str))
df['mtrans']=le.fit_transform(df['MTRANS'].astype(str))
df['nobeyes']=le.fit_transform(df['NObeyesdad'].astype(str))
df=df.drop(['Gender','family_history_with_overweight','SMOKE','MTRANS','NObeyesdad'],axis=1)
df.to_csv('obesitydatasetpreprocessed.csv')

y=df.nobeyes
X=df.drop(['nobeyes'],axis='columns')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
X_train.shape, X_test.shape

### Category Boosting (CatBoost).

clf = CatBoostClassifier(
    iterations=1000,
  learning_rate=0.4,
  depth=5,
  colsample_bylevel=0.8,
  random_seed = 2020,
  bagging_temperature = 0.2,
  metric_period = None,
  custom_loss=['AUC', 'Accuracy']
)

# cat_features = list(range(0, X.shape[1]))
# #print(cat_features)
#
# clf.fit(X_train, y_train)
#
# clf.is_fitted()
# clf.get_params()
# p=clf.predict(X_test)
# accuracy_score(y_test, p)
# precision_recall_fscore_support(y_test, p, average='weighted')
# clf.save_model("model")
clf.load_model('model')
pred_list=["Insufficient Weight","Normal","Obesity Type 1","Obesity Type 2","Obesity Type 3","Overweight level 1","Overweight level 2"] 
