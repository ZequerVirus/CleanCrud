from app_content.application.interface.module import Module

class UserRolesModule(Module):
    def get(self,)->str:
         '''Retorna todos los modulos'''
         return (
            f"{self.user()}\n"
            f"{self.role()}\n"
            f"{self.permission()}\n"
         )

    def role(self):
        '''Model de roles'''
        return (
            f"class Role(models.Model):\n"
            f"    '''Modelo de roles'''\n"
            f"    id = models.AutoField(primary_key=True)\n"
            f"    nombre = models.CharField(max_length=40)\n"
            f"    descripcion = models.CharField(max_length=100, blank=True, null=True)\n\n"

            f"class UserRole(models.Model):\n"
            f"    '''Modelo de relacion de usuarios y roles\n'''"
            f"    id = models.AutoField(primary_key=True)\n"
            f"    user = models.ForeignKey(User, on_delete=models.CASCADE)\n"
            f"    role = models.ForeignKey(Role, on_delete=models.CASCADE)\n\n"
        )
    
    def permission(self,):
         '''Modelo de permisos'''
         return (
            f"class Permission(models.Model):\n"
            f"    '''Modelo de permisos'''\n"
            f"    id = models.AutoField(primary_key=True)\n"
            f"    nombre = models.CharField(max_length=40)\n"
            f"    descripcion = models.CharField(max_length=100, blank=True, null=True)\n\n"

            f"class RolePermission(models.Model):\n"
            f"    '''Modelo de relacion de roles y permisos'''\n"
            f"    id = models.AutoField(primary_key=True)\n"
            f"    role = models.ForeignKey(Role, on_delete=models.CASCADE)\n"
            f"    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)\n\n"
         )

    def user(self,):
            '''Model del modulo de usuarios'''
            return (
                f"class User(models.Model):\n"
                f"    '''Modelo de usuarios genericos sin abstractuser'''\n"
                f"    GENEROS = (('M', 'Masculino'), ('F', 'Femenino'))\n"
                f"    id = models.AutoField(primary_key=True)\n"
                f"    nombre = models.CharField(max_length=40)\n"
                f"    apellido = models.CharField(max_length=40)\n"
                f"    genero = models.CharField(max_length=1, choices=GENEROS, default='M')\n"
                f"    fecha_nacimiento = models.DateField()\n"
                f"    telefono = models.CharField(max_length=20, blank=True, null=True)\n"
                f"    ci = models.CharField(max_length=20)\n\n"
            )