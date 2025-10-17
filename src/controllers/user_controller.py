"""Controlador de usuarios."""

from typing import Optional, List
from models.user import User, UserRole
from repositories.user_repository import UserRepository


class UserController:
    """
    Controlador para gestionar operaciones de usuarios.
    
    Maneja la lógica de negocio entre la vista y el repositorio.
    """
    
    def __init__(self, user_repository: UserRepository):
        """
        Inicializa el controlador de usuarios.
        
        Args:
            user_repository: Repositorio de usuarios
        """
        self.user_repository = user_repository
    
    def register_user(
        self,
        username: str,
        email: str,
        password: str,
        role: UserRole,
        full_name: str
    ) -> Optional[User]:
        """
        Registra un nuevo usuario en el sistema.
        
        Args:
            username: Nombre de usuario
            email: Correo electrónico
            password: Contraseña
            role: Rol del usuario
            full_name: Nombre completo
            
        Returns:
            Usuario creado o None si falla
        """
        # Validar que el username y email no existan
        if self.user_repository.find_by_username(username):
            return None
        if self.user_repository.find_by_email(email):
            return None
        
        # Hash de la contraseña (simplificado para el ejemplo)
        password_hash = self._hash_password(password)
        
        # Crear y guardar usuario
        user = User(
            user_id=self.user_repository.get_next_id(),
            username=username,
            email=email,
            password_hash=password_hash,
            role=role,
            full_name=full_name
        )
        
        return self.user_repository.save(user)
    
    def authenticate(self, username: str, password: str) -> Optional[User]:
        """
        Autentica un usuario.
        
        Args:
            username: Nombre de usuario
            password: Contraseña
            
        Returns:
            Usuario autenticado o None si falla
        """
        user = self.user_repository.find_by_username(username)
        if not user or not user.is_active:
            return None
        
        password_hash = self._hash_password(password)
        if user.password_hash == password_hash:
            return user
        
        return None
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Obtiene un usuario por ID."""
        return self.user_repository.find_by_id(user_id)
    
    def update_user(self, user: User) -> Optional[User]:
        """Actualiza un usuario."""
        return self.user_repository.update(user)
    
    def delete_user(self, user_id: int) -> bool:
        """Elimina un usuario."""
        return self.user_repository.delete(user_id)
    
    def list_all_users(self) -> List[User]:
        """Lista todos los usuarios."""
        return self.user_repository.find_all()
    
    def activate_user(self, user_id: int) -> bool:
        """Activa un usuario."""
        user = self.get_user(user_id)
        if user:
            user.activate()
            self.user_repository.update(user)
            return True
        return False
    
    def deactivate_user(self, user_id: int) -> bool:
        """Desactiva un usuario."""
        user = self.get_user(user_id)
        if user:
            user.deactivate()
            self.user_repository.update(user)
            return True
        return False
    
    @staticmethod
    def _hash_password(password: str) -> str:
        """Hash de contraseña (implementación simplificada)."""
        # En producción usar bcrypt o similar
        return f"hashed_{password}"
