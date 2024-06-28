import joblib

def load_pipeline(file_path):
    try:
        pipeline = joblib.load(file_path)
        return pipeline
    except Exception as e:
        print(f"Error loading pipeline: {e}")
        return None

def main():
    logistic_regression_pipeline_path = './models/Logistic_Regression.joblib'
    random_forest_pipeline_path = './models/Random_Forest.joblib'

    print("Loading Logistic Regression Pipeline...")
    logistic_regression_pipeline = load_pipeline(logistic_regression_pipeline_path)
    if logistic_regression_pipeline:
        print("Logistic Regression Pipeline:")
        print(logistic_regression_pipeline)

    print("\nLoading Random Forest Pipeline...")
    random_forest_pipeline = load_pipeline(random_forest_pipeline_path)
    if random_forest_pipeline:
        print("Random Forest Pipeline:")
        print(random_forest_pipeline)

if __name__ == "__main__":
    main()
