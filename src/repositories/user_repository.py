"""Repositorio de usuarios."""

from typing import Optional, List, Dict
from models.user import User


class UserRepository:
    """
    Repositorio para gestionar la persistencia de usuarios.
    
    Implementa el patrón Repository para abstraer el acceso a datos.
    """
    
    def __init__(self):
        """Inicializa el repositorio con almacenamiento en memoria."""
        self._users: Dict[int, User] = {}
        self._next_id = 1
    
    def save(self, user: User) -> User:
        """
        Guarda un usuario en el repositorio.
        
        Args:
            user: Usuario a guardar
            
        Returns:
            Usuario guardado
        """
        self._users[user.user_id] = user
        return user
    
    def find_by_id(self, user_id: int) -> Optional[User]:
        """
        Busca un usuario por ID.
        
        Args:
            user_id: ID del usuario
            
        Returns:
            Usuario encontrado o None
        """
        return self._users.get(user_id)
    
    def find_by_username(self, username: str) -> Optional[User]:
        """
        Busca un usuario por nombre de usuario.
        
        Args:
            username: Nombre de usuario
            
        Returns:
            Usuario encontrado o None
        """
        for user in self._users.values():
            if user.username == username:
                return user
        return None
    
    def find_by_email(self, email: str) -> Optional[User]:
        """
        Busca un usuario por email.
        
        Args:
            email: Email del usuario
            
        Returns:
            Usuario encontrado o None
        """
        for user in self._users.values():
            if user.email == email:
                return user
        return None
    
    def find_all(self) -> List[User]:
        """
        Obtiene todos los usuarios.
        
        Returns:
            Lista de usuarios
        """
        return list(self._users.values())
    
    def update(self, user: User) -> Optional[User]:
        """
        Actualiza un usuario.
        
        Args:
            user: Usuario a actualizar
            
        Returns:
            Usuario actualizado o None si no existe
        """
        if user.user_id in self._users:
            self._users[user.user_id] = user
            return user
        return None
    
    def delete(self, user_id: int) -> bool:
        """
        Elimina un usuario.
        
        Args:
            user_id: ID del usuario
            
        Returns:
            True si se eliminó, False si no existía
        """
        if user_id in self._users:
            del self._users[user_id]
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
