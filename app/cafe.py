from datetime import date, timedelta
from .errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    UnknownVaccinationDateError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if vaccine_details := visitor.get("vaccine", None):
            if expiration_date := vaccine_details.get("expiration_date"):
                current_date = date.today()
                delta_date: timedelta = expiration_date - current_date
                if delta_date.days < 0:
                    raise OutdatedVaccineError(
                        "Visit is refused if vaccination expired"
                    )
                else:
                    if visitor.get("wearing_a_mask", False):
                        return f"Welcome to {self.name}"
                    else:
                        raise NotWearingMaskError(
                            "Visit is refused without a mask"
                        )  # noqa: E501

            else:
                raise UnknownVaccinationDateError(
                    "Visit is refused if vaccination date is unknown"
                )
        else:
            raise NotVaccinatedError("Visit is refused without a vaccination")
