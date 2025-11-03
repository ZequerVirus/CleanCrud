from app_content.domain.entities.model_entity import ModelEntity
import os

class ReactView:
    def __init__(self):
        pass

    def execute(self, model: ModelEntity, basepath: str):
        '''Genera la vista React para el modelo dado'''
        nombre = f"{model.nombre[0].upper()}{model.nombre[1:]}"
        path = os.path.join(basepath, "presentation", "views", f"{nombre}")
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, f"{model.nombre}_view.tsx")
        try:
            with open(filepath, "w") as f:
                f.write(self.__imports(model=model, nombre=nombre))
                f.write(self.__component(model=model, nombre=nombre))
        except Exception as e:
            raise Exception(e)
        
    def __imports(self, model: ModelEntity, nombre: str)->str:
        return (
            f"import {{ {nombre}Entity }} from '../../../domain/entities/{model.nombre}_entity';\n"
            f"import {nombre}Form from './{nombre}_form';\n"
            f"import Modal from '../../components/Modal';\n"
            f"import SearchBar from '../../components/SearchBar';\n"
            f"import {nombre}Table from './{model.nombre}_table';\n"
            f"import {{ useState }} from 'react';\n"
            f"import {{ {nombre}Hook }} from './{model.nombre}_hook';\n\n"
        )

    def __component(self, model: ModelEntity, nombre: str)->str:
        return (
            f"function {nombre}() {{\n"
            f"  const {{\n"
            f"    loading,\n"
            f"    message,\n"
            f"    filtered,\n"
            f"    handleSearch,\n"
            f"    handleCreate,\n"
            f"    handleUpdate,\n"
            f"    handleDelete,\n"
            f"  }} = {nombre}Hook();\n\n"
            f"  const [showModal, setShowModal] = useState<boolean>(false);\n"
            f"  const [editingItem, setEditingItem] = useState<{nombre}Entity | undefined>(undefined);\n\n"
            f"  if (loading) {{\n"
            f"    return (\n"
            f"      <div>\n"
            f"        {{showModal && (\n"
            f"          <Modal title=\"\" onClose={{() => setShowModal(false)}}>\n"
            f"            <h1 className=\"text-center mb-3\">\n"
            f"              <i className=\"bi bi-hourglass-split\"></i> Cargando...\n"
            f"            </h1>\n"
            f"          </Modal>\n"
            f"        )}}\n"
            f"      </div>\n"
            f"    );\n"
            f"  }}\n\n"
            f"  return (\n"
            f"    <div className=\"container py-5\">\n"
            f"      <h1 className=\"text-center mb-3\">Gestión de {nombre}</h1>\n\n"
            f"      <div className=\"mb-4\">\n"
            f"        <SearchBar onSearch={{(term) => handleSearch(term)}} />\n"
            f"      </div>\n\n"
            f"      <div className=\"d-flex justify-content-end mb-3 flex-wrap\">\n"
            f"        <button\n"
            f"          className=\"btn btn-primary mb-2\"\n"
            f"          onClick={{() => {{\n"
            f"            setEditingItem(undefined);\n"
            f"            setShowModal(true);\n"
            f"          }}}}\n"
            f"        >\n"
            f"          <i className=\"bi bi-plus-circle me-2\"></i>\n"
            f"          Crear {nombre}\n"
            f"        </button>\n"
            f"      </div>\n\n"
            f"      <div className=\"container py-5\">\n"
            f"        <{nombre}Table\n"
            f"          {nombre}={{filtered}}\n"
            f"          editItem={{(item) => {{ setShowModal(true); setEditingItem(item); }}}}\n"
            f"          deleteItem={{(item) => {{ handleDelete(item.id?.toString() ?? ''); setShowModal(false); }}}}\n"
            f"        />\n"
            f"      </div>\n\n"
            f"      {{showModal && (\n"
            f"        <Modal\n"
            f"          title={{editingItem ? `Editar {nombre}` : `Crear {nombre}`}}\n"
            f"          onClose={{() => setShowModal(false)}}\n"
            f"        >\n"
            f"          <{nombre}Form\n"
            f"            initial{nombre}={{editingItem}}\n"
            f"            onSubmit={{(item) => {{\n"
            f"              editingItem\n"
            f"                ? handleUpdate(item.id?.toString() ?? '', item)\n"
            f"                : handleCreate(item);\n"
            f"              setShowModal(false);\n"
            f"            }}}}\n"
            f"            onCancel={{() => setShowModal(false)}}\n"
            f"          />\n"
            f"        </Modal>\n"
            f"      )}}\n"
            f"    </div>\n"
            f"  );\n"
            f"}}\n\n"
            f"export default {nombre};\n"
        )
