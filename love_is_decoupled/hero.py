from typing import Optional, List
from .partner import Partner


class Hero:
    def __init__(
        self, name: str, interests: List[str], partner: Optional[Partner] = Partner()
    ):
        self.name = name
        self.interests = interests
        self.partner = partner
