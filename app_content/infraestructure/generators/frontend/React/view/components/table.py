import os
from app_content.application.interface.generator import Generator

class ReactTable(Generator):
    def execute(self, ):
        ''' Generate the files for the model '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        path = os.path.join(self.basepath, "presentation", "views", f"{nombre}")
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, f"{self.model.nombre}_table.tsx")
        try:
            with open(filepath, "w") as f:
                f.write(f"{self.__imports()}\n")
                f.write(f"{self.__tableprops()}\n")
                f.write(f"{self.__table()}\n")
                f.write(f"export default {nombre}Table;\n")
        except Exception as e:
            raise Exception(e)
        
    def __imports(self, )->str:
        ''' Generate the imports for the file '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"import {{ useState }} from 'react';\n"
            f"import type {{ {nombre}Entity }} from '../../../domain/entities/{self.model.nombre}_entity';\n"
        )
    
    def __tableprops(self, )->str:
        ''' Generate the interface for the file '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"type {nombre}TableProps = {{\n"
            f"    {self.model.nombre}: {self.model.nombre}Entity[];\n"
            f"    editItem: ({self.model.nombre}: {self.model.nombre}Entity) => void;\n"
            f"    deleteItem: ({self.model.nombre}: {self.model.nombre}Entity) => void;\n"
            f"}}\n"
        )
    
    def __table(self,)->str:
        ''' Generate the interface for the file '''
        nombre = f"{self.model.nombre[0].capitalize()}{self.model.nombre[1:]}"
        return (
            f"function {nombre}Table({{ {self.model.nombre}, editItem, deleteItem }}: {nombre}TableProps) {{\n"
            f"  const [currentPage, setCurrentPage] = useState(1);\n"
            f"  const [itemsPerPage] = useState(10);\n"
            f"  const totalPages = Math.ceil({self.model.nombre}.length / itemsPerPage);\n"
            f"  const startIndex = (currentPage - 1) * itemsPerPage;\n"
            f"  const visibleItems = {self.model.nombre}.slice(startIndex, startIndex + itemsPerPage);\n"
            f"  const handlePrev = () => setCurrentPage((prev)=> Math.max(prev-1, 1));\n"
            f"  const handleNext = () => setCurrentPage((prev) => Math.min(prev + 1, totalPages));\n"
            f"  return (\n"
            f"  <div className=\"table-responsive\">\n"
            f"      <table className=\"table table-striped align-middle\">\n"
            f"        <thead className=\"table-dark\">\n"
            f"          <tr>\n"
            f"{('\n').join([f'          <th>{field.nombre}</th>' for field in self.model.fields])}\n"
            f"          </tr>\n"
            f"        </thead>\n"
            f"        <tbody>\n"
            f"          {{visibleItems.map((item) => (\n"
            f"            <tr key={{item.id}}>\n"
            f"{('\n').join([f"              <td>{{item.{field.nombre}}}</td>" for field in self.model.fields])}\n"
            f"              <td className=\"text-end\">\n"
            f"                <button className=\"btn btn-sm btn-outline-warning me-2\" onClick={{() => editItem(item)}}>\n"
            f"                  <i className=\"bi bi-pencil-square\"></i> Editar\n"
            f"                </button>\n"
            f"                <button className=\"btn btn-sm btn-outline-danger\" onClick={{() => deleteItem(item)}}>\n"
            f"                  <i className=\"bi bi-trash\"></i> Eliminar\n"
            f"                </button>\n"
            f"              </td>\n"
            f"            </tr>\n"
            f"          ))}}\n"
            f"        </tbody>\n"
            f"      </table>\n"
            f"      \n"
            f"      {{/* 🔹 Paginación */}}\n"
            f"      <nav>\n"
            f"        <ul className=\"pagination justify-content-center\">\n"
            f"          <li className={{`page-item ${{currentPage === 1 ? \"disabled\" : \"\"}}`}}>\n"
            f"            <button className=\"page-link\" onClick={{handlePrev}}>\n"
            f"              Anterior\n"
            f"            </button>\n"
            f"          </li>\n"
            f"      \n"
            f"          {{Array.from({{ length: totalPages }}, (_, i) => (\n"
            f"            <li\n"
            f"              key={{i}}\n"
            f"              className={{`page-item ${{currentPage === i + 1 ? \"active\" : \"\"}}`}}\n"
            f"            >\n"
            f"              <button className=\"page-link\" onClick={{() => setCurrentPage(i + 1)}}>\n"
            f"                {{i + 1}}\n"
            f"              </button>\n"
            f"            </li>\n"
            f"          ))}}\n"
            f"      \n"
            f"          <li className={{`page-item ${{currentPage === totalPages ? \"disabled\" : \"\"}}`}}>\n"
            f"            <button className=\"page-link\" onClick={{handleNext}}>\n"
            f"              Siguiente\n"
            f"            </button>\n"
            f"          </li>\n"
            f"        </ul>\n"
            f"      </nav>\n"
            f"      \n"
            f"      {{/* 🔹 Info de paginación */}}\n"
            f"      <div className=\"text-center text-muted small mt-2\">\n"
            f"        Página {{currentPage}} de {{totalPages}} — Mostrando {{visibleItems.length}} de {{{nombre}.length}} registros\n"
            f"      </div>\n"
            f"   </div>\n"
            f");\n"
            f"}}\n"
        )