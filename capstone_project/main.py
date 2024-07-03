from capstone_project import Analyzer, Classifier, Regressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, root_mean_squared_error, mean_absolute_error

def main(): 
#read data
    #absolute_path= 'E:/Repos/capstone_project/capstone_project/diamonds.csv'
    absolute_path= 'capstone_project/diamonds.csv'
    df = Analyzer.read_dataset(dataset_path=absolute_path)

#Testing for analyzer

#data exploration and preprocessing
    my_data_manipulation = Analyzer.DataManipulation(df=df)

#describe dataset
    #Analyzer.describe(dataset=df)

# Drop Missing Data
    #data_df = my_data_manipulation.drop_missing_data(df)
    #print(data_df)

# Drop columns if needed
    cleaned_df = my_data_manipulation.drop_column(column_names="Unnamed: 0")
    #print(cleaned_df)

# One hot encoder
    #encoded_df = my_data_manipulation.encode_features(column_names="color")
    #print(encoded_df)

# Label encoder
    lblencoded_df = my_data_manipulation.encode_label(column_names="color")
    lblencoded_df = my_data_manipulation.encode_label(column_names="cut")
    lblencoded_df = my_data_manipulation.encode_label(column_names="clarity")
    #print(lblencoded_df)

# Scale encoded data
    #scaled_df = my_data_manipulation.standardize(df=df)
    #print(scaled_df)

# Shuffle dataset
    shuffled_df = my_data_manipulation.shuffle(df=df)
    #print(shuffled_df)

# Get 50% sample of dataset
    sampled_df = my_data_manipulation.sample(df=df)
    #print(sampled_df)

# Retrieve data
    retrieved_df = my_data_manipulation.retrieve_data(df=df)
    #print(retrieved_df)


#testing DataVisualization class

   #my_data_visualization = Analyzer.DataVisualization(df=df)

# Plot correlation matrix
    #corr_matrix = my_data_visualization.plot_correlationMatrix(df=retrieved_df)
    #print(corr_matrix)

# Pair Plot
    #pair_plot = my_data_visualization.plot_pairplot(df=retrieved_df)
    #print(pair_plot)

# Plotting of histogram grouped - not utilized currently
    #histogram_group = my_data_visualization.plot_histograms_group(df=retrieved_df)
    #print(histogram_group)

#testing plotting of histogram categorical
    #histogram_cat = my_data_visualization.plot_histograms_categorical(column_name1="clarity")
    #print(histogram_cat)

# Box plot categorical
    #box_plotting = my_data_visualization.box_plot(df=retrieved_df, column_name1="clarity", column_name2="cut")
    #print(box_plotting)# execute encoding

#Before fitting and training we need to split the data

# train is now 80% of the entire data set
    y_true = retrieved_df['clarity'].values
    y_true = y_true.astype(int)
    #y_train = y_train.astype(int)
    x = retrieved_df[["carat","cut","color", "price", "depth","table","x","y","z"]].values
    
    x_train, x, y_train, y_true = train_test_split(x, y_true, random_state=0, test_size=0.8)

# test is now 10% of the initial data set
# validation is now 10% of the initial data set
    x_val, x, y_val, y_true = train_test_split(x, y_true, random_state=0, test_size=.5)

    score_dict = {}

# # Testing classifier.py

# NOTES for presentation: for Classifier we want the label to be clarity of the diamonds.

    score_dict = {}

#  #testing logisctical regression classifier   
#     logistic_regression_classifier = Classifier.CustomLogiscticRegression(params={}, random_state=0) 
#     logistic_regression_classifier.fit(x_train, y_train)
#     log_reg_predict = logistic_regression_classifier.predict(x)
#     score_dict["Logistic Regression"] = logistic_regression_classifier.score(y_true, log_reg_predict)
#     print(score_dict)
  


