from app_content.application.interface.module import Module

class ImpExpDataModule(Module):
    def get(self,)->str:
        return (
            f"{self.data_validation()}\n"
            f"{self.export_template()}\n"
            f"{self.data_mapping()}\n"
            f"{self.backup_schedule()}\n"
        )

    def data_mapping(self,):
        return (
            f"class DataMapping(models.Model):\n"
            f"    '''Modelo de mapeo de datos'''\n"
            f"    id = models.AutoField(primary_key=True)\n"
            f"    nombre = models.CharField(max_length=40)\n"
            f"    descripcion = models.TextField(blank=True, null=True)\n"
            f"    source_format = models.CharField(max_length=20, choices=FORMATOS, default='sql')\n"
            f"    target_format = models.CharField(max_length=20, choices=FORMATOS, default='json')\n"
            f"    # Mapeo de campos\n"
            f"    field_mapping = models.JSONField(default=dict, help_text='Mapeo de campos')\n"
            f"    transformations = models.JSONField(default=dict, help_text='Transformaciones')\n"
            f"    # Configuracion\n"
            f"    is_default = models.BooleanField(default=False)\n\n"
        )
    
    def backup_schedule(self,):
        return (
            f"class BackupSchedule(models.Model):\n"
            f"    '''Modelo de programacion de backups'''\n"
            f"    FRECUENCIA= (\n('custom', 'Custom'),\n('diaria', 'Diaria'),\n('semanal', 'Semanal'),\n('mensual', 'Mensual'), \n('anual', 'Anual'))\n"
            f"    id = models.AutoField(primary_key=True)\n"
            f"    nombre = models.CharField(max_length=40)\n"
            f"    descripcion = models.TextField(blank=True, null=True)\n"
            f"    frecuencia = models.CharField(max_length=20, choices=FRECUENCIA, default='diaria')\n"
            f"    cron_expresion = models.CharField(max_length=100, blank=True, null=True, help_text='Expresion cron')\n"
            f"    # Configuracion del backup\n"
            f"    backup_type = models.CharField(max_length=20, choices=[('full','Full'), ('incremental', 'Incremental'), ('partial', 'Partial')], default='full')\n"
            f"    # incluye:\n"
            f"    include_database = models.BooleanField(default=True)\n"
            f"    include_media = models.BooleanField(default=False)\n"
            f"    include_static = models.BooleanField(default=False)\n"
            f"    # configuracion especifica\n"
            f"    models_to_include = models.JSONField(default=list, help_text='Modelos a incluir')\n"
            f"    exclude_tables = models.JSONField(default=list, help_text='Tablas a excluir')\n"
            f"    # retencion\n"
            f"    keep_last_n= models.IntegerField(default=10, help_text='Numero de backups a mantener')\n"
            f"    retention_days= models.IntegerField(default=30, help_text='Dias de retencion')\n"
            f"    # estado\n"
            f"    is_active = models.BooleanField(default=True)\n"
            f"    last_run = models.DateTimeField(null=True, blank=True)\n"
            f"    next_run = models.DateTimeField(null=True, blank=True)\n"
            f"    # Configuracion de notificaciones\n"
            f"    notify_on_success = models.BooleanField(default=True)\n"
            f"    notify_on_failure = models.BooleanField(null=True, blank=True)\n"
            f"    notifications_emails = models.JSONField(default=list, help_text='Correos de notificacion')\n\n"
        )
    
    def data_validation(self,):
        return (
            f"class DataValidationRule(models.Model):\n"
            f"    ''' Modelo de reglas de validacion de datos'''\n"
            f"    RULE_TYPE = [('required','Campo requerido'), ('unique','Valor unico'), ('format', 'Formato Especifico'), ('range', 'Rando de valores'), ('custom','Validacion personalizada')]\n"
            f"    id = models.AutoField(primary_key=True)\n"
            f"    nombre = models.CharField(max_length=40)\n"
            f"    descripcion = models.CharField(max_length=100, blank=True, null=True)\n"
            f"    rule_type = models.CharField(max_length=20, choices=RULE_TYPE, default='required')\n"
            f"    nombre_modelo = models.CharField(max_length=40, help_text='Nombre del modelo Django')\n"
            f"    nombre_campo = models.CharField(max_length=40, help_text='Nombre del campo del modelo Django')\n"
            f"    # Configuracion de la regla\n"
            f"    rule_config = models.JSONField(default=dict, help_text='Configuracion especifica de la regla')\n"
            f"    error_message = models.CharField(max_length=100, help_text='Mensaje de error personalizado')\n"
            f"    # Aplicacion\n"
            f"    is_active= models.BooleanField(default=True)\n"
            f"    apply_on_import = models.BooleanField(default=True)\n"
            f"    apply_on_export = models.BooleanField(default=False)\n\n"
        )
    
    def export_template(self,):
        return (
            f"class ExportTemplate(models.Models):\n"
            f"    '''Plantillas predefinidas para exportaciones'''\n"
            f"    FORMATOS = (('json', 'JSON'),\n('csv', 'CSV'),\n('xml', 'XML'),\n('sql', 'SQL'),\n('sql', 'SQL'),\n('excel','Excel'),\n('zip', 'Zip'))\n"
            f"    id = models.AutoField(primary_key=True)\n"
            f"    nombre= models.CharField(max_length=255)\n"
            f"    description = models.TextField(blank=True, null=True)\n"
            f"    # Configuracion de exportacion\n"
            f"    dataformat = models.CharField(max_length=20, choices=FORMATOS, default='json')\n"
            f"    # Campos a incluir\n"
            f"    included_models = models.JSONField(default=list, help_text='Modelos a incluir')\n"
            f"    included_fields = models.JSONField(default=dict, help_text='Campos a incluir')\n"
            f"    # Orden y filtros\n"
            f"    ordering = models.JSONField(default=dict, help_text='Orden de los campos')\n"
            f"    default_filters = models.JSONField(default=dict, help_text='Filtros por defecto')\n"
            f"    # Configuracion adicional\n"
            f"    options = models.JSONField(default=dict, help_text='Opciones especificas del formato')\n"
            f"    is_public = models.BooleanField(default=False, help_text='Disponible para todos los usuarios')\n\n"
        )

    def import_export_data(self,):    
        return (
            f"class ImportExportData(models.Model):\n"
            f"    '''Modelo de importacion y exportacion de datos'''\n"
            f"    STATUS = (\n('pendiente',\n'Pendiente'),\n('procesando',\n'Procesando'),\n('finalizado',\n'Finalizado'),\n('fallido', 'Fallido'),\n('cancelado', 'Cancelado'))\n"
            f"    OPERACIONES = (('importar', 'Importar'),\n('exportar', 'Exportar'),\n('backup', 'Backup'),\n('restore', 'Restore'),\n('sync', 'Sync'))\n"
            f"    FORMATOS = (('json', 'JSON'),\n('csv', 'CSV'),\n('xml', 'XML'),\n('sql', 'SQL'),\n('sql', 'SQL'),\n('excel','Excel'),\n('zip', 'Zip'))\n"
            f"    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)\n"
            f"    nombre = models.CharField(max_length=40, help_text='Nombre del archivo')\n"
            f"    operacion = models.CharField(max_length=20, choices=OPERACIONES, default='importar')\n"
            f"    formato = models.CharField(max_length=20, choices=FORMATOS, default='json')\n"
            f"    status = models.CharField(max_length=20, choices=STATUS, default='pendiente')\n"
            f"    file = models.FileField(upload_to='files/', storage=DefaultStorage(), null=True, blank=True)\n"
            f"    file_size= models.BigIntegerField(default=0, help_text='Tamaño del archivo en bytes')\n"
            f"    checksum = models.CharField(max_length=64, help_text='sha-256 del archivo', null=True, blank=True)\n\n"       
        )