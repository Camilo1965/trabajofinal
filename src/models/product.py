"""Módulo de gestión de productos."""

from enum import Enum
from datetime import datetime
from typing import Optional, List


class ProductCategory(Enum):
    """Categorías de productos."""
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    FOOD = "food"
    BOOKS = "books"
    TOYS = "toys"
    FURNITURE = "furniture"
    OTHER = "other"


class Product:
    """
    Clase que representa un producto en el sistema.
    
    Attributes:
        product_id: Identificador único del producto
        name: Nombre del producto
        description: Descripción del producto
        price: Precio del producto
        category: Categoría del producto
        stock_quantity: Cantidad en inventario
        sku: Código SKU del producto
        created_at: Fecha de creación
        is_available: Disponibilidad del producto
    """
    
    def __init__(
        self,
        product_id: int,
        name: str,
        description: str,
        price: float,
        category: ProductCategory,
        stock_quantity: int,
        sku: str,
        is_available: bool = True
    ):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity
        self.sku = sku
        self.created_at = datetime.now()
        self.is_available = is_available
        self.supplier: Optional['Supplier'] = None
        self.reviews: List['ProductReview'] = []
    
    def update_price(self, new_price: float) -> None:
        """
        Actualiza el precio del producto.
        
        Args:
            new_price: Nuevo precio del producto
        """
        if new_price < 0:
            raise ValueError("El precio no puede ser negativo")
        self.price = new_price
    
    def add_stock(self, quantity: int) -> None:
        """
        Agrega cantidad al inventario.
        
        Args:
            quantity: Cantidad a agregar
        """
        if quantity < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.stock_quantity += quantity
    
    def reduce_stock(self, quantity: int) -> None:
        """
        Reduce cantidad del inventario.
        
        Args:
            quantity: Cantidad a reducir
            
        Raises:
            ValueError: Si no hay suficiente stock
        """
        if quantity < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if self.stock_quantity < quantity:
            raise ValueError("Stock insuficiente")
        self.stock_quantity -= quantity
    
    def is_in_stock(self) -> bool:
        """Verifica si el producto está en stock."""
        return self.stock_quantity > 0
    
    def set_availability(self, available: bool) -> None:
        """Establece la disponibilidad del producto."""
        self.is_available = available
    
    def add_review(self, review: 'ProductReview') -> None:
        """Agrega una reseña al producto."""
        self.reviews.append(review)
    
    def get_average_rating(self) -> float:
        """Calcula el rating promedio del producto."""
        if not self.reviews:
            return 0.0
        return sum(r.rating for r in self.reviews) / len(self.reviews)
    
    def __repr__(self) -> str:
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price})"


class Supplier:
    """
    Clase que representa un proveedor.
    
    Attributes:
        supplier_id: Identificador del proveedor
        name: Nombre del proveedor
        contact_email: Email de contacto
        phone: Teléfono
    """
    
    def __init__(
        self,
        supplier_id: int,
        name: str,
        contact_email: str,
        phone: str
    ):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email
        self.phone = phone
    
    def __repr__(self) -> str:
        return f"Supplier(id={self.supplier_id}, name='{self.name}')"


class ProductReview:
    """
    Reseña de producto.
    
    Attributes:
        review_id: ID de la reseña
        product_id: ID del producto
        user_id: ID del usuario que escribió la reseña
        rating: Calificación (1-5)
        comment: Comentario
        created_at: Fecha de creación
    """
    
    def __init__(
        self,
        review_id: int,
        product_id: int,
        user_id: int,
        rating: int,
        comment: str
    ):
        if not 1 <= rating <= 5:
            raise ValueError("El rating debe estar entre 1 y 5")
        self.review_id = review_id
        self.product_id = product_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
    
    def __repr__(self) -> str:
        return f"ProductReview(id={self.review_id}, rating={self.rating})"
