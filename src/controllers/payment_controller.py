"""Controlador de pagos."""

from typing import Optional, List
from models.payment import Payment, PaymentMethod, PaymentStatus
from repositories.payment_repository import PaymentRepository


class PaymentController:
    """
    Controlador para gestionar operaciones de pagos.
    
    Maneja la lógica de negocio entre la vista y el repositorio.
    """
    
    def __init__(self, payment_repository: PaymentRepository):
        """
        Inicializa el controlador de pagos.
        
        Args:
            payment_repository: Repositorio de pagos
        """
        self.payment_repository = payment_repository
    
    def create_payment(
        self,
        order_id: int,
        user_id: int,
        amount: float,
        payment_method: PaymentMethod,
        transaction_id: Optional[str] = None
    ) -> Optional[Payment]:
        """
        Crea un nuevo pago.
        
        Args:
            order_id: ID de la orden
            user_id: ID del usuario
            amount: Monto del pago
            payment_method: Método de pago
            transaction_id: ID de transacción externo
            
        Returns:
            Pago creado o None si falla
        """
        if amount <= 0:
            return None
        
        payment = Payment(
            payment_id=self.payment_repository.get_next_id(),
            order_id=order_id,
            user_id=user_id,
            amount=amount,
            payment_method=payment_method,
            transaction_id=transaction_id
        )
        
        return self.payment_repository.save(payment)
    
    def get_payment(self, payment_id: int) -> Optional[Payment]:
        """Obtiene un pago por ID."""
        return self.payment_repository.find_by_id(payment_id)
    
    def process_payment(self, payment_id: int) -> bool:
        """
        Procesa un pago.
        
        Args:
            payment_id: ID del pago
            
        Returns:
            True si el pago se procesó correctamente
        """
        payment = self.get_payment(payment_id)
        if not payment:
            return False
        
        try:
            payment.process()
            self.payment_repository.update(payment)
            
            # Simulación de procesamiento
            success = self._process_with_gateway(payment)
            
            if success:
                payment.complete()
            else:
                payment.fail("Error al procesar con el gateway de pago")
            
            self.payment_repository.update(payment)
            return success
        except ValueError:
            return False
    
    def complete_payment(self, payment_id: int) -> bool:
        """Marca un pago como completado."""
        payment = self.get_payment(payment_id)
        if payment:
            try:
                payment.complete()
                self.payment_repository.update(payment)
                return True
            except ValueError:
                return False
        return False
    
    def refund_payment(self, payment_id: int) -> bool:
        """Reembolsa un pago."""
        payment = self.get_payment(payment_id)
        if payment:
            try:
                payment.refund()
                self.payment_repository.update(payment)
                return True
            except ValueError:
                return False
        return False
    
    def cancel_payment(self, payment_id: int) -> bool:
        """Cancela un pago."""
        payment = self.get_payment(payment_id)
        if payment:
            try:
                payment.cancel()
                self.payment_repository.update(payment)
                return True
            except ValueError:
                return False
        return False
    
    def list_payments_by_user(self, user_id: int) -> List[Payment]:
        """Lista pagos de un usuario."""
        return self.payment_repository.find_by_user_id(user_id)
    
    def list_payments_by_status(self, status: PaymentStatus) -> List[Payment]:
        """Lista pagos por estado."""
        return self.payment_repository.find_by_status(status)
    
    @staticmethod
    def _process_with_gateway(payment: Payment) -> bool:
        """
        Procesa el pago con el gateway externo.
        
        Esta es una simulación. En producción se conectaría
        con un gateway de pago real (Stripe, PayPal, etc.).
        
        Args:
            payment: Pago a procesar
            
        Returns:
            True si el procesamiento fue exitoso
        """
        # Simulación: 90% de éxito
        import random
        return random.random() > 0.1
