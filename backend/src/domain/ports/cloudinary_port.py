from abc import ABC, abstractmethod
from typing import Optional

class CloudinaryPort(ABC): # Clase abstracta para representar puertos de Cloudinary
    @abstractmethod
    def upload_image(self, file_data: bytes, filename: str) -> dict: # Método para subir una imagen a Cloudinary
        pass
        
    @abstractmethod
    def delete_image(self, public_id: str) -> bool: # Método para eliminar una imagen de Cloudinary
        pass
