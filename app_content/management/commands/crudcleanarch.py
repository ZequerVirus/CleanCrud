from django.core.management.base import BaseCommand, CommandError, CommandParser
from app_content.application.usecases.generate_files import GenerateFiles
from app_content.infraestructure.generators.Python.entity import PythonEntity
from app_content.infraestructure.generators.Python.usecase import PythonUseCase
from app_content.infraestructure.generators.Python.repository import PythonRepository
from app_content.infraestructure.generators.Python.repositoryimpl import PythonRepositoryImpl
from app_content.infraestructure.generators.Python.view import PythonView

import os
import traceback
from app_content.infraestructure.mappers.Django.djangofieldmapper import DjangoFieldMapper
from app_content.infraestructure.mappers.Django.fieldstype import DjangoFieldType
from app_content.infraestructure.generators.flutter.bloc.bloc import FlutterBloc
from app_content.infraestructure.generators.flutter.bloc.event import FlutterEvent
from app_content.infraestructure.generators.flutter.bloc.state import FlutterState
from app_content.infraestructure.generators.flutter.usecase import FlutterUseCase
from app_content.infraestructure.generators.flutter.entity import FlutterEntity

class Command(BaseCommand):
    help = 'Generate CRUD clean architecture using a model'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--model', required=True, help='Model name to generate (example: User)')
        parser.add_argument('--basepath', required=True, help='Base path to generate (example: app_content/)')
        parser.add_argument('--model_path', required=True, help='Path to the models.py file (example: app_content/models.py) recommended to have the model in the same directory')
        parser.add_argument('--language', required=False, default='python', help='Language/framework to generate files (default: python)')
        parser.add_argument('--model_language', required=False, default='django', help='Model Mapper (default: django) to map fields from the model')

    def handle(self, *args, **options):
        model_path = options['model_path']
        model_name = options['model']
        base_path = options['basepath']
        language = options['language']
        mapper = options['model_language']


        if not os.path.exists(model_path):
            raise CommandError(f"❌ Model path {model_path} does not exist")
        
        if not os.path.exists(base_path):
            raise CommandError(f"❌ Base path {base_path} does not exist")

        fieldmapper = None
        match mapper:
            case 'django':
                fieldmapper = DjangoFieldMapper()
            # anadir mas mappers
            
            case _:
                raise CommandError(f"❌ Mapper {mapper} is not supported")

        match language:
            case 'python':
                try:
                    generador = GenerateFiles(
                        model_name= model_name,
                        model_path= model_path,
                        base_path= base_path,
                        fieldmapper= fieldmapper,
                        language_to_map="python",
                        entity= PythonEntity(),
                        usecase= PythonUseCase(),
                        repository= PythonRepository(),
                        repository_impl= PythonRepositoryImpl(),
                        view= PythonView(),
                        
                    )
                    self.stdout.write(self.style.SUCCESS(f"🔥 Generating files for {model_name}..."))
                    generador.execute()

                    self.stdout.write(self.style.SUCCESS(f"✨ Files for {model_name} generated successfully!"))

                except Exception as e:
                    tb = traceback.format_exc()
                    raise CommandError(f"Error generating files: {e}\n{tb}")
            case 'flutter':
                try:
                    generador = GenerateFiles(
                        model_name= model_name,
                        model_path= model_path,
                        base_path= base_path,
                        fieldmapper= fieldmapper,
                        language_to_map="flutter",
                        bloc= FlutterBloc(),
                        event= FlutterEvent(),
                        state= FlutterState(),
                        usecase= FlutterUseCase(),
                        entity= FlutterEntity(),
                    )
                    self.stdout.write(self.style.SUCCESS(f"🔥 Generating files for {model_name}..."))
                    generador.execute()

                    self.stdout.write(self.style.SUCCESS(f"✨ Files for {model_name} generated successfully!"))

                except Exception as e:
                    tb = traceback.format_exc()
                    raise CommandError(f"Error generating files: {e}\n{tb}")

            case _:
                raise CommandError(f"❌ Language {language} is not supported")
            
