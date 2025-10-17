"""Repositorio de pagos."""

from typing import Optional, List, Dict
from models.payment import Payment, PaymentStatus


class PaymentRepository:
    """
    Repositorio para gestionar la persistencia de pagos.
    
    Implementa el patrón Repository para abstraer el acceso a datos.
    """
    
    def __init__(self):
        """Inicializa el repositorio con almacenamiento en memoria."""
        self._payments: Dict[int, Payment] = {}
        self._next_id = 1
    
    def save(self, payment: Payment) -> Payment:
        """
        Guarda un pago en el repositorio.
        
        Args:
            payment: Pago a guardar
            
        Returns:
            Pago guardado
        """
        self._payments[payment.payment_id] = payment
        return payment
    
    def find_by_id(self, payment_id: int) -> Optional[Payment]:
        """
        Busca un pago por ID.
        
        Args:
            payment_id: ID del pago
            
        Returns:
            Pago encontrado o None
        """
        return self._payments.get(payment_id)
    
    def find_by_user_id(self, user_id: int) -> List[Payment]:
        """
        Busca pagos por ID de usuario.
        
        Args:
            user_id: ID del usuario
            
        Returns:
            Lista de pagos del usuario
        """
        return [p for p in self._payments.values() if p.user_id == user_id]
    
    def find_by_order_id(self, order_id: int) -> List[Payment]:
        """
        Busca pagos por ID de orden.
        
        Args:
            order_id: ID de la orden
            
        Returns:
            Lista de pagos de la orden
        """
        return [p for p in self._payments.values() if p.order_id == order_id]
    
    def find_by_status(self, status: PaymentStatus) -> List[Payment]:
        """
        Busca pagos por estado.
        
        Args:
            status: Estado del pago
            
        Returns:
            Lista de pagos con ese estado
        """
        return [p for p in self._payments.values() if p.status == status]
    
    def find_all(self) -> List[Payment]:
        """
        Obtiene todos los pagos.
        
        Returns:
            Lista de pagos
        """
        return list(self._payments.values())
    
    def update(self, payment: Payment) -> Optional[Payment]:
        """
        Actualiza un pago.
        
        Args:
            payment: Pago a actualizar
            
        Returns:
            Pago actualizado o None si no existe
        """
        if payment.payment_id in self._payments:
            self._payments[payment.payment_id] = payment
            return payment
        return None
    
    def delete(self, payment_id: int) -> bool:
        """
        Elimina un pago.
        
        Args:
            payment_id: ID del pago
            
        Returns:
            True si se eliminó, False si no existía
        """
        if payment_id in self._payments:
            del self._payments[payment_id]
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
