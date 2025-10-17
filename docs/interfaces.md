# Interfaces del Sistema de Gestión

## 1. Introducción

Este documento describe las interfaces y contratos entre los componentes del Sistema de Gestión. Define cómo los módulos se comunican entre sí, incluyendo entradas, salidas y tipos de datos.

## 2. Interfaces Principales

### 2.1 Interfaz Vista → Controlador

#### UserController
```python
class UserController:
    def register_user(
        username: str,
        email: str,
        password: str,
        role: UserRole,
        full_name: str
    ) -> Optional[User]
    
    def authenticate(
        username: str,
        password: str
    ) -> Optional[User]
    
    def get_user(user_id: int) -> Optional[User]
    
    def update_user(user: User) -> Optional[User]
    
    def delete_user(user_id: int) -> bool
    
    def list_all_users() -> List[User]
    
    def activate_user(user_id: int) -> bool
    
    def deactivate_user(user_id: int) -> bool
```

**Tipos de Entrada**:
- `username`, `email`, `password`, `full_name`: strings
- `role`: Enum UserRole
- `user_id`: int
- `user`: objeto User

**Tipos de Salida**:
- User object o None
- bool para operaciones de éxito/falla
- List[User] para listados

#### ProductController
```python
class ProductController:
    def create_product(
        name: str,
        description: str,
        price: float,
        category: ProductCategory,
        stock_quantity: int,
        sku: str
    ) -> Optional[Product]
    
    def get_product(product_id: int) -> Optional[Product]
    
    def update_product(product: Product) -> Optional[Product]
    
    def delete_product(product_id: int) -> bool
    
    def list_all_products() -> List[Product]
    
    def list_by_category(
        category: ProductCategory
    ) -> List[Product]
    
    def update_price(
        product_id: int,
        new_price: float
    ) -> bool
    
    def add_stock(
        product_id: int,
        quantity: int
    ) -> bool
    
    def reduce_stock(
        product_id: int,
        quantity: int
    ) -> bool
```

**Tipos de Entrada**:
- Strings: `name`, `description`, `sku`
- float: `price`, `new_price`
- int: `product_id`, `stock_quantity`, `quantity`
- Enum: `ProductCategory`

**Tipos de Salida**:
- Product object o None
- bool para operaciones
- List[Product] para listados

#### PaymentController
```python
class PaymentController:
    def create_payment(
        order_id: int,
        user_id: int,
        amount: float,
        payment_method: PaymentMethod,
        transaction_id: Optional[str] = None
    ) -> Optional[Payment]
    
    def get_payment(payment_id: int) -> Optional[Payment]
    
    def process_payment(payment_id: int) -> bool
    
    def complete_payment(payment_id: int) -> bool
    
    def refund_payment(payment_id: int) -> bool
    
    def cancel_payment(payment_id: int) -> bool
    
    def list_payments_by_user(
        user_id: int
    ) -> List[Payment]
    
    def list_payments_by_status(
        status: PaymentStatus
    ) -> List[Payment]
```

**Tipos de Entrada**:
- int: `order_id`, `user_id`, `payment_id`
- float: `amount`
- Enums: `PaymentMethod`, `PaymentStatus`
- Optional[str]: `transaction_id`

**Tipos de Salida**:
- Payment object o None
- bool para operaciones
- List[Payment] para listados

### 2.2 Interfaz Controlador → Repositorio

#### RepositoryInterface (Genérico)
```python
class Repository[T]:
    def save(entity: T) -> T
    """
    Guarda una entidad en el repositorio.
    Entrada: Objeto del modelo
    Salida: Objeto guardado con ID asignado
    """
    
    def find_by_id(id: int) -> Optional[T]
    """
    Busca una entidad por ID.
    Entrada: ID entero
    Salida: Objeto encontrado o None
    """
    
    def find_all() -> List[T]
    """
    Obtiene todas las entidades.
    Entrada: Ninguna
    Salida: Lista de objetos
    """
    
    def update(entity: T) -> Optional[T]
    """
    Actualiza una entidad existente.
    Entrada: Objeto modificado
    Salida: Objeto actualizado o None
    """
    
    def delete(id: int) -> bool
    """
    Elimina una entidad.
    Entrada: ID entero
    Salida: True si se eliminó, False si no
    """
    
    def get_next_id() -> int
    """
    Obtiene el siguiente ID disponible.
    Entrada: Ninguna
    Salida: ID entero
    """
```

