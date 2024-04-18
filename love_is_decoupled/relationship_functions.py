from typing import Dict, List, Literal, Set
from .hero import Hero
from .partner import Partner, HERO
from .wellness import Wellness


def get_wellness(partner: Partner) -> Literal[Wellness.JUST_FINE, Wellness.UNHEALTHY]:
    """
    Returns Just fine if partner is communicative and Unhealthy otherwise.
    Returns:
        Literal[Wellness.JUST_FINE, Wellness.UNHEALTHY]
    """
    if partner.communicate() is None:
        return Wellness.UNHEALTHY
    return Wellness.JUST_FINE


def get_life_plan(hero: Hero) -> Dict[str, int]:
    """Construct a life plan for the Hero. The Hero will first check
    in with their partner to see what their priorities are. The Hero
    will then construct a life plan based on their own interests and
    their partner's priorities.

    Returns:
        Dict[str, int]: Interests and their values for the life plan
    """
    partner_priorities = get_partner_priorities(hero.partner)
    return {
        interest: 2 if interest in partner_priorities else 1
        for interest in hero.interests
    }


def get_new_partner(hero: Hero, partner_interests: List[str] = None) -> None:
    hero.partner = Partner(partner_interests)


def should_find_new_partner(partner: Partner, critical_priority: str = HERO) -> bool:
    """
    Check that a critical priority is in a partners list.
    Returns:
        bool: If caller should find a new partner or not.

    """
    return critical_priority not in get_partner_priorities(partner)


def get_partner_priorities(partner: Partner) -> Set[str]:
    partner_priorities = partner.list_priorities()
    if not partner_priorities:
        return set()
    return set(partner_priorities)
