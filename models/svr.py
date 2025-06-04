from sklearn.svm import SVR

def get_svr_model():
    return SVR()

def get_svr_param_grid():
    return {
        'regression__kernel': ['rbf', 'linear'],
        'regression__C': [0.1, 1, 10],
        'regression__gamma': ['scale', 'auto']
    }