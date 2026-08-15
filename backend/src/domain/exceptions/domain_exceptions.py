class DomainException(Exception):  # clase para representar excepciones de dominio
    pass

class UserNotFound(DomainException):  # clase para representar excepciones de usuario no encontrado
    pass

class UnauthorizedAccess(DomainException): # clase para representar excepciones de acceso no autorizado
    pass

class MedicationNotFound(DomainException): # clase para representar excepciones de medicamento no encontrado
    pass

class DuplicateMedication(DomainException): # clase para representar excepciones de medicamento duplicado
    pass

class InvalidDosage(DomainException): # clase para representar excepciones de dosis inválida
    pass

class TreatmentNotFound(DomainException): # clase para representar excepciones de tratamiento no encontrado
    pass
