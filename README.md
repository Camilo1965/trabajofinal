# Sistema de Gestión

Sistema integral de gestión empresarial desarrollado en Python con arquitectura Modelo-Vista-Controlador (MVC). Incluye módulos de gestión de usuarios, productos y procesamiento de pagos.

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Arquitectura](#arquitectura)
- [Tecnologías](#tecnologías)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Diagramas](#diagramas)
- [Base de Datos](#base-de-datos)
- [Documentación](#documentación)
- [Contribución](#contribución)

## 📝 Descripción

El Sistema de Gestión es una aplicación empresarial que proporciona funcionalidades completas para:
- **Gestión de Usuarios**: Registro, autenticación, roles y permisos
- **Gestión de Productos**: Catálogo, inventario, categorías y reseñas
- **Procesamiento de Pagos**: Transacciones, múltiples métodos de pago, reembolsos

El sistema está diseñado con una arquitectura escalable y mantenible, siguiendo principios SOLID y patrones de diseño establecidos.

## ✨ Características

### Módulo de Usuarios
- ✅ Registro y autenticación de usuarios
- ✅ Sistema de roles (Admin, Manager, Employee, Client)
- ✅ Gestión de permisos granulares
- ✅ Perfiles de usuario con información extendida
- ✅ Activación/desactivación de cuentas

### Módulo de Productos
- ✅ Catálogo completo de productos
- ✅ Gestión de inventario en tiempo real
- ✅ Categorización flexible
- ✅ Sistema de reseñas y calificaciones
- ✅ Gestión de proveedores
- ✅ Control de disponibilidad

### Módulo de Pagos
- ✅ Múltiples métodos de pago (Tarjeta, PayPal, Transferencia, Efectivo)
- ✅ Estados de pago (Pendiente, Procesando, Completado, Fallido, Reembolsado)
- ✅ Integración con gateways de pago externos
- ✅ Sistema de órdenes y items
- ✅ Procesamiento de reembolsos

## 🏗️ Arquitectura

El sistema implementa el patrón **Modelo-Vista-Controlador (MVC)** con las siguientes capas:

```
┌─────────────────────────────────────┐
│         CAPA DE VISTA               │
│    (Interfaz de Usuario)            │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│      CAPA DE CONTROLADORES          │
│  (Lógica de Negocio)                │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│       CAPA DE MODELOS               │
│  (Entidades de Dominio)             │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│     CAPA DE REPOSITORIOS            │
│  (Acceso a Datos)                   │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│        BASE DE DATOS                │
│     (SQLite/MySQL)                  │
└─────────────────────────────────────┘
```

### Patrones de Diseño Utilizados

- **MVC**: Separación de responsabilidades
- **Repository**: Abstracción de persistencia
- **Strategy**: Métodos de pago intercambiables
- **State**: Estados de pago y orden
- **Factory Method**: Creación de objetos

Para más detalles, consulta [docs/arquitectura.md](docs/arquitectura.md).

## 🛠️ Tecnologías

- **Python**: 3.11+
- **Graphviz**: 0.20.1+ (generación de diagramas UML)
- **SQLite**: Base de datos (desarrollo)
- **MySQL/PostgreSQL**: Soportado para producción

### Herramientas de Desarrollo
- **pylint**: Análisis estático de código
- **Git**: Control de versiones

## 📁 Estructura del Proyecto

```
trabajofinal/
├── src/                          # Código fuente
│   ├── models/                   # Modelos de dominio
│   │   ├── user.py              # Gestión de usuarios
│   │   ├── product.py           # Gestión de productos
│   │   └── payment.py           # Procesamiento de pagos
│   ├── controllers/             # Controladores
│   │   ├── user_controller.py
│   │   ├── product_controller.py
│   │   └── payment_controller.py
│   ├── repositories/            # Capa de persistencia
│   │   ├── user_repository.py
│   │   ├── product_repository.py
│   │   └── payment_repository.py
│   ├── views/                   # Interfaces de usuario
│   │   └── console_view.py
│   └── main.py                  # Aplicación principal
├── diagrams/                     # Diagramas UML
│   ├── generate_diagrams.py    # Script de generación
│   ├── user_class_diagram.png
│   ├── product_class_diagram.png
│   ├── payment_class_diagram.png
│   ├── component_diagram.png
│   ├── deployment_diagram.png
│   └── sequence_diagram.png
├── database/                     # Scripts de base de datos
│   ├── schema.sql               # Esquema SQL
│   ├── generate_er_diagram.py  # Generador de diagrama ER
│   └── er_diagram.png
├── docs/                         # Documentación
│   ├── arquitectura.md          # Documentación de arquitectura
│   └── interfaces.md            # Documentación de interfaces
├── requirements.txt              # Dependencias Python
└── README.md                     # Este archivo
```

## 🚀 Instalación

### Prerrequisitos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Graphviz (para generación de diagramas)

#### Instalar Graphviz

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install graphviz
```

**macOS:**
```bash
brew install graphviz
```

**Windows:**
Descarga e instala desde [graphviz.org](https://graphviz.org/download/)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/Camilo1965/trabajofinal.git
cd trabajofinal
```

2. **Crear entorno virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Generar diagramas UML**
```bash
python diagrams/generate_diagrams.py
```

5. **Generar diagrama ER**
```bash
python database/generate_er_diagram.py
```

6. **Crear base de datos (opcional)**
```bash
sqlite3 database/sistema.db < database/schema.sql
```

## 💻 Uso

### Ejecutar la aplicación

```bash
cd src
python main.py
```

### Menú Principal

La aplicación presenta un menú interactivo:

```
====================================
   SISTEMA DE GESTIÓN
====================================

--- MENÚ PRINCIPAL ---
1. Gestión de Usuarios
2. Gestión de Productos
3. Gestión de Pagos
4. Salir

Seleccione una opción:
```

### Datos de Ejemplo

El sistema crea automáticamente:
- Usuario administrador: `admin` / `admin123`
- Productos de ejemplo en categoría electrónica

### Ejemplos de Uso

#### Registrar un Usuario
```python
from src.models.user import UserRole
from src.controllers.user_controller import UserController
from src.repositories.user_repository import UserRepository

# Inicializar
repo = UserRepository()
controller = UserController(repo)

# Registrar usuario
user = controller.register_user(
    username="usuario1",
    email="usuario1@example.com",
    password="password123",
    role=UserRole.CLIENT,
    full_name="Usuario Ejemplo"
)
```

#### Crear un Producto
```python
from src.models.product import ProductCategory
from src.controllers.product_controller import ProductController
from src.repositories.product_repository import ProductRepository

# Inicializar
repo = ProductRepository()
controller = ProductController(repo)

# Crear producto
product = controller.create_product(
    name="Teclado Mecánico",
    description="Teclado mecánico RGB",
    price=129.99,
    category=ProductCategory.ELECTRONICS,
    stock_quantity=15,
    sku="KBD-MEC-001"
)
```

#### Procesar un Pago
```python
from src.models.payment import PaymentMethod
from src.controllers.payment_controller import PaymentController
from src.repositories.payment_repository import PaymentRepository

# Inicializar
repo = PaymentRepository()
controller = PaymentController(repo)

# Crear pago
payment = controller.create_payment(
    order_id=1,
    user_id=1,
    amount=259.98,
    payment_method=PaymentMethod.CREDIT_CARD
)

# Procesar pago
success = controller.process_payment(payment.payment_id)
```

## 📊 Diagramas

El sistema incluye los siguientes diagramas UML:

### Diagramas de Clases

1. **Módulo de Usuarios** (`diagrams/user_class_diagram.png`)
   - Clases: User, UserProfile, UserRole, UserController, UserRepository

2. **Módulo de Productos** (`diagrams/product_class_diagram.png`)
   - Clases: Product, ProductCategory, Supplier, ProductReview, ProductController, ProductRepository

3. **Módulo de Pagos** (`diagrams/payment_class_diagram.png`)
   - Clases: Payment, PaymentStatus, PaymentMethod, Order, OrderItem, PaymentController, PaymentRepository

### Diagramas Arquitectónicos

4. **Diagrama de Componentes** (`diagrams/component_diagram.png`)
   - Muestra la interacción entre módulos y capas

5. **Diagrama de Despliegue** (`diagrams/deployment_diagram.png`)
   - Representa cómo se ejecuta el sistema en diferentes entornos

6. **Diagrama de Secuencia** (`diagrams/sequence_diagram.png`)
   - Flujo de procesamiento de pagos

### Generar Diagramas

```bash
# Generar todos los diagramas UML
python diagrams/generate_diagrams.py

# Generar diagrama ER
python database/generate_er_diagram.py
```

Los diagramas se generan en formato PNG en sus respectivas carpetas.

## 🗄️ Base de Datos

### Modelo Relacional

El sistema utiliza las siguientes tablas:

- **users**: Usuarios del sistema
- **user_profiles**: Perfiles extendidos
- **user_permissions**: Permisos de usuarios
- **suppliers**: Proveedores
- **products**: Catálogo de productos
- **product_reviews**: Reseñas de productos
- **orders**: Órdenes de compra
- **order_items**: Items de órdenes
- **payments**: Registro de pagos
- **payment_details**: Detalles de pagos

### Diagrama Entidad-Relación

Ver `database/er_diagram.png` para el diagrama completo con relaciones.

### Crear Base de Datos

```bash
# SQLite (desarrollo)
sqlite3 database/sistema.db < database/schema.sql

# MySQL (producción)
mysql -u usuario -p sistema_gestion < database/schema.sql

# PostgreSQL (producción)
psql -U usuario -d sistema_gestion -f database/schema.sql
```

### Scripts SQL

El archivo `database/schema.sql` incluye:
- Definición completa de tablas
- Restricciones (PRIMARY KEY, FOREIGN KEY, CHECK)
- Índices para optimización
- Triggers para auditoría
- Datos de ejemplo

## 📚 Documentación

### Documentos Principales

1. **[Arquitectura del Sistema](docs/arquitectura.md)**
   - Visión general de la arquitectura
   - Descripción de capas y componentes
   - Patrones de diseño utilizados
   - Diagramas arquitectónicos
   - Consideraciones de escalabilidad y seguridad

2. **[Interfaces del Sistema](docs/interfaces.md)**
   - Contratos entre componentes
   - Definición de interfaces
   - Tipos de datos y formatos
   - Diagramas de secuencia
   - Códigos de error

### Generación de Documentación

La documentación está escrita en Markdown y puede convertirse a HTML:

```bash
# Usando mkdocs (requiere instalación)
pip install mkdocs
mkdocs build
mkdocs serve  # Servidor local en http://127.0.0.1:8000
```

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

### Estándares de Código

- Seguir PEP 8 (guía de estilo de Python)
- Documentar todas las funciones y clases
- Incluir type hints
- Escribir tests para nuevo código
- Mantener cobertura de tests > 80%

### Ejecutar Linter

```bash
pylint src/
```

## 📄 Licencia

Este proyecto es un trabajo académico desarrollado para el curso de Ingeniería de Software.

## 👥 Autores

- **Sistema de Gestión Team**
- Repositorio: [Camilo1965/trabajofinal](https://github.com/Camilo1965/trabajofinal)

## 📮 Contacto

Para preguntas o sugerencias, por favor abre un issue en GitHub.

---

## 🎯 Roadmap

### Versión 1.0 (Actual)
- ✅ Implementación de arquitectura MVC
- ✅ Módulos básicos (Usuarios, Productos, Pagos)
- ✅ Diagramas UML completos
- ✅ Base de datos relacional
- ✅ Documentación completa

### Versión 1.1 (Planeada)
- 🔲 Interfaz web con Flask/Django
- 🔲 API RESTful
- 🔲 Autenticación JWT
- 🔲 Tests unitarios completos
- 🔲 CI/CD con GitHub Actions

### Versión 2.0 (Futuro)
- 🔲 Arquitectura de microservicios
- 🔲 Contenedores Docker
- 🔲 Kubernetes para orquestación
- 🔲 Message Queue (RabbitMQ/Kafka)
- 🔲 Cache distribuido (Redis)
- 🔲 Monitoreo con Prometheus/Grafana

---

**¡Gracias por usar el Sistema de Gestión!** ⭐