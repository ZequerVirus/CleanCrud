from app_content.application.interface.module import Module

class CreateModule():
    def __init__(self, basepath: str, name:str, module:Module):
        self.basepath = basepath
        self.name = name
        self.module = module

    def execute(self,):
        try:
            self.module.execute()
        except Exception as e:
            raise Exception(e)
        
    