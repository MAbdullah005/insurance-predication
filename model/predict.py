import pandas as pd
import json
import pickle

with open('model/model.pkl','rb') as f:
    model=pickle.load(f)

MODEL_VERSION='1.0.0'

class_label=model.classes_.tolist()

def predict_output(user_input:dict):

    df=pd.DataFrame([user_input])
    output=model.predict(df)[0]

    # get the probabilities for all classes
    probalities=model.predict_proba(df)[0]
    Confidence=max(probalities)
    # create mapping : {class name :probality}
    class_prob=dict(zip(class_label,map(lambda p:round(p,4),probalities)))
    return {'predicted_category':output,
            'confidence':round(Confidence,4),
            'class_probabilities':class_prob}