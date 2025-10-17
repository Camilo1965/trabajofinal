"""Aplicación principal del Sistema de Gestión."""

from models.user import UserRole
from models.product import ProductCategory
from models.payment import PaymentMethod
from controllers.user_controller import UserController
from controllers.product_controller import ProductController
from controllers.payment_controller import PaymentController
from repositories.user_repository import UserRepository
from repositories.product_repository import ProductRepository
from repositories.payment_repository import PaymentRepository
from views.console_view import ConsoleView


class SistemaGestion:
    """Aplicación principal del Sistema de Gestión."""
    
    def __init__(self):
        """Inicializa el sistema con todos sus componentes."""
        # Inicializar repositorios
        self.user_repository = UserRepository()
        self.product_repository = ProductRepository()
        self.payment_repository = PaymentRepository()
        
        # Inicializar controladores
        self.user_controller = UserController(self.user_repository)
        self.product_controller = ProductController(self.product_repository)
        self.payment_controller = PaymentController(self.payment_repository)
        
        # Inicializar vista
        self.view = ConsoleView()
    
    def run(self) -> None:
        """Ejecuta el bucle principal de la aplicación."""
        self.view.display_welcome()
        
        # Crear datos de ejemplo
        self._create_sample_data()
        
        while True:
            self.view.display_menu()
            option = self.view.get_input("Seleccione una opción: ")
            
            if option == "1":
                self._user_management()
            elif option == "2":
                self._product_management()
            elif option == "3":
                self._payment_management()
            elif option == "4":
                self.view.display_info("¡Hasta luego!")
                break
            else:
                self.view.display_error("Opción inválida")
    
    def _user_management(self) -> None:
        """Gestiona el menú de usuarios."""
        while True:
            self.view.display_user_menu()
            option = self.view.get_input("Seleccione una opción: ")
            
            if option == "1":
                self._register_user()
            elif option == "2":
                self._list_users()
            elif option == "3":
                self._search_user()
            elif option == "4":
                break
            else:
                self.view.display_error("Opción inválida")
    
    def _product_management(self) -> None:
        """Gestiona el menú de productos."""
        while True:
            self.view.display_product_menu()
            option = self.view.get_input("Seleccione una opción: ")
            
            if option == "1":
                self._create_product()
            elif option == "2":
                self._list_products()
            elif option == "3":
                self._update_stock()
            elif option == "4":
                break
            else:
                self.view.display_error("Opción inválida")
    
    def _payment_management(self) -> None:
        """Gestiona el menú de pagos."""
        while True:
            self.view.display_payment_menu()
            option = self.view.get_input("Seleccione una opción: ")
            
            if option == "1":
                self._create_payment()
            elif option == "2":
                self._process_payment()
            elif option == "3":
                self._list_payments()
            elif option == "4":
                break
            else:
                self.view.display_error("Opción inválida")
    
    def _register_user(self) -> None:
        """Registra un nuevo usuario."""
        username = self.view.get_input("Username: ")
        email = self.view.get_input("Email: ")
        password = self.view.get_input("Password: ")
        full_name = self.view.get_input("Nombre completo: ")
        
        user = self.user_controller.register_user(
            username=username,
            email=email,
            password=password,
            role=UserRole.CLIENT,
            full_name=full_name
        )
        
        if user:
            self.view.display_success(f"Usuario creado con ID: {user.user_id}")
        else:
            self.view.display_error("No se pudo crear el usuario")
    
    def _list_users(self) -> None:
        """Lista todos los usuarios."""
        users = self.user_controller.list_all_users()
        if users:
            for user in users:
                self.view.display_user(user)
        else:
            self.view.display_info("No hay usuarios registrados")
    
    def _search_user(self) -> None:
        """Busca un usuario por ID."""
        user_id = int(self.view.get_input("ID del usuario: "))
        user = self.user_controller.get_user(user_id)
        if user:
            self.view.display_user(user)
        else:
            self.view.display_error("Usuario no encontrado")
    
    def _create_product(self) -> None:
        """Crea un nuevo producto."""
        name = self.view.get_input("Nombre: ")
        description = self.view.get_input("Descripción: ")
        price = float(self.view.get_input("Precio: "))
        sku = self.view.get_input("SKU: ")
        stock = int(self.view.get_input("Stock inicial: "))
        
        product = self.product_controller.create_product(
            name=name,
            description=description,
            price=price,
            category=ProductCategory.OTHER,
            stock_quantity=stock,
            sku=sku
        )
        
        if product:
            self.view.display_success(f"Producto creado con ID: {product.product_id}")
        else:
            self.view.display_error("No se pudo crear el producto")
    
    def _list_products(self) -> None:
        """Lista todos los productos."""
        products = self.product_controller.list_all_products()
        if products:
            for product in products:
                self.view.display_product(product)
        else:
            self.view.display_info("No hay productos registrados")
    
    def _update_stock(self) -> None:
        """Actualiza el stock de un producto."""
        product_id = int(self.view.get_input("ID del producto: "))
        quantity = int(self.view.get_input("Cantidad a agregar: "))
        
        if self.product_controller.add_stock(product_id, quantity):
            self.view.display_success("Stock actualizado")
        else:
            self.view.display_error("No se pudo actualizar el stock")
    
    def _create_payment(self) -> None:
        """Crea un nuevo pago."""
        order_id = int(self.view.get_input("ID de la orden: "))
        user_id = int(self.view.get_input("ID del usuario: "))
        amount = float(self.view.get_input("Monto: "))
        
        payment = self.payment_controller.create_payment(
            order_id=order_id,
            user_id=user_id,
            amount=amount,
            payment_method=PaymentMethod.CREDIT_CARD
        )
        
        if payment:
            self.view.display_success(f"Pago creado con ID: {payment.payment_id}")
        else:
            self.view.display_error("No se pudo crear el pago")
    
    def _process_payment(self) -> None:
        """Procesa un pago."""
        payment_id = int(self.view.get_input("ID del pago: "))
        
        if self.payment_controller.process_payment(payment_id):
            self.view.display_success("Pago procesado exitosamente")
        else:
            self.view.display_error("No se pudo procesar el pago")
    
    def _list_payments(self) -> None:
        """Lista todos los pagos."""
        payments = self.payment_repository.find_all()
        if payments:
            for payment in payments:
                self.view.display_payment(payment)
        else:
            self.view.display_info("No hay pagos registrados")
    
    def _create_sample_data(self) -> None:
        """Crea datos de ejemplo para demostración."""
        # Crear usuario admin
        self.user_controller.register_user(
            username="admin",
            email="admin@sistema.com",
            password="admin123",
            role=UserRole.ADMIN,
            full_name="Administrador del Sistema"
        )
        
        # Crear productos de ejemplo
        self.product_controller.create_product(
            name="Laptop HP",
            description="Laptop HP Core i5, 8GB RAM, 256GB SSD",
            price=799.99,
            category=ProductCategory.ELECTRONICS,
            stock_quantity=10,
            sku="LAP-HP-001"
        )
        
        self.product_controller.create_product(
            name="Mouse Logitech",
            description="Mouse inalámbrico Logitech MX Master",
            price=89.99,
            category=ProductCategory.ELECTRONICS,
            stock_quantity=25,
            sku="MOU-LOG-001"
        )


def main():
    """Función principal."""
    app = SistemaGestion()
    app.run()


if __name__ == "__main__":
    main()