#### UserRepository (Específico)
```python
class UserRepository(Repository[User]):
    def find_by_username(username: str) -> Optional[User]
    """
    Busca usuario por nombre de usuario.
    Entrada: username (str)
    Salida: User o None
    """
    
    def find_by_email(email: str) -> Optional[User]
    """
    Busca usuario por email.
    Entrada: email (str)
    Salida: User o None
    """
```

#### ProductRepository (Específico)
```python
class ProductRepository(Repository[Product]):
    def find_by_sku(sku: str) -> Optional[Product]
    """
    Busca producto por SKU.
    Entrada: sku (str)
    Salida: Product o None
    """
    
    def find_by_category(
        category: ProductCategory
    ) -> List[Product]
    """
    Busca productos por categoría.
    Entrada: category (ProductCategory enum)
    Salida: List[Product]
    """
```

#### PaymentRepository (Específico)
```python
class PaymentRepository(Repository[Payment]):
    def find_by_user_id(user_id: int) -> List[Payment]
    """
    Busca pagos de un usuario.
    Entrada: user_id (int)
    Salida: List[Payment]
    """
    
    def find_by_order_id(order_id: int) -> List[Payment]
    """
    Busca pagos de una orden.
    Entrada: order_id (int)
    Salida: List[Payment]
    """
    
    def find_by_status(
        status: PaymentStatus
    ) -> List[Payment]
    """
    Busca pagos por estado.
    Entrada: status (PaymentStatus enum)
    Salida: List[Payment]
    """
```

### 2.3 Interfaz Repositorio → Base de Datos

#### Operaciones SQL
```python
# CREATE
"""
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...)
RETURNING id
"""
Entrada: Valores de columnas
Salida: ID del registro creado

# READ
"""
SELECT * FROM table_name WHERE id = ?
"""
Entrada: ID o criterios de búsqueda
Salida: Fila(s) de datos

# UPDATE
"""
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE id = ?
"""
Entrada: ID y nuevos valores
Salida: Número de filas afectadas

# DELETE
"""
DELETE FROM table_name WHERE id = ?
"""
Entrada: ID
Salida: Número de filas eliminadas
```

### 2.4 Interfaz Sistema → API Externa (Payment Gateway)

#### PaymentGateway Interface
```python
class PaymentGatewayInterface:
    def process_transaction(
        payment_data: Dict[str, Any]
    ) -> Dict[str, Any]
    """
    Procesa una transacción de pago.
    
    Entrada:
    {
        "amount": float,
        "currency": str,
        "payment_method": str,
        "card_number": str (opcional),
        "cardholder_name": str (opcional),
        "expiry_date": str (opcional),
        "cvv": str (opcional)
    }
    
    Salida:
    {
        "success": bool,
        "transaction_id": str,
        "status": str,
        "message": str,
        "error_code": str (opcional)
    }
    """
    
    def refund_transaction(
        transaction_id: str,
        amount: float
    ) -> Dict[str, Any]
    """
    Procesa un reembolso.
    
    Entrada:
    - transaction_id: str (ID de transacción original)
    - amount: float (monto a reembolsar)
    
    Salida:
    {
        "success": bool,
        "refund_id": str,
        "status": str,
        "message": str
    }
    """
    
    def get_transaction_status(
        transaction_id: str
    ) -> Dict[str, Any]
    """
    Consulta el estado de una transacción.
    
    Entrada:
    - transaction_id: str
    
    Salida:
    {
        "transaction_id": str,
        "status": str,
        "amount": float,
        "created_at": str,
        "completed_at": str (opcional)
    }
    """
```

## 3. Diagramas de Secuencia

### 3.1 Registro de Usuario
```
Usuario → Vista: ingresa datos
Vista → UserController: register_user(...)
UserController → UserRepository: find_by_username(username)
UserRepository → UserController: None (no existe)
UserController → User: new User(...)
UserController → UserRepository: save(user)
UserRepository → DB: INSERT INTO users
DB → UserRepository: user_id
UserRepository → UserController: user
UserController → Vista: user
Vista → Usuario: muestra confirmación
```

