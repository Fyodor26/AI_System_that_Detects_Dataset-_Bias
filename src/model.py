from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_model(df, target):

    X = df.drop(target, axis=1)
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # save indices for fairness metrics
    train_index = X_train.index
    test_index = X_test.index

    # Random Forest model
    model = RandomForestClassifier(
       n_estimators=50,
       max_depth=8,
       random_state=42,
       n_jobs=-1
)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    return (
        model,
        X_train,
        X_test,
        y_train,
        y_test,
        predictions,
        accuracy,
        train_index,
        test_index
    )