# testing Knn Classifier

    #KNN
    
    """  scores = []
    nums = range(1,25)
    best_knn = []
    best_score_i = -1000

    for i in nums:
        knn = Classifier.KNeighborsClassifier(n_neighbors = i)
        knn.fit(x_train, y_train)
        score_i = knn.score(x, y_true)
        scores.append(score_i)
        
        if score_i > best_score_i:
            best_score_i = score_i
            best_knn = i

    print(best_knn)

    knn = Classifier.CustomKNN_Classifier(n_neighbours=best_knn, params={})
    knn.fit(x_train, y_train)
    log_reg_predict = knn.predict(x)
    score_dict["KNN"] = knn.score(y_true, log_reg_predict)
    print(score_dict) """

 #testing Decistion Tree classifier   
   # decision_tree_classifier = Classifier.CustomDecisionTree(params={'criterion':'gini'})
   # decision_tree_classifier.fit(x_train, y_train)
    #log_reg_predict = decision_tree_classifier.predict(x)
   # score_dict["Decision Tree"] = decision_tree_classifier.score(y_true, log_reg_predict)
   # print(score_dict)

 #testing Random Forest classifier   
    
    #random_forest_classifier = Classifier.CustomRandomForest(n_estimators=100, random_state=0,params={'criterion':'gini', 'max_leaf_nodes': 100})
    #random_forest_classifier.fit(x_train, y_train)
    #log_reg_predict = random_forest_classifier.predict(x)
    #score_dict["Random Forest"] = random_forest_classifier.score(y_true, log_reg_predict)
    #print(score_dict)

#testing SVC Classifier
    #svc_classifier = Classifier.CustomSVC(random_state=0, params={'kernel':'rbf', 'max_iter': 3, 'verbose':True})
    #svc_classifier.fit(x_train, y_train)
    #log_reg_predict = svc_classifier.predict(x)
    #score_dict["SVC"] = svc_classifier.score(y_true, log_reg_predict)
    #print(score_dict)

#testing ANN Classifier
    #ann_classifier = Classifier.CustomANN_Classifier(params={"hidden_layer_sizes":(100, 100, 100),'activation':'relu', 'solver':'adam', 'max_iter': 1000}, random_state=0)
    #ann_classifier.fit(x_train, y_train)
    #log_reg_predict = ann_classifier.predict(x)
    #score_dict["ANN"] = ann_classifier.score(y_true, log_reg_predict)
    #print(score_dict)

# #Plot of end results
# #plt.figure(figsize=(12,8))
# #plt.ylim(.5, 1)
# #sns.barplot(x=estimator, y= accuracy_score)


# Testing Regressor.py

# NOTES for presentation: for Regressor we want to switch price and clarity again for label as the problem we are trying to solve with regression is the pricing of the diamonds based on their features

#testing Linear Regressor  
    linear_regression = Regressor.CustomLinearRegression(params={}, random_state=0)
    linear_regression.fit(x_train, y_train)
    linear_regression.score(y_true=y_true, x=x)
 

# testing Knn Regressor

#KNN

    # scores = []
    # nums = range(1,25)
    # best_knn = []
    # best_score_i = -1000

    # for i in nums:
    #     knn_reg = Regressor.KNeighborsRegressor(n_neighbors = i)
    #     knn_reg.fit(x_train, y_train)
    #     score_i = knn_reg.score(x, y_true)
    #     scores.append(score_i)
        
    #     if score_i > best_score_i:
    #         best_score_i = score_i
    #         best_knn = i

    # print(best_knn)

    # knn_reg = Regressor.CustomKNN_Regressor(n_neighbours=best_knn, params={})
    # knn_reg.fit(x_train, y_train)
    # knn_reg.score(y_true=y_true, x=x)


 #testing Decision Tree Regressor   
    # decision_tree_reg = Regressor.CustomDecisionTreeReg(params={})
    # decision_tree_reg.fit(x_train, y_train)
    # decision_tree_reg.score(y_true=y_true, x=x)


 #testing Random Forest Regressor   
    
    # random_forest_regressor = Regressor.CustomRandomForestReg(n_estimators=100, random_state=0,params={'max_leaf_nodes': 100})
    # random_forest_regressor.fit(x_train, y_train)
    # random_forest_regressor.score(y_true=y_true, x=x)


#testing SVR Regressor
    # svr_regressor = Regressor.CustomSVR(params={}, random_state=0)
    # svr_regressor.fit(x_train, y_train)
    # svr_regressor.score(y_true=y_true, x=x)

#testing ANN Regressor
    #ann_regressor = Regressor.CustomANN_Regressor(params={"hidden_layer_sizes":(100, 100, 100),'activation':'relu', 'solver':'adam', 'max_iter': 1000}, random_state=0)
    #ann_regressor.fit(x_train, y_train)
    #ann_regressor.score(y_true=y_true, x=x)

main()