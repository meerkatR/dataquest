## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

# same result with .iloc and .loc
dc_listings = dc_listings.iloc[numpy.random.permutation(len(dc_listings))]
split_one = dc_listings[0:1862]
split_two = dc_listings[1862:]

## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

knn = KNeighborsRegressor(n_neighbors = 5, algorithm = 'auto')

## here X must be of shape [n_samples, n_features]
## train_one['accommodates'] is a Series, and has the wierd shape [1862, ]
## train_one[['accommodates']] is a DataFrame, and has the correct shape [1862, 1]
knn.fit(train_one[['accommodates']], train_one['price'])
prediction = knn.predict(test_one[['accommodates']])
iteration_one_mse = mean_squared_error(prediction, test_one['price'])
iteration_one_rmse = iteration_one_mse**(1/2)


knn.fit(train_two[['accommodates']], train_two['price'])
prediction = knn.predict(test_two[['accommodates']])
iteration_two_mse = mean_squared_error(prediction, test_two['price'])
iteration_two_rmse = iteration_two_mse**(1/2)

avg_rmse = numpy.mean([iteration_one_rmse, iteration_two_rmse])



## 3. K-Fold Cross Validation ##

dc_listings['fold'] = numpy.repeat([1.0, 2.0, 3.0, 4.0, 5.0], [745, 745, 744, 744, 745])
#for i in list(range(5)):
#    dc_listings['fold'][(745*i):(745*(i+1))] = i+1
    
print(dc_listings['fold'].value_counts())
print(dc_listings['fold'].isnull().sum())


## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_iteration_one = dc_listings[dc_listings['fold'] != 1].copy()
test_iteration_one = dc_listings[dc_listings['fold'] == 1].copy()

model = KNeighborsRegressor()
model.fit(train_iteration_one[['accommodates']], train_iteration_one['price'])
labels = model.predict(test_iteration_one[['accommodates']])
iteration_one_rmse = mean_squared_error(test_iteration_one['price'], labels)**(1/2)

## 5. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]

def train_and_validate(df, folds):
    model = KNeighborsRegressor()
    rmses = []
    for fold in folds:
        train_df = dc_listings[dc_listings['fold'] != fold].copy()
        test_df = dc_listings[dc_listings['fold'] == fold].copy()
        model.fit(train_df[['accommodates']], train_df['price'])
        labels = model.predict(test_df[['accommodates']])
        rmse = mean_squared_error(test_df['price'], labels)**(1/2)
        rmses.append(rmse)
    return rmses

rmses = train_and_validate(dc_listings, fold_ids)
avg_rmse = np.mean(rmses)
print(rmses, avg_rmse)
    

## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

from sklearn.model_selection import cross_val_score, KFold
kf = KFold(n_splits = 5, shuffle = True, random_state = 1)
knn = KNeighborsRegressor()
mses = cross_val_score(estimator = knn, X = dc_listings[['accommodates']], y = dc_listings['price'], scoring = 'neg_mean_squared_error', cv = kf)
rmses = np.absolute(mses)**(1/2)
avg_rmse = np.mean(rmses)

## 7. Exploring Different K Values ##

from sklearn.model_selection import cross_val_score, KFold

num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="neg_mean_squared_error", cv=kf)
    rmses = np.sqrt(np.absolute(mses))
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))