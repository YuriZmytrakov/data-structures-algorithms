from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KDTree
import pandas as pd
import numpy as np
import os

os.chdir("/Users/yurizmytrakov/Desktop/")

def read_data(fileName):
    return pd.read_csv(fileName)

def prepare_df(data):
    df_place_features = data.pivot(
        index='userID',
        columns='placeID',
        values='rating'
    ).fillna(0)
    return df_place_features

def recommend_places(userID, placeID, place_ratings, n_neighbors):
    try:
        already_predicted = place_ratings.loc[userID][placeID]
        if(already_predicted == 0):
            users_that_rated = place_ratings[place_ratings[placeID] > 0 ][placeID]
            closest = users_that_rated[:n_neighbors]
            return np.mean(closest), closest
        else:
            return already_predicted, None
    except:
        users_that_rated = place_ratings[place_ratings[placeID] > 0 ][placeID]
        print(users_that_rated)
        closest = users_that_rated[:n_neighbors]
        return np.mean(closest), closest

def getPredictedRatings_KNN(fileName, givenUserID, givenPlaceID, n_neighbors=2):
    data = read_data(fileName)
    place_ratings = prepare_df(data)
    rating, similar_users = recommend_places(givenUserID, givenPlaceID, place_ratings, n_neighbors)
    if (similar_users is None):  
        return rating, None
    else:
        return rating, similar_users.index

pred_rating, nsimilar_users = getPredictedRatings_KNN('ratings_data.csv','U1001', 'H132830', 2)
print(pred_rating, nsimilar_users)