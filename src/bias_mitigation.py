from fairlearn.reductions import ExponentiatedGradient
from fairlearn.reductions import DemographicParity
from sklearn.ensemble import RandomForestClassifier


def mitigate_bias(X_train, y_train, sensitive):

    mitigator = ExponentiatedGradient(
        RandomForestClassifier(
         n_estimators=30,
         max_depth=6,
         random_state=42,
         n_jobs=-1
    ),
        constraints=DemographicParity()
    )

    mitigator.fit(
        X_train,
        y_train,
        sensitive_features=sensitive
    )

    return mitigator