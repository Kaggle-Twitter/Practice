import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import feature_extraction, linear_model, model_selection, preprocessing

# Read dara

train_df = pd.read_csv("/Practice/Data/train.csv")
test_df = pd.read_csv("/Practice/Data/test.csv")

train_df[train_df["target"] == 0]["text"].values[1]

# Translating tweets to word vectors
count_vectorizer = feature_extraction.text.CountVectorizer()
