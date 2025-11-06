import pydantic
class heartInput(pydantic.BaseModel):
    #   Column    Non-Null Count  Dtype--    --------------  -----  
    age       :   int  
    sex       :   int  
    cp        :   int  
    trestbps  :   int  
    chol      :   int  
    fbs       :   int  
    thalach   :   int  
    oldpeak   :   float


class heartOutput(pydantic.BaseModel):
    prediction: str