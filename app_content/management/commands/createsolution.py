from django.core.management.base import BaseCommand, CommandError
from app_content.application.usecases.create_module import CreateSolution
import os

class Command(BaseCommand):
    help = '''Create a complete system using clean architecture
    '''
    # opciones disponibles
    SYSTEMS = [
        "CRM",
        "ERP",
        "SCM",
        "GENERIC",
        # anadir las otras opciones que tengo
    ]

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Seleccione el sistema que desea crear:\n"))
        # mostrar la lista numerada
        for i, system in enumerate(self.SYSTEMS, start=1):
            self.stdout.write(f"{i}. {system}\n")
        self.stdout.write("\n")
        # leer opcion ingresada
        opcion = input("Ingrese el numero del sistema: ").strip()
        # validar
        if not opcion.isdigit():
            raise CommandError("Debe ingresar un numero")
        opcion = int(opcion)
        if opcion < 1 or opcion > len(self.SYSTEMS):
            raise CommandError("Debe ingresar un numero entre 1 y {}".format(len(self.SYSTEMS)))
        system = self.SYSTEMS[opcion - 1]
        self.stdout.write(self.style.SUCCESS("Sistema seleccionado: {}".format(system)))
        self.stdout.write("\n")
        self.stdout.write(self.style.SUCCESS("Ingrese la direccion base del proyecto (ejm: app_content/):\n"))
        
        basepath = input("Ingrese la direccion base del proyecto: ").strip()
        basepath = basepath[:-1] if basepath.endswith("/") else basepath
        self.stdout.write(self.style.SUCCESS("Direccion base del proyecto: {}/".format(basepath)))
        # validar si la direccion existe
        if not os.path.exists(basepath):
            raise CommandError("La direccion base {} no existe".format(basepath))
        try:
            usecase = CreateSolution(basepath=basepath, name=system,)
            self.stdout.write(self.style.SUCCESS("Creando sistema..."))
            usecase.execute()
            self.stdout.write(self.style.SUCCESS("Sistema creado con exito"))
        except Exception as e:
            raise CommandError("Error al crear el sistema: {}".format(e))