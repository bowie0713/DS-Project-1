from DataCleaning import data_cleaning
import joblib

df = data_cleaning()
def hotelmodel(df):
    import pandas as pd
    import numpy as np
    import warnings

    from sklearn.preprocessing import LabelEncoder
    #from sklearn.preprocessing import OneHotEncoder
    #from sklearn.preprocessing import OrdinalEncoder
    import re
    from sklearn.model_selection import train_test_split
    from xgboost import XGBClassifier
    from imblearn.over_sampling import SMOTE

    label_encoder = LabelEncoder()

    X = df.drop(['start_date', 'end_date','month', 'day', 'hotel_name'], axis=1)
    y = df['hotel_name']


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Sed seed so results can be duplicated, use stratify to make sure to keep the same percentages of classes for the split
    y_train = label_encoder.fit_transform(y_train) # Class column has to start from 0 to solve "Invalid classes inferred from unique values of `y`"

    #smenn = SMOTEENN()
    #X_train_smenn, y_train_smenn = SMOTE(k_neighbors=3).fit_resample (X_train2, y_train2)

    # calculate class weights based on the training data
    # classes = np.unique(y_train)
    # class_weights = compute_class_weight('balanced', classes=classes, y=y_train)
    # class_weight_dict = {classes[i]: class_weights[i] for i in range(len(classes))}
    # sample_weights = np.array([class_weight_dict[class_] for class_ in y_train])
    xgb_base_model = XGBClassifier(n_estimators = 200, base_score = 0.005, learning_rate = 0.05, random_state=42, eval_metric='mlogloss', max_depth = 3) 
    #base_score: inverse of the number of classes
    xgb_base_model.fit(X_train, y_train)
    base_predictions2 = xgb_base_model.predict(X_test)

    joblib.dump(xgb_base_model, 'saved_model.pkl')
    #return base_predictions2
hotelmodel(df)
