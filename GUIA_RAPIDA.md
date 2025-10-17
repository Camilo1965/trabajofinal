# 🚀 Guía Rápida - Sistema de Gestión

## Instalación en 3 Pasos

### 1. Clonar e Instalar
```bash
git clone https://github.com/Camilo1965/trabajofinal.git
cd trabajofinal
pip install -r requirements.txt
```

### 2. Generar Diagramas
```bash
# Instalar Graphviz (si no está instalado)
# Ubuntu/Debian: sudo apt-get install graphviz
# macOS: brew install graphviz
# Windows: descarga desde graphviz.org

# Generar todos los diagramas
python diagrams/generate_diagrams.py
python database/generate_er_diagram.py
```

### 3. Ejecutar la Aplicación
```bash
cd src
python main.py
```

## 📁 Navegación Rápida

### Código Fuente
- **Modelos**: [`src/models/`](src/models/) - Clases de dominio (User, Product, Payment)
- **Controladores**: [`src/controllers/`](src/controllers/) - Lógica de negocio
- **Repositorios**: [`src/repositories/`](src/repositories/) - Acceso a datos
- **Vistas**: [`src/views/`](src/views/) - Interfaz de usuario
- **Principal**: [`src/main.py`](src/main.py) - Aplicación principal

### Documentación
- **README Principal**: [`README.md`](README.md) - Documentación completa
- **Arquitectura**: [`docs/arquitectura.md`](docs/arquitectura.md) - Detalles de arquitectura MVC
- **Interfaces**: [`docs/interfaces.md`](docs/interfaces.md) - Contratos entre componentes
- **Resumen**: [`docs/resumen.md`](docs/resumen.md) - Resumen ejecutivo y estadísticas

### Diagramas
- **Usuario**: [`diagrams/user_class_diagram.png`](diagrams/user_class_diagram.png)
- **Producto**: [`diagrams/product_class_diagram.png`](diagrams/product_class_diagram.png)
- **Pago**: [`diagrams/payment_class_diagram.png`](diagrams/payment_class_diagram.png)
- **Componentes**: [`diagrams/component_diagram.png`](diagrams/component_diagram.png)
- **Despliegue**: [`diagrams/deployment_diagram.png`](diagrams/deployment_diagram.png)
- **Secuencia**: [`diagrams/sequence_diagram.png`](diagrams/sequence_diagram.png)
- **ER**: [`database/er_diagram.png`](database/er_diagram.png)

### Base de Datos
- **Esquema SQL**: [`database/schema.sql`](database/schema.sql) - Script completo de creación

## 💻 Ejemplos de Uso Rápido

### Ejemplo 1: Crear Usuario
```python
import sys
sys.path.insert(0, 'src')

from models.user import UserRole
from controllers.user_controller import UserController
from repositories.user_repository import UserRepository

repo = UserRepository()
controller = UserController(repo)

user = controller.register_user(
    username="usuario1",
    email="usuario@example.com",
    password="password123",
    role=UserRole.CLIENT,
    full_name="Usuario Ejemplo"
)

print(f"Usuario creado: {user}")
```

### Ejemplo 2: Crear Producto
```python
from models.product import ProductCategory
from controllers.product_controller import ProductController
from repositories.product_repository import ProductRepository

repo = ProductRepository()
controller = ProductController(repo)

product = controller.create_product(
    name="Laptop HP",
    description="Laptop HP Core i5, 8GB RAM",
    price=799.99,
    category=ProductCategory.ELECTRONICS,
    stock_quantity=10,
    sku="LAP-HP-001"
)

print(f"Producto creado: {product}")
```

### Ejemplo 3: Procesar Pago
```python
from models.payment import PaymentMethod
from controllers.payment_controller import PaymentController
from repositories.payment_repository import PaymentRepository

repo = PaymentRepository()
controller = PaymentController(repo)

# Crear pago
payment = controller.create_payment(
    order_id=1,
    user_id=1,
    amount=799.99,
    payment_method=PaymentMethod.CREDIT_CARD
)

# Procesar pago
success = controller.process_payment(payment.payment_id)
print(f"Pago procesado: {success}")
```

## 🔧 Comandos Útiles

### Verificar Importaciones
```bash
cd trabajofinal
python -c "import sys; sys.path.insert(0, 'src'); from models import *; from controllers import *; print('✓ OK')"
```

### Ejecutar Prueba Completa
```bash
cd trabajofinal
python -c "
import sys
sys.path.insert(0, 'src')
from controllers.user_controller import UserController
from repositories.user_repository import UserRepository
from models.user import UserRole

repo = UserRepository()
ctrl = UserController(repo)
user = ctrl.register_user('test', 'test@test.com', 'pass', UserRole.CLIENT, 'Test')
print(f'✓ Sistema funcional: {user}')
"
```

### Regenerar Diagramas
```bash
python diagrams/generate_diagrams.py
python database/generate_er_diagram.py
```

## 📚 Documentación Adicional

### Para Desarrolladores
1. Lee [`docs/arquitectura.md`](docs/arquitectura.md) para entender la arquitectura MVC
2. Revisa [`docs/interfaces.md`](docs/interfaces.md) para conocer los contratos
3. Examina el código en [`src/`](src/) para ver la implementación

### Para Usuarios
1. Sigue las instrucciones en [`README.md`](README.md)
2. Ejecuta [`src/main.py`](src/main.py) para la interfaz de consola
3. Consulta los diagramas en [`diagrams/`](diagrams/) para visualizar el sistema

### Para Evaluadores
1. [`docs/resumen.md`](docs/resumen.md) - Resumen ejecutivo con estadísticas
2. [`database/schema.sql`](database/schema.sql) - Esquema de base de datos completo
3. Diagramas en [`diagrams/`](diagrams/) y [`database/`](database/)

## 🎯 Características Principales

- ✅ **MVC**: Arquitectura Modelo-Vista-Controlador
- ✅ **3 Módulos**: Usuarios, Productos, Pagos
- ✅ **7 Diagramas**: Clases, Componentes, Despliegue, Secuencia, ER
- ✅ **Base de Datos**: Esquema SQL completo con 10 tablas
- ✅ **Documentación**: 1,452 líneas de docs
- ✅ **Código**: 1,789 líneas de Python
- ✅ **Probado**: Sistema completamente funcional

## 🚨 Solución de Problemas

### Error: "ModuleNotFoundError"
```bash
# Asegúrate de estar en el directorio correcto
cd trabajofinal
# Agrega src/ al path de Python
python -c "import sys; sys.path.insert(0, 'src'); import models"
```

### Error: "Graphviz not found"
```bash
# Ubuntu/Debian
sudo apt-get install graphviz

# macOS
brew install graphviz

# Windows
# Descarga e instala desde: https://graphviz.org/download/
```

### Los diagramas no se generan
```bash
# Verifica que Graphviz esté instalado
dot -V

# Reinstala la librería Python
pip install --upgrade graphviz
```

## 📞 Soporte

Para preguntas o problemas:
1. Revisa la documentación en [`docs/`](docs/)
2. Consulta el [`README.md`](README.md)
3. Abre un issue en el repositorio GitHub

---

**¡Disfruta del Sistema de Gestión!** 🎉
