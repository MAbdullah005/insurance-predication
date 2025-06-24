from pydantic import BaseModel,Field
from typing import Dict


class PredicationeRespornce(BaseModel):
    predicted_category:str=Field(...,
                                    description='The predication insurance prenium categorey',
                                    examples=['low'])
    confidence:float=Field(...,
                           description='model confedence score for the prediation class (range 0 to 1)',
                           examples=[0.3213])
    class_probabilities:dict[str,float]=Field(...,
                                             description='probalities distribution across all ' \
                                             'possiable given classes ',
                                             examples=[{'Low':0.01,'medium':0.35,'high':0.89}])
    