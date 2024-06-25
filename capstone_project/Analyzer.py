import os
import sys
import pandas as pd
import numpy as np
from random import sample
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler


# Read dataset = function
def read_dataset(dataset_path: str) -> pd.DataFrame: 
    """ This function is to read the dataset
    """
    dataset = pd.read_csv(filepath_or_buffer=dataset_path)
    return dataset

# Describe dataset = function
def describe(dataset: pd.DataFrame): 
    """ This function is to describe the dataset
    """
    print(dataset.describe()) 
    
# Class 1 = Data Manipulation class, any below are members

class DataManipulation:
    def __init__(self, df: pd.DataFrame) -> pd.DataFrame:
        self.df_raw = df
        self.df = df.copy()

    
    def drop_missing_data(self, df: pd.DataFrame) -> pd.DataFrame: 
        """Drops rows with missing values in the specified column.

        Args:
            column_name (str): The name of the column to drop missing values from.

        Returns: pd.DataFrame: The DataFrame with missing values dropped.
        """
        self.df = self.df.dropna()
        return self.df
    
    def drop_column(self, column_names: str) -> pd.DataFrame:
        """Drop entire specified column
    
        Args:
        column_name (str): The name of the column to completely drop.
        
        Returns: pd.DataFrame: The DataFrame with the selected column removed
        """
        self.df = self.df.drop([column_names], axis=1)
        return self.df
    
    def encode_features(self, column_names: str) -> pd.DataFrame:
        """One hot encodes features of the specified column.

        Args:
            column_name (str): The name of the column to encode values from.

        Returns: pd.DataFrame: The DataFrame with features encoded.
        """
        enc = OneHotEncoder()
        self.df_onehot = pd.get_dummies(self.df[[column_names]], dtype=int)
        self.df = pd.concat([self.df, self.df_onehot], axis=1) 
        self.df = self.df.drop([column_names], axis=1)
        return self.df
    
    def encode_label(self, column_names: str) -> pd.DataFrame:
        """Label encodes in the specified column.

        Args:
            column_name (str): The name of the column to label encode values from.

        Returns: pd.DataFrame: The DataFrame with label encoded.
        """
        lbl_enc = LabelEncoder()
        self.df.loc[:, column_names] = lbl_enc.fit_transform(self.df[column_names])
        return self.df
    
    def standardize(self, df: pd.DataFrame) -> pd.DataFrame:
        """Standardize data in the dataset.

        Args:
            df (pd.DataFrame): The name of the dataset to standardize.

        Returns: pd.DataFrame: The DataFrame with standardization.
        """
        scaler = StandardScaler().set_output(transform="pandas")
        self.df = scaler.fit_transform(self.df)
        return self.df

    def shuffle(self, df: pd.DataFrame) -> pd.DataFrame:
        """Shuffle the dataset

        Args:
            df (pd.DataFrame): The name of the dataset to shuffle.

        Returns: pd.DataFrame: The DataFrame shuffled.
        """
        shuffled_df = self.df.sample(n=len(self.df))
        return shuffled_df
    
    def sample(self, df: pd.DataFrame) -> pd.DataFrame:
        """Get 50% sample (0.5 frac) of the dataset

        Args:
            df (pd.DataFrame): The name of the dataset to shuffle.

        Returns: 50% of the pd.DataFrame:
        """
        self.df = self.df.sample(frac=0.5, replace=True, random_state=1)
        return self.df
    
    def retrieve_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Retrieve data at it's current

        Args:
            df (pd.DataFrame): The name of the dataset to retrieve.

        retrieved current (transformed) verion of pd.DataFrame:
        """
        return self.df
    
# Class 2 = Data Visualization class, any below are members

class DataVisualization:
    def __init__(self, df: pd.DataFram, column_name1: str, column_name2: str) -> pd.DataFrame:
        self.df = df
        self.column_name1 = column_name1
        self.column_name2 = column_name2

    def plot_correlationMatrix(self, df: pd.DataFrame) -> plt.show(): 
        """Using a heatmap show correlation matrix of features of dataset

        Args:
            df (pd.Dataframe): The name of the dataframe to use for visualization

        Returns: plt.show(): The heatmap visualization of the features
        """
        plt.figure(figsize=(12,12))
        correlation = sns.heatmap(df.corr(), annot=True).set_title('Correlated Heatmap of diamond features with price')
        return plt.show()
    
    def plot_pairplot(self, df: pd.DataFrame) -> plt.show(): 
        """Using a pairplot to visualize features of dataset
        
        Args:
            df (pd.Dataframe): The name of the dataframe to use for visualization

        Returns: plt.show(): The pairplot visualization of the features
        """
        
        sns.pairplot(df)
        return plt.show()
    
    def plot_histograms_group(self, df: pd.DataFrame) -> plt.show():
        """Using a histogram to visualilze the dataset

        Args:
            df (pd.Dataframe): The name of the dataframe to use for visualization

        Returns: plt.show(): The histogram visualization of the features
        """
        dataset_d = df.groupby(['color_D'])['price'].mean()
        dataset_e = df.groupby(['color_E'])['price'].mean()
        dataset_f = df.groupby(['color_F'])['price'].mean()
        dataset_g = df.groupby(['color_G'])['price'].mean()
        dataset_h = df.groupby(['color_H'])['price'].mean()
        dataset_i = df.groupby(['color_I'])['price'].mean()
        dataset_j = df.groupby(['color_J'])['price'].mean()

        fig, axs = plt.subplots(4, 2, figsize=(12,12))
        axs[0, 0].bar(dataset_d.index, dataset_d.values, width=0.5, color='green')
        axs[0, 0].set_title('Price for Color D')
        axs[0, 1].bar(dataset_e.index, dataset_e.values, width=0.5, color='blue')
        axs[0, 1].set_title('Price for Color E')
        axs[1, 0].bar(dataset_f.index, dataset_f.values, width=0.5, color='cyan')
        axs[1, 0].set_title('Price for Color F')
        axs[1, 1].bar(dataset_g.index, dataset_g.values, width=0.5, color='orange')
        axs[1, 1].set_title('Price for Color G')
        axs[2, 0].bar(dataset_h.index, dataset_h.values, width=0.5, color='magenta')
        axs[2, 0].set_title('Price for Color H')
        axs[2, 1].bar(dataset_i.index, dataset_i.values, width=0.5, color='yellow')
        axs[2, 1].set_title('Price for Color I')
        axs[3, 0].bar(dataset_j.index, dataset_j.values, width=0.5, color='black')
        axs[3, 0].set_title('Price for Color J')

        
        for ax in axs.flat:
            ax.set(xlabel='Feature', ylabel='Price')

        return plt.show()
    
    def plot_histograms_categorical(self, column_name1: str) -> plt.show():
        """Using a histogram to visualilze the dataset

        Args:
            df (pd.Dataframe): The name of the dataframe to use for visualization

        Returns: plt.show(): The histogram visualization of the features
        """   
        plt.figure(figsize=(12,12))
        ax = sns.catplot(x=column_name1, kind="count", palette="ch:.25", data=self.df)
        ax.figure.suptitle('Diamond Feature Count')
        return plt.show()
    
    def box_plot(self, df: pd.DataFrame, column_name1: str, column_name2: str) -> plt.show(): 
        """Using a boxplot to visualize features of dataset
        
        Args:
            df (pd.Dataframe): The name of the dataframe to use for visualization

        Returns: plt.show(): The boxplot visualization of the features
        """
        self.column
        sns.boxplot(data=df, x=column_name1, y=column_name2, whis=(0, 100))
        return plt.show()

if __name__== "__main__":

    #testing read dataset function

    #os.path.isdir('E:/Repos/capstone_project/capstone_project/diamonds.csv') os path exists

    absolute_path= 'E:/Repos/capstone_project/capstone_project/diamonds.csv'
    #absolute_path= 'C:/Users/hyppi/Repos/capstone_project/capstone_project/diamonds.csv'
    df = read_dataset(dataset_path=absolute_path)

    #testing describe function
    #describe(dataset=df)
    
   
    #testing DataManipulation class
    my_data_manipulation = DataManipulation(df=df)

    #testing drop na
    data_df = my_data_manipulation.drop_missing_data(df)
    #print(data_df)

    #testing drop column
    cleaned_df = my_data_manipulation.drop_column(column_names="Unnamed: 0")
    #print(cleaned_df)

    #testing feature one hot encoder
    #encoded_df = my_data_manipulation.encode_features(column_names="color")
    #print(encoded_df)

    #testing label encoder
    lblencoded_df = my_data_manipulation.encode_label(column_names="color")
    lblencoded_df = my_data_manipulation.encode_label(column_names="cut")
    lblencoded_df = my_data_manipulation.encode_label(column_names="clarity")
    #print(lblencoded_df)

    #testing label encoder
    scaled_df = my_data_manipulation.standardize(df=df)
    #print(scaled_df)
    
    #testing dataset shuffle
    shuffled_df = my_data_manipulation.shuffle(df=df)
    #print(shuffled_df)

    #testing dataset 50% sample
    sampled_df = my_data_manipulation.sample(df=df)
    #print(sampled_df)

    #testing retrieve data
    retrieved_df = my_data_manipulation.retrieve_data(df=df)
    print(retrieved_df)


    #testing DataVisualization class
    my_data_visualization = DataVisualization(df=df)

    #testing plotting of correlation matrix
    #corr_matrix = my_data_visualization.plot_correlationMatrix(df=retrieved_df)
    #print(corr_matrix)

    #testing pair Plot
    #pair_plot = my_data_visualization.plot_pairplot(df=retrieved_df)
    #print(pair_plot)


    #testing plotting of histogram grouped
    #histogram_group = my_data_visualization.plot_histograms_group(df=retrieved_df)
    #print(histogram_group)

    #testing plotting of histogram categorical
    #histogram_cat = my_data_visualization.plot_histograms_categorical(column_name1="clarity")
    #print(histogram_cat)

    #testing plotting of box plot categorical
    box_plotting = my_data_visualization.box_plot(column_name1="clarity")
    box_plotting = my_data_visualization.box_plot(column_name2="cut")
    print(box_plotting)