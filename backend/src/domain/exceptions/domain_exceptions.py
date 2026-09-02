class DomainException(Exception): # clase para representar excepciones de dominio
    """Excepción base para errores relacionados con las reglas del dominio"""
    def __init__(self, message: str): 
       super().__init__(message) 
       self.message = message 

class UserNotFound(DomainException):  # clase para representar excepciones de usuario no encontrado
    def __init__(self, message: str):
        self.message = message

class UnauthorizedAccess(DomainException): # clase para representar excepciones de acceso no autorizado
    def __init__(self, message: str):
        self.message = message

class MedicationNotFound(DomainException): # clase para representar excepciones de medicamento no encontrado
    def __init__(self, message: str):
        self.message = message

class DuplicateMedication(DomainException): # clase para representar excepciones de medicamento duplicado
    def __init__(self, message: str):
        self.message = message

class InvalidDosage(DomainException): # clase para representar excepciones de dosis inválida
    def __init__(self, message: str):
        self.message = message

class TreatmentNotFound(DomainException): # clase para representar excepciones de tratamiento no encontrado
    def __init__(self, message: str):
        self.message = message
