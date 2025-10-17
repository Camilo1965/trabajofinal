"""Módulo de procesamiento de pagos."""

from enum import Enum
from datetime import datetime
from typing import Optional, List


class PaymentStatus(Enum):
    """Estados de un pago."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"
    CANCELLED = "cancelled"


class PaymentMethod(Enum):
    """Métodos de pago disponibles."""
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"
    CASH = "cash"


class Payment:
    """
    Clase que representa un pago en el sistema.
    
    Attributes:
        payment_id: Identificador único del pago
        order_id: ID de la orden asociada
        user_id: ID del usuario que realiza el pago
        amount: Monto del pago
        payment_method: Método de pago utilizado
        status: Estado actual del pago
        transaction_id: ID de transacción externo
        created_at: Fecha de creación
        processed_at: Fecha de procesamiento
    """
    
    def __init__(
        self,
        payment_id: int,
        order_id: int,
        user_id: int,
        amount: float,
        payment_method: PaymentMethod,
        transaction_id: Optional[str] = None
    ):
        self.payment_id = payment_id
        self.order_id = order_id
        self.user_id = user_id
        self.amount = amount
        self.payment_method = payment_method
        self.status = PaymentStatus.PENDING
        self.transaction_id = transaction_id
        self.created_at = datetime.now()
        self.processed_at: Optional[datetime] = None
        self.refunded_at: Optional[datetime] = None
        self.payment_details: Optional['PaymentDetails'] = None
    
    def process(self) -> None:
        """Inicia el procesamiento del pago."""
        if self.status != PaymentStatus.PENDING:
            raise ValueError("Solo se pueden procesar pagos pendientes")
        self.status = PaymentStatus.PROCESSING
    
    def complete(self) -> None:
        """Marca el pago como completado."""
        if self.status != PaymentStatus.PROCESSING:
            raise ValueError("Solo se pueden completar pagos en procesamiento")
        self.status = PaymentStatus.COMPLETED
        self.processed_at = datetime.now()
    
    def fail(self, error_message: str) -> None:
        """
        Marca el pago como fallido.
        
        Args:
            error_message: Mensaje de error
        """
        self.status = PaymentStatus.FAILED
        if self.payment_details:
            self.payment_details.error_message = error_message
    
    def refund(self) -> None:
        """Procesa un reembolso del pago."""
        if self.status != PaymentStatus.COMPLETED:
            raise ValueError("Solo se pueden reembolsar pagos completados")
        self.status = PaymentStatus.REFUNDED
        self.refunded_at = datetime.now()
    
    def cancel(self) -> None:
        """Cancela el pago."""
        if self.status not in [PaymentStatus.PENDING, PaymentStatus.PROCESSING]:
            raise ValueError("No se puede cancelar un pago completado o fallido")
        self.status = PaymentStatus.CANCELLED
    
    def is_successful(self) -> bool:
        """Verifica si el pago fue exitoso."""
        return self.status == PaymentStatus.COMPLETED
    
    def __repr__(self) -> str:
        return f"Payment(id={self.payment_id}, amount={self.amount}, status={self.status.value})"


class PaymentDetails:
    """
    Detalles adicionales del pago.
    
    Attributes:
        details_id: ID de los detalles
        payment_id: ID del pago asociado
        card_last_four: Últimos 4 dígitos de tarjeta
        billing_address: Dirección de facturación
        error_message: Mensaje de error si aplica
    """
    
    def __init__(
        self,
        details_id: int,
        payment_id: int,
        card_last_four: Optional[str] = None,
        billing_address: Optional[str] = None
    ):
        self.details_id = details_id
        self.payment_id = payment_id
        self.card_last_four = card_last_four
        self.billing_address = billing_address
        self.error_message: Optional[str] = None
    
    def __repr__(self) -> str:
        return f"PaymentDetails(id={self.details_id}, payment_id={self.payment_id})"


class Order:
    """
    Clase que representa una orden de compra.
    
    Attributes:
        order_id: Identificador de la orden
        user_id: ID del usuario
        total_amount: Monto total
        items: Lista de items en la orden
        created_at: Fecha de creación
    """
    
    def __init__(
        self,
        order_id: int,
        user_id: int,
        total_amount: float
    ):
        self.order_id = order_id
        self.user_id = user_id
        self.total_amount = total_amount
        self.items: List['OrderItem'] = []
        self.created_at = datetime.now()
        self.payment: Optional[Payment] = None
    
    def add_item(self, item: 'OrderItem') -> None:
        """Agrega un item a la orden."""
        self.items.append(item)
    
    def calculate_total(self) -> float:
        """Calcula el total de la orden."""
        return sum(item.subtotal for item in self.items)
    
    def __repr__(self) -> str:
        return f"Order(id={self.order_id}, total={self.total_amount})"


class OrderItem:
    """
    Item de una orden.
    
    Attributes:
        item_id: ID del item
        order_id: ID de la orden
        product_id: ID del producto
        quantity: Cantidad
        unit_price: Precio unitario
        subtotal: Subtotal del item
    """
    
    def __init__(
        self,
        item_id: int,
        order_id: int,
        product_id: int,
        quantity: int,
        unit_price: float
    ):
        self.item_id = item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.subtotal = quantity * unit_price
    
    def __repr__(self) -> str:
        return f"OrderItem(id={self.item_id}, quantity={self.quantity}, subtotal={self.subtotal})"
