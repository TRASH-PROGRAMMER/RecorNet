from dataclasses import dataclass, field
from typing import Optional
from datetime import date, datetime

@dataclass
class Report:
    id: Optional[str] = None
    subject_user_id: str = ""
    created_by_user_id: str = ""
    period_from: date = field(default_factory=date.today)
    period_to: date = field(default_factory=date.today)
    content: dict = field(default_factory=dict)
    create_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())