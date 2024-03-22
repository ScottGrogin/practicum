from .hero import Hero
from .wellness import Wellness
from .partner import HERO

"""
Geezum creepers, I am finding it really hard to validate the expected behaviors
of our Hero.

The tests are taking forever to run. Its slowing down my feedback,
and its making it a real pain to continue to develop the Hero.

There are a couple of cases that I'd like to test, but its just so painful.

Right now there is a lot of behavior that I'd like to test in the three public
methods (get_wellness, get_life_plan, should_find_new_partner) of the Hero class.
But I am finding it really hard to do so.

I'd also like to clean-codeify Hero, but without tests in place, that would be
irresponsible.
"""


class MockPartner:
    def __init__(self, priorities=None, communicates=True):
        self.priorities = priorities
        self.communicates = communicates

    def list_priorities(self):
        return self.priorities

    def communicate(self):
        if self.communicates:
            return "Howdy Partner!"
        return None


def test_hero_get_wellness_communicative_partner():
    """
    Given:
        - a Hero instance
        - a communicative partner

    When:
        - the get_wellness method is called

    Then:
        - the method should return Wellness.JUST_FINE
    """
    # Given
    hero = Hero(
        name="Pat", interests=["doesn't matter"], partner=MockPartner(None, True)
    )

    # When
    wellness = hero.get_wellness()

    # Then
    assert wellness == Wellness.JUST_FINE


def test_hero_get_wellness_non_communicative_partner():
    """
    Given:
        - a Hero instance
        - a non-communicative partner

    When:
        - the get_wellness method is called

    Then:
        - the method should return Wellness.UNHEALTHY
    """
    # Given
    hero = Hero(
        name="Kayleigh", interests=["Everything"], partner=MockPartner(None, False)
    )

    # When
    wellness = hero.get_wellness()

    # Then
    assert wellness == Wellness.UNHEALTHY


def test_hero_get_life_plan_no_overlapping_interests():
    """
    Given:
        - a Hero instance
        - a Partner that has no overlapping interests with the Hero

    When:
        - the get_life_plan method is called

    Then:
        - the method should return a dictionary with the interests as keys and the value as 1
    """
    # Given
    hero = Hero(
        name="Vic",
        interests=["entrepreneurship", "helping others"],
        partner=MockPartner(["Theft", "Giving people weird looks"], True),
    )

    # When
    life_plan = hero.get_life_plan()

    # Then
    assert life_plan == {"entrepreneurship": 1, "helping others": 1}


def test_hero_get_life_plan_overlapping_interests():
    """
    Given:
        - a Hero instance
        - a Partner that has overlapping interests with the Hero

    When:
        - the get_life_plan method is called

    Then:
        - the method should return a dictionary with the interests as keys and the value as 2
        for each overlapping interest and 1 otherwise.
    """
    # Given
    hero = Hero(
        name="Luna",
        interests=["Watching paint dry", "Bugs", "Delinquency", "Eating light bulbs"],
        partner=MockPartner(["Bugs", "Eating light bulbs"], True),
    )

    # When
    life_plan = hero.get_life_plan()

    # Then
    assert life_plan == {
        "Bugs": 2,
        "Eating light bulbs": 2,
        "Delinquency": 1,
        "Watching paint dry": 1,
    }


def test_hero_should_find_new_partner_prioritizing():
    """
    Given:
        - a Hero instance
        - a Partner with HERO in their list of priorities

    When:
        - the should_find_new_partner method is called

    Then:
        - the method should return False
    """
    # Given
    hero = Hero(
        name="Tracy",
        interests=["vaping", "Jean-Claude Van Damme"],
        partner=MockPartner([HERO, HERO, HERO, HERO, HERO, "HERO!!!"], True),
    )

    # When
    should_find_new_partner = hero.should_find_new_partner()

    # Then
    assert should_find_new_partner is False


def test_hero_should_find_new_partner_not_prioritizing():
    """
    Given:
        - a Hero instance
        - a Partner without HERO in their list of priorities

    When:
        - the should_find_new_partner method is called

    Then:
        - the method should return True
    """
    # Given
    hero = Hero(
        name="Abcde",
        interests=["Rocks", "Papers", "Scissors"],
        partner=MockPartner(None, True),
    )

    # When
    should_find_new_partner = hero.should_find_new_partner()

    # Then
    assert should_find_new_partner is True
