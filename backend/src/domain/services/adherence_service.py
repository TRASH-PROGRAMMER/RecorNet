from src.repositories.adherence_repository import AdherenceRepository

class AdherenceService:
    def __init__(self, adherence_repository: AdherenceRepository) -> None:
        self._adherence_repository = adherence_repository
        def calculate_adherence(self, user_id: str) -> float:
         """Calcula el porcentaje de adherencia del usuario."""
         adherence = self._adherence_repository.get_by_user_id(user_id)
         if not adherence:
             return 0.0
         return sum(adherence) / len(adherence)
    
