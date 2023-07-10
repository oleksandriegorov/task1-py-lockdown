class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class UnknownVaccinationDateError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass
