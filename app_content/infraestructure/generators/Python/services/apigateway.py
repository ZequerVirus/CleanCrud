# from app_content.application.interface.services.apigateway import APIGateway
# import os

# class APIGatewayService(APIGateway):
#     def execute(self,):
#         path = os.path.join("application", "services")
#         os.makedirs(os.path.dirname(path), exist_ok=True)
#         file_path = os.path.join(path, "gateway.py")
#         try:
#             with open(file_path, "w") as f:
#                 f.write(f"{self.interface_imports()}\n")
#                 f.write(f"    pass\n")
#         except Exception as e:
#             raise Exception(e)
        

#     def interface_imports(self,)->str:
#         return (
#             f"from abc import ABC, abstractmethod\n"
#         )