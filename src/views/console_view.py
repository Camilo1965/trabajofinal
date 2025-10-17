"""Vista de consola para el Sistema de Gestión."""

from typing import Optional
from models.user import User, UserRole
from models.product import Product, ProductCategory
from models.payment import Payment, PaymentMethod


class ConsoleView:
    """
    Vista de consola para interactuar con el sistema.
    
    Proporciona una interfaz de línea de comandos para el usuario.
    """
    
    @staticmethod
    def display_welcome() -> None:
        """Muestra el mensaje de bienvenida."""
        print("=" * 50)
        print("   SISTEMA DE GESTIÓN")
        print("=" * 50)
        print()
    
    @staticmethod
    def display_menu() -> None:
        """Muestra el menú principal."""
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Productos")
        print("3. Gestión de Pagos")
        print("4. Salir")
        print()
    
    @staticmethod
    def display_user_menu() -> None:
        """Muestra el menú de usuarios."""
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Volver")
        print()
    
    @staticmethod
    def display_product_menu() -> None:
        """Muestra el menú de productos."""
        print("\n--- GESTIÓN DE PRODUCTOS ---")
        print("1. Crear producto")
        print("2. Listar productos")
        print("3. Actualizar stock")
        print("4. Volver")
        print()
    
    @staticmethod
    def display_payment_menu() -> None:
        """Muestra el menú de pagos."""
        print("\n--- GESTIÓN DE PAGOS ---")
        print("1. Crear pago")
        print("2. Procesar pago")
        print("3. Listar pagos")
        print("4. Volver")
        print()
    
    @staticmethod
    def display_user(user: User) -> None:
        """
        Muestra información de un usuario.
        
        Args:
            user: Usuario a mostrar
        """
        print(f"\nUsuario ID: {user.user_id}")
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Nombre: {user.full_name}")
        print(f"Rol: {user.role.value}")
        print(f"Activo: {'Sí' if user.is_active else 'No'}")
        print(f"Creado: {user.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
    
    @staticmethod
    def display_product(product: Product) -> None:
        """
        Muestra información de un producto.
        
        Args:
            product: Producto a mostrar
        """
        print(f"\nProducto ID: {product.product_id}")
        print(f"Nombre: {product.name}")
        print(f"Descripción: {product.description}")
        print(f"Precio: ${product.price:.2f}")
        print(f"Categoría: {product.category.value}")
        print(f"SKU: {product.sku}")
        print(f"Stock: {product.stock_quantity}")
        print(f"Disponible: {'Sí' if product.is_available else 'No'}")
    
    @staticmethod
    def display_payment(payment: Payment) -> None:
        """
        Muestra información de un pago.
        
        Args:
            payment: Pago a mostrar
        """
        print(f"\nPago ID: {payment.payment_id}")
        print(f"Orden ID: {payment.order_id}")
        print(f"Usuario ID: {payment.user_id}")
        print(f"Monto: ${payment.amount:.2f}")
        print(f"Método: {payment.payment_method.value}")
        print(f"Estado: {payment.status.value}")
        print(f"Creado: {payment.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        if payment.processed_at:
            print(f"Procesado: {payment.processed_at.strftime('%Y-%m-%d %H:%M:%S')}")
    
    @staticmethod
    def get_input(prompt: str) -> str:
        """
        Obtiene entrada del usuario.
        
        Args:
            prompt: Mensaje a mostrar
            
        Returns:
            Entrada del usuario
        """
        return input(prompt)
    
    @staticmethod
    def display_error(message: str) -> None:
        """
        Muestra un mensaje de error.
        
        Args:
            message: Mensaje de error
        """
        print(f"\n❌ ERROR: {message}")
    
    @staticmethod
    def display_success(message: str) -> None:
        """
        Muestra un mensaje de éxito.
        
        Args:
            message: Mensaje de éxito
        """
        print(f"\n✓ ÉXITO: {message}")
    
    @staticmethod
    def display_info(message: str) -> None:
        """
        Muestra un mensaje informativo.
        
        Args:
            message: Mensaje informativo
        """
        print(f"\nℹ INFO: {message}")
