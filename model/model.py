import pickle

with open("./model/xgb_model.pkl","rb") as f:
    aa = pickle.load(f)

def predict(input):
    pred=aa.predict_proba(input)
    print(pred)
    return pred 

    