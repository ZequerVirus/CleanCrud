from app_content.application.interface.module import Module

class NotificationModule(Module):
    def get(self)->str:
        return (
            f""
        )
    
    def notification_channel(self,):
        return (
            f"class NotificationChannel(models.Model):\n"
            f"    '''Modelo de canales de notificaciones'''\n"
            f"    id = models.AutoField(primary_key=True)\n"
            f"    nombre = models.CharField(max_length=20, unique=True, choices=[('email', 'Email'), ('sms', 'SMS'), ('push', 'Push'), ('web', 'Web'), ('in-app', 'In-App')], verbose_name='Nombre del canal')\n"
            f"    enabled = models.BooleanField(default=True)\n"
            f"    descripcion = models.TextField(blank=True, null=True)\n\n"
        )
    
    def notification_category(self,):
        return (
            f"class NotificationCategory(models.Model):\n"
            f"    '''Modelo de categorias de notificaciones'''\n"
            f"    id = models.AutoField(primary_key=True)\n"
            f"    nombre = models.CharField(max_length=40, unique=True, verbose_name='Nombre de la categoria')\n"
            f"    code = models.SlugField(max_length=40, unique=True, verbose_name='Codigo de la categoria')\n"
            f"    descripcion = models.TextField(blank=True, null=True)\n"
            f"    # apariencia\n"
            f"    icon = models.CharField(max_length=100, blank=True, null=True, verbose_name='Icono', help_text='url de imagen')\n"
            f"    # configuracion\n"
            f"    is_active = models.BooleanField(default=True)\n"
            f"    default_channel = models.ForeignKey(NotificationChannel, on_delete=models.PROTECT, verbose_name='Canal por defecto')\n"
            f"    default_priority = models.IntegerField(choices=[('low','Baja'), ('medium','Media'), ('high','Alta')], default='medium')\n"
            f"    is_system = models.BooleanField(default=False)\n"
            f"    require_confirmation = models.BooleanField(default=False)\n\n"
        )

    def notification_template(self,):
        return (
            f"class NotificationTemplate(models.Model):\n"
            f"    '''Modelo de plantillas de notificaciones'''\n"
            f"    id = models.AutoField(primary_key=True)\n"
            f"    nombre = models.CharField(max_length=40, unique=True, verbose_name='Nombre de la plantilla')\n"
            f"    code = models.SlugField(max_length=40, unique=True, verbose_name='Codigo de la plantilla')\n"
            f"    category = models.ForeignKey(NotificationCategory, on_delete=models.PROTECT, verbose_name='Categoria')\n"
            f"    # contenido por canal\n"
            f"    subject = models.CharField(max_length=255, blank=True, help_text='Asunto para email')\n"
            f"    title = models.CharField(max_length=255, blank=True, help_text='Titulo para notificaciones push/in-app')\n"
            f"    message = models.TextField(help_text='Cuerpo de la notificacion')\n"
            f"    # Plantillas especificas\n"
            f"    email_template = models.TextField(blank=True, null=True, help_text='Plantilla de email')\n"
            f"    sms_template = models.TextField(blank=True, null=True, help_text='Plantilla de SMS')\n"
            f"    push_template = models.JSONField(default=dict, blank=True, null=True, help_text='Plantilla de Push')\n"
            

        )