from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np


def displayNull(df):
    """
    Display percentage of NaN of values in each column of a dataframe
    """
    countNull = df.isnull().sum() * 100 / len(df)
    print(countNull)


def featureimportance(model, features):
    """
    Finds the feature imporatnce in Linear Regression model

    Returns a Dataframe of Features and its imporatance while training the model
    """
    model.coef_.T
    feature_importance = pd.DataFrame(np.hstack((np.reshape(np.array(
        features).T, (-1, 1)), model.coef_.T)), columns=['feature', 'importance'])
    feature_importance['importance'] = pd.to_numeric(
        feature_importance['importance'])

    return feature_importance.sort_values(by='importance', ascending=False)


def grid_search(X, y, model, hyperparameters, cv=3):
    """
    Applies grid search on a model to determine its best hyperparameters
    Returns GridSearch object and Best Parameters and Score
    """
    gs = GridSearchCV(model, hyperparameters, cv=cv,
                      verbose=0, scoring='accuracy')
    gs.fit(X, y)

    return gs, gs.best_params_, gs.best_score_


def saveCSV(data, prob):
    """
    Saves Probabilities of the Lead getting converted as a CSV file
    """
    info = {
        'Prospect ID': data.loc[:, 'Prospect ID'],
        'Lead Number': data.loc[:, 'Lead Number'],
        'Probability of getting converted': np.round(prob[:, 1], 2)
    }

    df = pd.DataFrame(info)
    df.to_csv('lead_prob.csv', sep=',')

    return df
