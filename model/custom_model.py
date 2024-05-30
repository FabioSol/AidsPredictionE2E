from sklearn.ensemble import RandomForestClassifier

class CustomModel(RandomForestClassifier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

