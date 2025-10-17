"""Repositorio de productos."""

from typing import Optional, List, Dict
from models.product import Product, ProductCategory


class ProductRepository:
    """
    Repositorio para gestionar la persistencia de productos.
    
    Implementa el patrón Repository para abstraer el acceso a datos.
    """
    
    def __init__(self):
        """Inicializa el repositorio con almacenamiento en memoria."""
        self._products: Dict[int, Product] = {}
        self._next_id = 1
    
    def save(self, product: Product) -> Product:
        """
        Guarda un producto en el repositorio.
        
        Args:
            product: Producto a guardar
            
        Returns:
            Producto guardado
        """
        self._products[product.product_id] = product
        return product
    
    def find_by_id(self, product_id: int) -> Optional[Product]:
        """
        Busca un producto por ID.
        
        Args:
            product_id: ID del producto
            
        Returns:
            Producto encontrado o None
        """
        return self._products.get(product_id)
    
    def find_by_sku(self, sku: str) -> Optional[Product]:
        """
        Busca un producto por SKU.
        
        Args:
            sku: Código SKU del producto
            
        Returns:
            Producto encontrado o None
        """
        for product in self._products.values():
            if product.sku == sku:
                return product
        return None
    
    def find_by_category(self, category: ProductCategory) -> List[Product]:
        """
        Busca productos por categoría.
        
        Args:
            category: Categoría del producto
            
        Returns:
            Lista de productos de la categoría
        """
        return [p for p in self._products.values() if p.category == category]
    
    def find_all(self) -> List[Product]:
        """
        Obtiene todos los productos.
        
        Returns:
            Lista de productos
        """
        return list(self._products.values())
    
    def update(self, product: Product) -> Optional[Product]:
        """
        Actualiza un producto.
        
        Args:
            product: Producto a actualizar
            
        Returns:
            Producto actualizado o None si no existe
        """
        if product.product_id in self._products:
            self._products[product.product_id] = product
            return product
        return None
    
    def delete(self, product_id: int) -> bool:
        """
        Elimina un producto.
        
        Args:
            product_id: ID del producto
            
        Returns:
            True si se eliminó, False si no existía
        """
        if product_id in self._products:
            del self._products[product_id]
            return True
        return False
    
    def get_next_id(self) -> int:
        """
        Obtiene el siguiente ID disponible.
        
        Returns:
            Siguiente ID
        """
        current_id = self._next_id
        self._next_id += 1
        return current_id
