from abc import ABC, abstractmethod
from typing import Optional
import cloudinary
from cloudinary.uploader import upload, destroy
class CloudinaryPort(ABC): # Clase abstracta para representar puertos de Cloudinary
    @abstractmethod
    def upload_image(self, file_data: bytes, filename: str) -> dict: # Método para subir una imagen a Cloudinary
        pass
        
    @abstractmethod
    def delete_image(self, public_id: str) -> bool: # Método para eliminar una imagen de Cloudinary
        pass

class CloudinaryConnection:
    def __init__(self):
        self.cloudinary_client = cloudinary
        cloudinary.config(
            cloud_name="dld27w62u",
            api_key="197348884741175",
            api_secret="[ENCRYPTION_KEY]"
        )
    def upload_image(self, file_data: bytes, filename: str) -> dict:
        return self.cloudinary_client.uploader.upload(file_data, filename)
    def delete_image(self, public_id: str) -> bool:
        self.cloudinary_client.uploader.destroy(public_id)
        return True


