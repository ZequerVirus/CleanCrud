from django.core.management.base import BaseCommand, CommandError
from app_content.infraestructure.generators.Python.modules.generic import Generic
from app_content.application.usecases.create_module import CreateModule
import os
from app_content.application.interface.module import Module
from app_content.infraestructure.generators.Python.modules.crm import CRM

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
            obj = None
            match system:
                case "CRM":
                    '''Customer Relationship Management
                    Sistema de gestion de relaciones con clientes.
                    Permite administrar:
                    - Informacion de clientes
                    - Ventas y prospectos
                    - Comunicaciones (email, llamadas, reuniones)
                    - Atencion al cliente
                    - Marketing y seguimiento comercial
                    '''
                    obj = CRM()

                case "ERP":
                    '''Enterprise Resource Planning
                    Sistema de planificacion de recursos empresariales.
                    Integra y centraliza todos los procesos internos de una empresa, tales como:
                    - Finanzas y contabilidad
                    - Inventarios
                    - Compras
                    - Recursos humanos
                    - Produccion
                    - Logistica
                    '''
                    pass
                case "SCM":
                    '''Supply Chain Management
                    Gestion de la cadena de suministro.
                    Traza y optimiza el recorrido completo de los productos
                    - Proveedores
                    - Produccion
                    - Almacenamiento
                    - Transporte y distribucion
                    - Inventarios
                    '''
                    pass
                case "BI":
                    '''Business Intelligence
                    Inteligencia de negocio.
                    Conjunto de herramientas y tecnicas para transformar datos en informacion
                    util para la toma de decisiones
                    Incluye:
                    - Dashboard
                    - Reportes
                    - Analisis de datos historicos
                    - Indicadores KPI
                    - Data Warehouses
                    '''
                    pass
                case "BPM":
                    '''Business Process Management
                    Gestion de procesos de negocio.
                    Disciplina que analiza, disena y optimiza los procesos operativos de una 
                    empresa
                    Incluye:
                    - Modelado de procesos (BPMN)
                    - Automatizacion con flujos de trabajo
                    - Monitoreo
                    '''
                    pass
                case "MES":
                    '''Manifacturing Execution System
                    Sistema usados en plantas de produccion para controlar:
                    - Ordenes de fabricacion
                    - Maquinaria
                    - Control de calidad
                    - Rendimiento
                    - Trazabilidad
                    '''
                    pass
                case "WMS":
                    '''Warehouse Management System
                    Sistema de gestion de almacenes
                    - Ubicaciones
                    - Picking
                    - Historial de movimiento
                    - Inventario en tiempo real
                    - Optimizacion del espacio
                    '''
                    pass
                case "POS":
                    '''Point of sale
                    Sistema de punto de venta:
                    - Ventas en tienda
                    - Caja registrados
                    - Gestion de inventarios
                    - Tickets y facturacion
                    '''
                    pass
                case "HCM/HRM":
                    '''Human Capital Management / Human Resource
                    Gestion de Recursos Humanos:
                    - Nomina
                    - Reclutamiento
                    - Capacitacion
                    - Evaluacion de desempeno
                    '''
                    pass
                case "CMS":
                    '''Content management system
                    Sistema de gestion de contenido:
                    - Paginas web
                    - Blog
                    - Ecommerce
                    - Plantillas
                    '''
                    pass
                case "generic":
                    '''Generic
                    Modulos que pueden pertenecer a cualquier sistema:
                    - usuarios y roles
                    - auditoria
                    - notificaciones
                    - integraciones
                    - reportes
                    - multiempresa
                    - multisucursal
                    - configuraciones
                    - logs
                    - auth
                    - importacion y exportacion de datos
                    '''
                    obj = Generic()
                case _:
                    raise CommandError("Sistema no valido")
            if obj is not None and basepath is not None and isinstance(obj, Module):
                usecase = CreateModule(basepath=basepath, name=system, module=obj)
                self.stdout.write(self.style.SUCCESS("Creando sistema..."))
                usecase.execute()
                self.stdout.write(self.style.SUCCESS("Sistema creado con exito"))
            else:
                raise CommandError("Error al crear el sistema")
        except Exception as e:
            raise CommandError("Error al crear el sistema: {}".format(e))