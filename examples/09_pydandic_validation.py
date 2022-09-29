from pydantic import BaseModel, HttpUrl, Field, DirectoryPath

class ModelInput(BaseModel):
    url:HttpUrl
    rate:int = Field(ge=1, le=10) 
    target_dir: DirectoryPath
    
if __name__ == '__main__':
    valid_input = dict(url='https://naver.com',
                       rate=2,
                       target_dir='/home/dialog/ok/FastAPI/examples')
    invalid_input = dict(url='https://naver.com',
                       rate=2000,
                       target_dir='/home/dialog/ok/FastAPI/examples')
    
    from pydantic import ValidationError
    valid_pydantic_model_input = ModelInput(**valid_input)
    
    try: 
        invalid_pydantic_model_input = ModelInput(**invalid_input)
    except ValidationError as exc: # 이런 log도 차후에 저장해도 좋을 듯
        print(exc.json())
        pass