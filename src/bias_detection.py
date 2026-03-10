from fairlearn.metrics import demographic_parity_difference

def detect_bias(y_true, predictions, sensitive):

    bias_score = demographic_parity_difference(
        y_true,
        predictions,
        sensitive_features=sensitive
    )

    return bias_score