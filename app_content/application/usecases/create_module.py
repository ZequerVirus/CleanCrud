from app_content.application.interface.solution import Solution
from app_content.infraestructure.generators.Python.solutions.generic import Generic
from app_content.infraestructure.generators.Python.solutions.crm import CRM

class CreateSolution():
    def __init__(self, basepath: str, name:str):
        self.basepath = basepath
        self.name = name

    def execute(self,):
        try:
            obj = None
            match self.name:
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
                    obj = Generic(basepath=self.basepath)
                case _:
                    raise Exception("Sistema no soportado")
                  
        except Exception as e:
            raise Exception(e)
        
    