# -*- coding: utf-8 -*-
"""German_Credit

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gDtyK1RixWH3d6S9RLCvPqYcNeq_J145
"""

#mounting drive
from google.colab import drive
drive.mount('/content/drive')

# Listing the file in the German_Credit folder to confirm dataset name
import os
print(os.listdir('/content/drive/My Drive/German_Credit'))

#importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display the first few rows of the dataset to understand the data structure and initial values
df=pd.read_csv('/content/drive/My Drive/German_Credit/German_Credit.csv')
df.head()

# Check data types and missing values
import pandas as pd
df.info()

import pandas as pd

# Load the dataset
df = pd.read_csv('/content/drive/My Drive/German_Credit/German_Credit.csv')

# Rename columns to correct spelling and follow consistent format
df.rename(columns={
    'Saving accounts': 'Savings account',
    }, inplace=True)

# Rename columns to snake_case for consistency
df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]

# Convert 'risk' column to a categorical data type
df['risk'] = df['risk'].astype('category')

# Convert object columns to category to save memory
categorical_columns = ['sex', 'job', 'housing', 'savings_account', 'checking_account', 'purpose']
df[categorical_columns] = df[categorical_columns].apply(lambda x: x.astype('category'))

# Display the updated dataset information
df.info()

df.shape

# Summary statistics for numeric columns
df.describe()

# Histogram for age
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=20, color='orange', kde=True)
plt.title("Distribution of Age")
plt.xlabel("age")
plt.ylabel("frequency")
plt.xticks(range(20, 81, 5))
plt.show()

# Histogram for credit_amount
plt.figure(figsize=(15, 6))
sns.histplot(df['credit_amount'], bins=10, color='green',kde=True,)
plt.title("Distribution of credit_amount")
plt.xlabel("credit_amount")
plt.ylabel("frequency")
plt.show()

# Histogram for duration
plt.figure(figsize=(15, 8))
sns.histplot(df['duration'], bins=20, kde=True, color='purple')
plt.title("Distribution of Loan Duration")
plt.xlabel("duration (months)")
plt.ylabel("frequency")
plt.show()

# Box plot for age vs risk
plt.figure(figsize=(10, 4))
sns.boxplot(x='risk', y='age', data=df)
plt.title("Age Distribution by Risk")
plt.xlabel("risk (0: Not at risk, 1: At Risk)")
plt.ylabel("age")
plt.show()

# Box plot for Duration vs Risk
plt.figure(figsize=(10, 4))
sns.boxplot(x='risk', y='duration', data=df)
plt.title("Loan Duration Distribution by Risk")
plt.xlabel("risk (0: Not at risk, 1: At risk)")
plt.ylabel("duration (months)")
plt.show()

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Create a count plot for sex against risk
plt.figure(figsize=(10, 6))
sns.countplot(x='sex', hue='risk', data=df, palette='Set2')

plt.title('Count of sex against risk', fontsize=16)
plt.xlabel('sex', fontsize=14)
plt.ylabel('count', fontsize=14)
plt.legend(title='risk', labels=['Not at risk (0)', 'At risk (1)(defaulter)'])
plt.show()

plt.figure(figsize=(15, 6))
sns.countplot(data=df, x='job', hue='risk')
plt.title('Job categories vs. Risk')
plt.xlabel('job categories')
plt.ylabel('count')
plt.legend(title='risk', labels=['Good Credit (0)', 'Bad Credit (1)'])
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='housing', hue='risk')
plt.title('Housing vs. Risk')
plt.xlabel('housing status')
plt.ylabel('count')
plt.legend(title='risk', labels=['Good Credit (0)', 'Bad Credit (1)'])
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='savings_account', hue='risk')
plt.title('savings_account vs. risk')
plt.xlabel('savings_account status')
plt.ylabel('count')
plt.legend(title='risk', labels=['Good Credit (0)', 'Bad Credit (1)'])
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='checking_account', hue='risk')
plt.title('checking_account vs. risk')
plt.xlabel('checking_account status')
plt.ylabel('count')
plt.legend(title='risk', labels=['Good Credit (0)', 'Bad Credit (1)'])
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='purpose', hue='risk')
plt.title('Purpose of Loan vs. Risk')
plt.xlabel('Purpose of Loan')
plt.ylabel('count')
plt.legend(title='risk', labels=['Good Credit (0)', 'Bad Credit (1)'])
plt.xticks(rotation=45)
plt.show()

sns.pairplot(df, hue='risk', vars=['age', 'credit_amount', 'duration'])

plt.title('Pair Plot of age, credit_amount, and duration by risk')

plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

plt.figure(figsize=(15, 8))

numerical_df = df.select_dtypes(include=np.number)

correlation_matrix = numerical_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

plt.figure(figsize=(15, 6))
sns.scatterplot(data=df, x='age', y='credit_amount', hue='job', style='risk')
plt.title('credit_amount vs age colored by job category and risk')
plt.xlabel('age')
plt.ylabel('credit_amount')
plt.legend(title='job category and risk')
plt.show()

import pandas as pd

# Load the data
df = pd.read_csv('/content/drive/My Drive/German_Credit/German_Credit.csv')

# Convert column names to lowercase (if not done already)
df.columns = [col.lower() for col in df.columns]

# Convert relevant columns to category
categorical_columns = ['sex', 'job', 'housing', 'saving accounts', 'checking account', 'purpose']
df[categorical_columns] = df[categorical_columns].apply(lambda x: x.astype('category'))

# One-hot encode categorical columns
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['age', 'credit amount', 'duration']] = scaler.fit_transform(df[['age', 'credit amount', 'duration']])

# Check for missing values
print(df.isnull().sum())

# Fill missing values or drop rows/columns as needed
df.fillna(df.median(), inplace=True)

df[['age', 'credit amount', 'duration']].mean(), df[['age', 'credit amount', 'duration']].std()

from sklearn.model_selection import train_test_split

# Define features and target variable
X = df.drop('risk', axis=1)  # Features
y = df['risk']  # Target variable

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

# Initialize and train Logistic Regression model with controlled iterations
model = LogisticRegression(random_state=42, max_iter=500)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])

# Display metrics
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
print(f"ROC-AUC Score: {roc_auc}")

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

# Define hyperparameter grid
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],  # Regularization strength
    'max_iter': [100, 200, 500, 1000]  # Iteration limits
}

# Initialize Logistic Regression
log_reg = LogisticRegression(random_state=42)

# GridSearchCV for Logistic Regression
grid_search = GridSearchCV(estimator=log_reg, param_grid=param_grid, cv=5, scoring='f1', verbose=1)
grid_search.fit(X_train, y_train)

# Best model and parameters
best_model = grid_search.best_estimator_
print("Best Parameters:", grid_search.best_params_)

# Evaluate the tuned model
y_pred_tuned = best_model.predict(X_test)
accuracy_tuned = accuracy_score(y_test, y_pred_tuned)
f1_tuned = f1_score(y_test, y_pred_tuned)

print(f"Tuned Accuracy: {accuracy_tuned}")
print(f"Tuned F1 Score: {f1_tuned}")

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

# Initialize and train Random Forest model
model_rf = RandomForestClassifier(random_state=42, n_estimators=100, max_depth=5)  # You can experiment with parameters
model_rf.fit(X_train, y_train)

# Make predictions
y_pred_rf = model_rf.predict(X_test)

# Calculate metrics
accuracy_rf = accuracy_score(y_test, y_pred_rf)
precision_rf = precision_score(y_test, y_pred_rf)
recall_rf = recall_score(y_test, y_pred_rf)
f1_rf = f1_score(y_test, y_pred_rf)
roc_auc_rf = roc_auc_score(y_test, model_rf.predict_proba(X_test)[:, 1])

# Print metrics
print(f"Accuracy: {accuracy_rf}")
print(f"Precision: {precision_rf}")
print(f"Recall: {recall_rf}")
print(f"F1 Score: {f1_rf}")
print(f"ROC-AUC Score: {roc_auc_rf}")

# Confusion Matrix
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
print("Random Forest - Confusion Matrix:\n", conf_matrix_rf)

from sklearn.ensemble import RandomForestClassifier

# Define parameter grid for Random Forest
param_grid_rf = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Perform Grid Search
grid_search_rf = GridSearchCV(RandomForestClassifier(random_state=42), param_grid_rf, cv=5, scoring='f1', verbose=1)
grid_search_rf.fit(X_train, y_train)

# Best parameters and model
best_rf_model = grid_search_rf.best_estimator_
print("Best parameters for Random Forest:", grid_search_rf.best_params_)

# Evaluate the model
y_pred_rf = best_rf_model.predict(X_test)
print("Random Forest Classification Report:\n", classification_report(y_test, y_pred_rf))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rf))

import xgboost as xgb
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

# Initialize and train XGBoost model
model_xgb = xgb.XGBClassifier(random_state=42, eval_metric='logloss', use_label_encoder=False)
model_xgb.fit(X_train, y_train)

# Make predictions
y_pred_xgb = model_xgb.predict(X_test)

