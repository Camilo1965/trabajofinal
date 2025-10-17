"""Controlador de productos."""

from typing import Optional, List
from models.product import Product, ProductCategory
from repositories.product_repository import ProductRepository


class ProductController:
    """
    Controlador para gestionar operaciones de productos.
    
    Maneja la lógica de negocio entre la vista y el repositorio.
    """
    
    def __init__(self, product_repository: ProductRepository):
        """
        Inicializa el controlador de productos.
        
        Args:
            product_repository: Repositorio de productos
        """
        self.product_repository = product_repository
    
    def create_product(
        self,
        name: str,
        description: str,
        price: float,
        category: ProductCategory,
        stock_quantity: int,
        sku: str
    ) -> Optional[Product]:
        """
        Crea un nuevo producto.
        
        Args:
            name: Nombre del producto
            description: Descripción
            price: Precio
            category: Categoría
            stock_quantity: Cantidad en stock
            sku: Código SKU
            
        Returns:
            Producto creado o None si falla
        """
        # Validar que el SKU no exista
        if self.product_repository.find_by_sku(sku):
            return None
        
        # Validar precio positivo
        if price < 0:
            return None
        
        product = Product(
            product_id=self.product_repository.get_next_id(),
            name=name,
            description=description,
            price=price,
            category=category,
            stock_quantity=stock_quantity,
            sku=sku
        )
        
        return self.product_repository.save(product)
    
    def get_product(self, product_id: int) -> Optional[Product]:
        """Obtiene un producto por ID."""
        return self.product_repository.find_by_id(product_id)
    
    def update_product(self, product: Product) -> Optional[Product]:
        """Actualiza un producto."""
        return self.product_repository.update(product)
    
    def delete_product(self, product_id: int) -> bool:
        """Elimina un producto."""
        return self.product_repository.delete(product_id)
    
    def list_all_products(self) -> List[Product]:
        """Lista todos los productos."""
        return self.product_repository.find_all()
    
    def list_by_category(self, category: ProductCategory) -> List[Product]:
        """Lista productos por categoría."""
        return self.product_repository.find_by_category(category)
    
    def update_price(self, product_id: int, new_price: float) -> bool:
        """Actualiza el precio de un producto."""
        product = self.get_product(product_id)
        if product:
            try:
                product.update_price(new_price)
                self.product_repository.update(product)
                return True
            except ValueError:
                return False
        return False
    
    def add_stock(self, product_id: int, quantity: int) -> bool:
        """Agrega stock a un producto."""
        product = self.get_product(product_id)
        if product:
            try:
                product.add_stock(quantity)
                self.product_repository.update(product)
                return True
            except ValueError:
                return False
        return False
    
    def reduce_stock(self, product_id: int, quantity: int) -> bool:
        """Reduce stock de un producto."""
        product = self.get_product(product_id)
        if product:
            try:
                product.reduce_stock(quantity)
                self.product_repository.update(product)
                return True
            except ValueError:
                return False
        return False
    
    def set_availability(self, product_id: int, available: bool) -> bool:
        """Establece la disponibilidad de un producto."""
        product = self.get_product(product_id)
        if product:
            product.set_availability(available)
            self.product_repository.update(product)
            return True
        return False
