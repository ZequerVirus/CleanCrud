from app_content.domain.entities.model_entity import ModelEntity
from app_content.application.interface.entity import Entity
from app_content.application.interface.usecase import UseCase
from app_content.application.interface.repository import Repository
from app_content.application.interface.repositoryimpl import RepositoryImpl
from app_content.application.interface.view import View
from app_content.application.interface.fieldmapper import FieldMapper

class GenerateFiles:
    def __init__(
            self, 
            model_name: str,
            model_path: str,
            base_path: str,
            fieldmapper: FieldMapper,
            # dto: GenerateDTO, 
            entity: Entity, 
            usecase: UseCase, 
            repository: Repository, 
            repository_impl: RepositoryImpl,
            view: View,
        ):
        # self.dto = dto
        self.model_name = model_name
        self.model_path = model_path
        self.base_path = base_path
        self.fieldmapper = fieldmapper
        self.entity = entity
        self.usecase = usecase
        self.repository = repository
        self.repository_impl = repository_impl
        self.view = view

    def execute(self,):
        ''' Generate the files for the model '''
        try:
            fields = self.fieldmapper.execute(model_name=self.model_name, model_path=self.model_path)
            model = ModelEntity(
                nombre=self.model_name,
                fields=fields,
            )
            # self.dto.execute(model=model, basepath=self.base_path,)
            self.entity.execute(model=model, basepath=self.base_path,)
            self.usecase.execute(model=model, basepath=self.base_path,)
            self.repository.execute(model=model, basepath=self.base_path,)
            self.repository_impl.execute(model=model, basepath=self.base_path,)
        except Exception as e:
            raise Exception(e)