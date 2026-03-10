from src.preprocessing import preprocess_data
from src.model import train_model
from src.bias_detection import detect_bias


def run_bias_pipeline(df, target, sensitive):

    # preprocessing
    df = preprocess_data(df)

    # convert target to binary
    if df[target].nunique() > 2:
        median_val = df[target].median()
        df[target] = (df[target] > median_val).astype(int)
    else:
        df[target] = df[target].astype("category").cat.codes

    (
        model,
        X_train,
        X_test,
        y_train,
        y_test,
        pred,
        acc,
        train_index,
        test_index
    ) = train_model(df, target)

    sensitive_test = df.loc[test_index, sensitive]

    bias_score = detect_bias(
        y_test,
        pred,
        sensitive_test
    )

    # bias interpretation
    if abs(bias_score) < 0.05:
        status = "Fair"
    elif abs(bias_score) < 0.1:
        status = "Mild Bias"
    else:
        status = "Bias Detected"

    return {
        "accuracy": acc,
        "bias_score": bias_score,
        "bias_status": status
    }