# Calculate metrics
accuracy_xgb = accuracy_score(y_test, y_pred_xgb)
precision_xgb = precision_score(y_test, y_pred_xgb)
recall_xgb = recall_score(y_test, y_pred_xgb)
f1_xgb = f1_score(y_test, y_pred_xgb)
roc_auc_xgb = roc_auc_score(y_test, model_xgb.predict_proba(X_test)[:, 1])

# Print metrics
print(f"Accuracy: {accuracy_xgb}")
print(f"Precision: {precision_xgb}")
print(f"Recall: {recall_xgb}")
print(f"F1 Score: {f1_xgb}")
print(f"ROC-AUC Score: {roc_auc_xgb}")

# Confusion Matrix
conf_matrix_xgb = confusion_matrix(y_test, y_pred_xgb)
print("XGBoost - Confusion Matrix:\n", conf_matrix_xgb)

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

# Initialize and train SVM model
model_svm = SVC(probability=True, random_state=42)
model_svm.fit(X_train, y_train)

# Make predictions
y_pred_svm = model_svm.predict(X_test)

# Calculate metrics
accuracy_svm = accuracy_score(y_test, y_pred_svm)
precision_svm = precision_score(y_test, y_pred_svm)
recall_svm = recall_score(y_test, y_pred_svm)
f1_svm = f1_score(y_test, y_pred_svm)
roc_auc_svm = roc_auc_score(y_test, model_svm.predict_proba(X_test)[:, 1])

# Print metrics
print(f"SVM - Accuracy: {accuracy_svm}")
print(f"SVM - Precision: {precision_svm}")
print(f"SVM - Recall: {recall_svm}")
print(f"SVM - F1 Score: {f1_svm}")
print(f"SVM - ROC-AUC Score: {roc_auc_svm}")

# Confusion Matrix
conf_matrix_svm = confusion_matrix(y_test, y_pred_svm)
print("SVM - Confusion Matrix:\n", conf_matrix_svm)

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

# Define the parameter grid
param_grid_svm = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
    'gamma': [0.01, 0.1, 1, 'scale', 'auto']
}

# Initialize GridSearchCV
grid_svm = GridSearchCV(SVC(probability=True, random_state=42), param_grid_svm, cv=5, scoring='roc_auc', verbose=2)

# Fit to the training data
grid_svm.fit(X_train, y_train)

# Best parameters and score
print("Best Parameters for SVM:", grid_svm.best_params_)
print("Best ROC-AUC for SVM:", grid_svm.best_score_)

from sklearn.ensemble import GradientBoostingClassifier

# Initialize and train Gradient Boosting model
model_gbm = GradientBoostingClassifier(random_state=42, n_estimators=100, max_depth=3)
model_gbm.fit(X_train, y_train)

# Make predictions
y_pred_gbm = model_gbm.predict(X_test)

# Calculate metrics
accuracy_gbm = accuracy_score(y_test, y_pred_gbm)
precision_gbm = precision_score(y_test, y_pred_gbm)
recall_gbm = recall_score(y_test, y_pred_gbm)
f1_gbm = f1_score(y_test, y_pred_gbm)
roc_auc_gbm = roc_auc_score(y_test, model_gbm.predict_proba(X_test)[:, 1])

# Print metrics
print(f"GBM - Accuracy: {accuracy_gbm}")
print(f"GBM - Precision: {precision_gbm}")
print(f"GBM - Recall: {recall_gbm}")
print(f"GBM - F1 Score: {f1_gbm}")
print(f"GBM - ROC-AUC Score: {roc_auc_gbm}")

# Confusion Matrix
conf_matrix_gbm = confusion_matrix(y_test, y_pred_gbm)
print("GBM - Confusion Matrix:\n", conf_matrix_gbm)

from sklearn.ensemble import GradientBoostingClassifier

# Define parameter grid for Gradient Boosting
param_grid_gb = {
    'learning_rate': [0.01, 0.1, 0.2],
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7]
}

# Perform Grid Search
grid_search_gb = GridSearchCV(GradientBoostingClassifier(random_state=42), param_grid_gb, cv=5, scoring='f1', verbose=1)
grid_search_gb.fit(X_train, y_train)

# Best parameters and model
best_gb_model = grid_search_gb.best_estimator_
print("Best parameters for Gradient Boosting:", grid_search_gb.best_params_)

# Evaluate the model
y_pred_gb = best_gb_model.predict(X_test)
print("Gradient Boosting Classification Report:\n", classification_report(y_test, y_pred_gb))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_gb))

from sklearn.neural_network import MLPClassifier

