from fastapi import FastAPI
from typing import  Literal,Annotated
from Schema.user_input import UserInput
from fastapi.responses import JSONResponse
from Schema.pred_responce import PredicationeRespornce
from model.predict import predict_output,model,MODEL_VERSION



app=FastAPI()
  

    # home endpoint for users 
@app.get('/')
def home():
    return {'message':'insurance prenium predicatio Api'}

# home endpoint for machine readable like aws,kuernative
@app.get('/health')
def health_check():
    return {'status':'OK',
            'Version ':MODEL_VERSION,
            'Model Loaded':model is not None}
    
@app.post('/predict',response_model=PredicationeRespornce)
def predict(data:UserInput):
    input_df={'bmi':data.bmi,'age_group':data.age_group,
                            'lifestyle_risk':data.lifestyle_risk,
                         'city_tier':data.city_tier,'income_lpa':data.income_lpa,
                         'occupation':data.occupation}
    try :
      predication=predict_output(input_df)
      return JSONResponse(status_code=200,content={'response':predication})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
    