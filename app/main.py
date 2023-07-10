from .cafe import Cafe
from .errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    num_masks_to_buy = 0
    vaccination_issue = False
    for person in friends:
        try:
            cafe.visit_cafe(visitor=person)
        except VaccineError:
            vaccination_issue = True
            break
        except NotWearingMaskError:
            num_masks_to_buy += 1
    if vaccination_issue:
        return "All friends should be vaccinated"
    elif num_masks_to_buy:
        return f"Friends should buy {num_masks_to_buy} masks"
    else:
        """I do not agree with "Avoid using unnecessary else"
        guideline in this particular case.
        This is because of several if clauses and that
        explicit is better than implicit."""
        return f"Friends can go to {cafe.name}"
