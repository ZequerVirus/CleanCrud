from app_content.domain.entities.model_entity import ModelEntity
from app_content.application.interface.backend.fieldmapper import FieldMapper

class GenerateFiles:
    ''' Generate the files from model '''
    def __init__(
            self, 
            model_name: str,
            model_path: str,
            base_path: str,
            fieldmapper: FieldMapper,
            language_to_map: str,
            **kwargs, 
            # entity: Entity, 
        ):
        '''
        Args:
            model_name (str): The name of the model
            model_path (str): The path of the model
            base_path (str): The base path to generate the files
            fieldmapper (FieldMapper): The field mapper
            language_to_map (str): The language to map
            kwargs (dict): The generators ex: { "repository": Repository(), "entity": Entity() }
        '''
        # self.dto = dto
        self.model_name = model_name
        self.model_path = model_path
        self.base_path = base_path[:-1] if base_path.endswith("/") else base_path
        self.fieldmapper = fieldmapper
        self.language_to_map = language_to_map
        self.generators = kwargs
        # self.entity = entity

    def execute(self,):
        ''' Generate the files for the model '''
        try:
            fields = self.fieldmapper.execute(model_name=self.model_name, model_path=self.model_path, language_to_map=self.language_to_map,)
            model = ModelEntity(
                nombre=self.model_name,
                fields=fields,
            )
            for key, generator in self.generators.items():
                print(f'Generando {key}...')
                if (hasattr(generator, 'execute') and callable(generator.execute)):
                    generator.model = model
                    generator.basepath = self.base_path
                    generator.execute()
                else:
                    raise Exception(f'Generator {key} does not have execute method')
            # self.entity.execute()
        except Exception as e:
            raise Exception(e)
        