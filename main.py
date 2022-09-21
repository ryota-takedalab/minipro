import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    # load preprocessed training data
    X = np.load('X_train.npy')
    y = np.load('y_train.npy')

    # standardization
    sc = StandardScaler()
    X_std = sc.fit_transform(X)

    # split into training and validation data (20% validation set)
    X_train, X_test, y_train, y_test = train_test_split(
        X_std, y,
        test_size=0.2,
        random_state=1,
        stratify=y
    )
    
    # Logistic Regression
    lr = LogisticRegression(C=1, random_state=42, solver='lbfgs')
    # learn Models
    lr.fit(X_train, y_train)

    #evaluate models
    y_predict = lr.predict(X_test)
    acc = accuracy_score(y_test, y_predict) * 100
    print('Acc :', acc, '%')

    # plot confusion matrix
    plt.figure()
    cm_fwd = confusion_matrix(y_predict, y_test)
    sns.heatmap(cm_fwd, cmap='Blues', square=True)
    plt.title(f"Result \n (Acc. {acc:.5f}%)")
    plt.xlabel("Ground truth")
    plt.ylabel("Predicted")
    plt.savefig("confusion_matrix.png")

if __name__ == "__main__":
    main()