from dataclasses import dataclass


@dataclass
class AccessibilityPreferences:
    """Preferencias persistentes que hacen accesible la experiencia para un usuario."""

    user_id: str
    text_scale: float = 1.0
    high_contrast: bool = False
    voice_guidance_enabled: bool = False
    haptics_enabled: bool = True
    reduce_motion: bool = False

    def validate(self) -> None:
        if not 0.8 <= self.text_scale <= 2.0:
            raise ValueError("text_scale must be between 0.8 and 2.0")
