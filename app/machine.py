from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import datetime
import joblib


class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Random Forest Model"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)
        self.timestamp = datetime.datetime.now()

    def __call__(self, feature_basis: DataFrame):
        prediction, *_ = self.model.predict(feature_basis)
        probability, *_ = self.model.predict_proba(feature_basis)
        return prediction, max(probability)

    def save(self, filepath):
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        loaded_model = joblib.load(filepath)
        return loaded_model

    def info(self):
        return self.name, self.timestamp
