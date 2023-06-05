from policyengine_us.model_api import *
import numpy as np


class sc_eitc(Variable):
    value_type = float
    entity = TaxUnit
    label = "South Carolina EITC"
    unit = USD
    definition_period = YEAR
    reference = "https://dor.sc.gov/about/forms"

    def formula(tax_unit, period, parameters):
        eitc = tax_unit("earned_income_tax_credit", period)
        rate = parameters(period).gov.states.sc.tax.income.credits.eitc.rate
        return np.round(eitc * rate, 1)