### 3.2 Procesamiento de Pago
```
Usuario → Vista: solicita pagar
Vista → PaymentController: create_payment(...)
PaymentController → Payment: new Payment(...)
PaymentController → PaymentRepository: save(payment)
PaymentRepository → DB: INSERT INTO payments
DB → PaymentRepository: payment_id
PaymentRepository → PaymentController: payment
Vista → Usuario: muestra payment_id

Usuario → Vista: confirmar pago
Vista → PaymentController: process_payment(payment_id)
PaymentController → PaymentRepository: find_by_id(payment_id)
PaymentRepository → DB: SELECT * FROM payments WHERE...
DB → PaymentRepository: payment_data
PaymentRepository → PaymentController: payment
PaymentController → Payment: process()
PaymentController → PaymentGateway: process_transaction(...)
PaymentGateway → PaymentController: {success: true, ...}
PaymentController → Payment: complete()
PaymentController → PaymentRepository: update(payment)
PaymentRepository → DB: UPDATE payments SET...
PaymentController → Vista: True
Vista → Usuario: muestra éxito
```

### 3.3 Actualización de Stock
```
Usuario → Vista: solicita agregar stock
Vista → ProductController: add_stock(product_id, quantity)
ProductController → ProductRepository: find_by_id(product_id)
ProductRepository → DB: SELECT * FROM products WHERE...
DB → ProductRepository: product_data
ProductRepository → ProductController: product
ProductController → Product: add_stock(quantity)
Product → Product: valida cantidad > 0
Product → Product: stock_quantity += quantity
ProductController → ProductRepository: update(product)
ProductRepository → DB: UPDATE products SET stock_quantity = ...
DB → ProductRepository: affected_rows
ProductRepository → ProductController: product
ProductController → Vista: True
Vista → Usuario: muestra confirmación
```

## 4. Formatos de Datos

### 4.1 JSON para API (Futuro)

#### User
```json
{
    "user_id": 1,
    "username": "admin",
    "email": "admin@sistema.com",
    "role": "admin",
    "full_name": "Administrador",
    "is_active": true,
    "created_at": "2024-01-15T10:30:00Z"
}
```

#### Product
```json
{
    "product_id": 1,
    "name": "Laptop HP",
    "description": "Laptop HP Core i5...",
    "price": 799.99,
    "category": "electronics",
    "stock_quantity": 10,
    "sku": "LAP-HP-001",
    "is_available": true
}
```

#### Payment
```json
{
    "payment_id": 1,
    "order_id": 1,
    "user_id": 1,
    "amount": 899.98,
    "payment_method": "credit_card",
    "status": "completed",
    "transaction_id": "txn_abc123",
    "created_at": "2024-01-15T14:20:00Z",
    "processed_at": "2024-01-15T14:20:05Z"
}
```

## 5. Códigos de Error

### 5.1 Controladores
- `USER_NOT_FOUND`: Usuario no encontrado
- `USER_ALREADY_EXISTS`: Usuario ya existe
- `INVALID_CREDENTIALS`: Credenciales inválidas
- `PRODUCT_NOT_FOUND`: Producto no encontrado
- `INSUFFICIENT_STOCK`: Stock insuficiente
- `PAYMENT_FAILED`: Fallo en el pago
- `INVALID_AMOUNT`: Monto inválido

### 5.2 Base de Datos
- `CONSTRAINT_VIOLATION`: Violación de restricción
- `FOREIGN_KEY_ERROR`: Error de clave foránea
- `DUPLICATE_KEY`: Clave duplicada
- `CONNECTION_ERROR`: Error de conexión

### 5.3 API Externa
- `GATEWAY_TIMEOUT`: Timeout del gateway
- `INSUFFICIENT_FUNDS`: Fondos insuficientes
- `CARD_DECLINED`: Tarjeta rechazada
- `INVALID_CARD`: Tarjeta inválida

## 6. Versionamiento de Interfaces

Todas las interfaces públicas siguen versionamiento semántico:
- **MAJOR**: Cambios incompatibles
- **MINOR**: Funcionalidad nueva compatible
- **PATCH**: Correcciones compatibles

Versión actual: **1.0.0**
