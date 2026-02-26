from app_content.application.interface.solution import Solution

class Generic(Solution):
    def __init__(self, basepath: str):
        self.basepath = basepath
        self.name = "generic"
    
    def execute(self,):
        '''Crea los modulos genericos en forma de model para despues usar
           el generador de archivos CRUD
        '''
        # genero por parte el model con el cual generare el sistema completo
        model = self.generate_model()
        # genero el sistema con el model creado
        self.generate_files(model=model, basepath=self.basepath,)

    def generate_files(self, model, basepath):
        '''Genero los files con la funcion generator del proyecto'''
        pass

    def generate_model(self,):
        '''
        Genero el model del sistema en string
        '''
        model = (
            f"{self.users_roles()}\n"
            f"{self.auditory()}\n"
            f"{self.notifications()}\n"
            f"{self.integration()}\n"
            f"{self.reports()}\n"
            f"{self.multicompany()}\n"
            f"{self.multibranch()}\n"
            f"{self.config()}\n"
            f"{self.logs()}\n"
            f"{self.auth()}\n"
            f"{self.imp_exp_data()}\n"
        )
        return model
    
    def users_roles(self,):
        '''Model del modulo de usuarios'''
        pass

    def auditory(self,):
        '''Model del modulo de auditoria'''
        pass
    
    def notifications(self,):
        pass
    
    def integration(self,):
        pass
    
    def reports(self,):
        pass
    
    def multicompany(self,):
        pass
    
    def multibranch(self,):
        pass
    
    def config(self,):
        pass
    
    def logs(self,):
        pass
    
    def auth(self,):
        pass
    
    def imp_exp_data(self,):
        ''' Model del modulo de importacion y exportacion de datos'''
        pass