# Initialize and train MLP model
model_mlp = MLPClassifier(hidden_layer_sizes=(100,50), max_iter=500, random_state=42)
model_mlp.fit(X_train, y_train)

# Make predictions
y_pred_mlp = model_mlp.predict(X_test)

# Calculate metrics
accuracy_mlp = accuracy_score(y_test, y_pred_mlp)
precision_mlp = precision_score(y_test, y_pred_mlp)
recall_mlp = recall_score(y_test, y_pred_mlp)
f1_mlp = f1_score(y_test, y_pred_mlp)
roc_auc_mlp = roc_auc_score(y_test, model_mlp.predict_proba(X_test)[:, 1])

# Print metrics
print(f"MLP - Accuracy: {accuracy_mlp}")
print(f"MLP - Precision: {precision_mlp}")
print(f"MLP - Recall: {recall_mlp}")
print(f"MLP - F1 Score: {f1_mlp}")
print(f"MLP - ROC-AUC Score: {roc_auc_mlp}")

# Confusion Matrix
conf_matrix_mlp = confusion_matrix(y_test, y_pred_mlp)
print("MLP - Confusion Matrix:\n", conf_matrix_mlp)

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid_nn = {
    'hidden_layer_sizes': [(50,), (100,), (50, 50), (100, 100)],
    'activation': ['tanh', 'relu'],
    'solver': ['adam', 'sgd'],
    'learning_rate': ['constant', 'adaptive'],
    'max_iter': [200, 300, 500]
}

# Initialize GridSearchCV
grid_nn = GridSearchCV(MLPClassifier(random_state=42), param_grid_nn, cv=5, scoring='roc_auc', verbose=2)

# Fit to the training data
grid_nn.fit(X_train, y_train)

# Best parameters and score
print("Best Parameters for Neural Network:", grid_nn.best_params_)
print("Best ROC-AUC for Neural Network:", grid_nn.best_score_)

!pip install catboost

import pandas as pd

# Load the data (you've already done this in your project)
df = pd.read_csv('/content/drive/My Drive/German_Credit/German_Credit.csv')

# Convert column names to lowercase (if not already done)
df.columns = [col.lower() for col in df.columns]

# Define features (X) and target (y)
X = df.drop('risk', axis=1)
y = df['risk']

# List of categorical columns
categorical_columns = ['sex', 'job', 'housing', 'saving accounts', 'checking account', 'purpose']

from sklearn.model_selection import train_test_split

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

# Initialize CatBoostClassifier
model_cat = CatBoostClassifier(
    iterations=500,       # Number of boosting iterations
    depth=6,              # Depth of the trees
    learning_rate=0.1,    # Learning rate
    cat_features=categorical_columns,  # List of categorical feature names
    verbose=100,          # Log progress every 100 iterations
    random_state=42       # Ensures reproducibility
)

# Train the model
model_cat.fit(X_train, y_train)

# Make predictions
y_pred_cat = model_cat.predict(X_test)
y_pred_proba_cat = model_cat.predict_proba(X_test)[:, 1]

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred_cat)
precision = precision_score(y_test, y_pred_cat)
recall = recall_score(y_test, y_pred_cat)
f1 = f1_score(y_test, y_pred_cat)
roc_auc = roc_auc_score(y_test, y_pred_proba_cat)

print(f"CatBoost - Accuracy: {accuracy}")
print(f"CatBoost - Precision: {precision}")
print(f"CatBoost - Recall: {recall}")
print(f"CatBoost - F1 Score: {f1}")
print(f"CatBoost - ROC-AUC Score: {roc_auc}")

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred_cat)
print("CatBoost - Confusion Matrix:\n", conf_matrix)

from catboost import CatBoostClassifier
from sklearn.model_selection import GridSearchCV

# Define the parameter grid
param_grid_cb = {
    'iterations': [100, 200, 500],
    'learning_rate': [0.01, 0.1, 0.2],
    'depth': [3, 5, 7],
    'l2_leaf_reg': [1, 3, 5],
    'border_count': [32, 64, 128]
}

# Initialize CatBoost model
catboost_model = CatBoostClassifier(random_state=42, verbose=0, eval_metric='AUC')

# Set up GridSearchCV
grid_cb = GridSearchCV(estimator=catboost_model, param_grid=param_grid_cb, cv=5, scoring='roc_auc', verbose=2)

# Fit the model
grid_cb.fit(X_train, y_train)

# Best parameters and score
print("Best Parameters for CatBoost:", grid_cb.best_params_)
print("Best ROC-AUC for CatBoost:", grid_cb.best_score_)