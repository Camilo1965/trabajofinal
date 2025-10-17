"""Módulo de gestión de usuarios."""

from enum import Enum
from datetime import datetime
from typing import Optional, List


class UserRole(Enum):
    """Roles de usuario en el sistema."""
    ADMIN = "admin"
    MANAGER = "manager"
    EMPLOYEE = "employee"
    CLIENT = "client"


class User:
    """
    Clase que representa un usuario en el sistema.
    
    Attributes:
        user_id: Identificador único del usuario
        username: Nombre de usuario único
        email: Correo electrónico
        password_hash: Hash de la contraseña
        role: Rol del usuario en el sistema
        full_name: Nombre completo del usuario
        created_at: Fecha de creación
        is_active: Estado del usuario
        profile: Información del perfil del usuario
    """
    
    def __init__(
        self,
        user_id: int,
        username: str,
        email: str,
        password_hash: str,
        role: UserRole,
        full_name: str,
        is_active: bool = True
    ):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.full_name = full_name
        self.created_at = datetime.now()
        self.is_active = is_active
        self.profile: Optional['UserProfile'] = None
        self.permissions: List[str] = []
    
    def activate(self) -> None:
        """Activa la cuenta del usuario."""
        self.is_active = True
    
    def deactivate(self) -> None:
        """Desactiva la cuenta del usuario."""
        self.is_active = False
    
    def change_password(self, new_password_hash: str) -> None:
        """
        Cambia la contraseña del usuario.
        
        Args:
            new_password_hash: Nuevo hash de la contraseña
        """
        self.password_hash = new_password_hash
    
    def has_permission(self, permission: str) -> bool:
        """
        Verifica si el usuario tiene un permiso específico.
        
        Args:
            permission: Nombre del permiso a verificar
            
        Returns:
            True si el usuario tiene el permiso
        """
        return permission in self.permissions
    
    def add_permission(self, permission: str) -> None:
        """Agrega un permiso al usuario."""
        if permission not in self.permissions:
            self.permissions.append(permission)
    
    def __repr__(self) -> str:
        return f"User(id={self.user_id}, username='{self.username}', role={self.role.value})"


class UserProfile:
    """
    Perfil extendido del usuario.
    
    Attributes:
        profile_id: Identificador del perfil
        user_id: ID del usuario asociado
        phone: Número de teléfono
        address: Dirección
        date_of_birth: Fecha de nacimiento
    """
    
    def __init__(
        self,
        profile_id: int,
        user_id: int,
        phone: Optional[str] = None,
        address: Optional[str] = None,
        date_of_birth: Optional[datetime] = None
    ):
        self.profile_id = profile_id
        self.user_id = user_id
        self.phone = phone
        self.address = address
        self.date_of_birth = date_of_birth
        self.updated_at = datetime.now()
    
    def update_contact_info(self, phone: str, address: str) -> None:
        """Actualiza la información de contacto."""
        self.phone = phone
        self.address = address
        self.updated_at = datetime.now()
    
    def __repr__(self) -> str:
        return f"UserProfile(id={self.profile_id}, user_id={self.user_id})"
