import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def main():
    # load preprocessed training data
    X = np.load('X_train.npy')
    y = np.load('y_train.npy')

    # 標準化のインスタンスを生成（平均=0, 標準偏差=1 に変換）
    sc = StandardScaler()
    X_std = sc.fit_transform(X)

    # split into training and validation data (20% validation set)
    X_train, X_test, y_train, y_test = train_test_split(
        X_std, y,
        test_size=0.2,
        random_state=1,
        stratify=y
    )
    
    # ロジスティック回帰のインスタンスを作成
    lr = LogisticRegression(C=1, random_state=42, solver='lbfgs')
    # モデルの学習
    lr.fit(X_train, y_train)
    
    print(lr.score(X_train,y_train))
    print(lr.score(X_test,y_test))

if __name__ == "__main__":
    main()