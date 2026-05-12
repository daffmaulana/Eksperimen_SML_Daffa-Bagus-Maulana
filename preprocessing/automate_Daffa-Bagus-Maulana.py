import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def rename_columns(df):
    df = df.rename(
        columns={
            'cp': 'chest_pain_type',
            'trestbps': 'resting_blood_pressure',
            'chol': 'cholesterol',
            'fbs': 'fasting_blood_sugar',
            'restecg': 'resting_electrocardiogram',
            'thalach': 'max_heart_rate_achieved',
            'exang': 'exercise_induced_angina',
            'oldpeak': 'st_depression',
            'slope': 'st_slope',
            'ca': 'num_major_vessels',
            'thal': 'thalassemia'
        },
        errors="raise"
    )

    return df

def remove_invalid_values(df):
    df = df[df['ca'] < 4]
    df = df[df['thal'] > 0]

    return df

def preprocess_data(df):
    df = remove_invalid_values(df)

    # Rename columns
    df = rename_columns(df)

    # Grouping features
    num_feats = [
        'age',
        'cholesterol',
        'resting_blood_pressure',
        'max_heart_rate_achieved',
        'st_depression',
        'num_major_vessels'
    ]

    bin_feats = [
        'sex',
        'fasting_blood_sugar',
        'exercise_induced_angina',
        'target'
    ]

    nom_feats = [
        'chest_pain_type',
        'resting_electrocardiogram',
        'st_slope',
        'thalassemia'
    ]

    cat_feats = nom_feats + bin_feats

    return df

def save_data(df, path):
    df.to_csv(path, index=False)

def main():
    df = load_data("./heartdisease_raw.csv")
    df = preprocess_data(df)
    save_data(df, "./preprocessing/heartdisease_preprocessing.csv")

if __name__ == "__main__":
    main()