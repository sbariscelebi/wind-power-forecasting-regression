from sklearn.neighbors import KNeighborsRegressor

def get_knn_model():
    return KNeighborsRegressor()

def get_knn_param_grid():
    return {
        'regression__n_neighbors': [3, 5, 7, 9]
    }