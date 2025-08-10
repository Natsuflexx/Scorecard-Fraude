from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel, create_model,Field
from fastapi.middleware.cors import CORSMiddleware


class MonthEnum(Enum):
    nov = "nov"
    dec = "dec"
    apr = "apr"
    jul = "jul"
    oct = "oct"
    jun = "jun"
    sep = "sep"
    feb = "feb"
    may = "may"
    aug = "aug"
    jan = "jan"
    mar = "mar"

class WeekOfMonthEnum(Enum):
    first = 1
    second = 2
    third = 3
    fourth = 4
    fifth = 5

class DayOfWeekEnum(Enum):
    thursday = "thursday"
    wednesday = "wednesday"
    tuesday = "tuesday"
    friday = "friday"
    monday = "monday"
    sunday = "sunday"
    saturday = "saturday"

class MakeEnum(Enum):
    toyota = "toyota"
    mazda = "mazda"
    honda = "honda"
    chevrolet = "chevrolet"
    pontiac = "pontiac"
    otros = "otros"


class AccidentAreaEnum(Enum):
    urban = "urban"
    rural = "rural"


class DayOfWeekClaimedEnum(Enum):
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    otros = "otros"


class MonthClaimedEnum(Enum):
    january = "jan"
    february = "feb"
    march = "mar"
    april = "apr"
    may = "may"
    june = "jun"
    july = "jul"
    august = "aug"
    september = "sep"
    october = "oct"
    november = "nov"
    december = "dec"


class WeekOfMonthClaimedEnum(Enum):
    first = 1
    second = 2
    third = 3
    fourth = 4
    fifth = 5


class SexEnum(Enum):
    male = "male"
    female = "female"

class MaritalStatusEnum(Enum):
    single = "single"
    married = "married"
    otros = "otros"

class VehiclePriceEnum(Enum):
    low = "less than 20000"
    mid = "20000 to 290000"
    high = "30000 to 39000"
    very_high = "more than 69000"
    otros = "otros"

class DeductibleEnum(Enum):
    v_300 = 300
    v_400 = 400
    v_500 = 500
    v_700 = 700

class DaysPolicy_AccidentEnum(Enum):
    more_than_30 = "more than 30"
    otros = "otros"

class DaysPolicy_ClaimEnum(Enum):
    more_than_30 = "more than 30"
    otros = "otros"

class PastNumberOfClaimsEnum(Enum):
    more_than_4 = "more than 4"
    one = 1
    two_to_four = "2 to 4"
    none = "none"

class AgeOfVehicleEnum(Enum):
    more_than_7 = "more than 7"
    seven_years = "7 years"
    six_years = "6 years"
    otros = "otros"
    five_years = "5 years"

class AgeOfPolicyHolderEnum(Enum):
    fiftyone_to_sixtyfive = "51 to 65"
    fortyone_to_fifty = "41 to 50"
    thirtysix_to_forty = "36 to 40"
    thirtyone_to_thirtyfive = "31 to 35"
    otros = "otros"

class PoliceReportFiledEnum(Enum):
    otros = "otros"
    no = "no"

class WitnessPresentEnum(Enum):
    no = "no"
    otros = "otros"

class AgentTypeEnum(Enum):
    otros = "otros"
    external = "external"

class NumberOfSupplimentsEnum(Enum):
    more_than_5 = "more than 5"
    three_to_five = "3 to 5"
    none = "none"
    one_to_two = "1 to 2"

class AddressChangeClaimEnum(Enum):
    no_change = "no change"
    otros = "otros"

class NumberOfCarsEnum(Enum):
    one_vehicle ="1 vehicle"
    otros = "otros"

class YearEnum(Enum):
    year_1994 = 1994
    year_1995 = 1995
    year_1996 = 1996
                 
class ClienteDatos(BaseModel):
    Month: MonthEnum
    WeekOfMonth: WeekOfMonthEnum
    DayOfWeek: DayOfWeekEnum
    Make: MakeEnum
    AccidentArea: AccidentAreaEnum
    DayOfWeekClaimed: DayOfWeekClaimedEnum
    MonthClaimed: MonthClaimedEnum
    WeekOfMonthClaimed: WeekOfMonthClaimedEnum
    Sex: SexEnum
    MaritalStatus: MaritalStatusEnum
    VehiclePrice: VehiclePriceEnum
    Deductible: DeductibleEnum
    DaysPolicyAccident: DaysPolicy_AccidentEnum
    DaysPolicyClaim: DaysPolicy_ClaimEnum
    PastNumberOfClaims: PastNumberOfClaimsEnum
    AgeOfVehicle: AgeOfVehicleEnum
    AgeOfPolicyHolder: AgeOfPolicyHolderEnum
    PoliceReportFiled: PoliceReportFiledEnum
    WitnessPresent: WitnessPresentEnum
    AgentType: AgentTypeEnum
    NumberOfSuppliments: NumberOfSupplimentsEnum
    AddressChangeClaim: AddressChangeClaimEnum
    NumberOfCars: NumberOfCarsEnum
    Year: YearEnum


#puntos_dict = {
#    "Month": {"nov": 29.60,"dec": 21.30,"apr": 10.10,"jul": 8.10,"oct": 6.30,"jun": 2.80,"sep": -3.40,"feb": -5.40,"may": -7.40,"aug": -8.90,"jan": -10.80,"mar": -20.40},
#    "WeekOfMonth": {1: -2.1,2: -4.2,3: -6.3,4: -8.4,5: -10.5},
#    "DayOfWeek": {"thursday": 10.10,"wednesday": 5.40,"tuesday": 4.40,"friday": 1.30,"monday": -1.50,"sunday": -7.60,"saturday": -11.20},
#    "Make": {"toyota": 2,"mazda": -3.2,"honda": 4.2,"chevrolet": 12.2,"pontiac": -3.6,"otros": -7.1},
#    "AccidentArea": {"urban": 3,"rural": -20.4},
#    "DayOfWeekClaimed": {"monday": 3.9,"tuesday": -2.1,"wednesday": 1.6,"thursday": -1.2,"friday": -2,"otros": -10.5},
#    "MonthClaimed": {"jan": -10.4,"feb": 0.1,"mar": -11.3,"apr": 0.1,"may": -10.2,"jun": 5.8,"jul": 19.4,"aug": -16.9,"sep": -5,"oct": 10.2,"nov": 20.2,"dec": 19.1},
#    "WeekOfMonthClaimed": {1: -2.8,2: -5.5,3: -8.3,4: -11.1,5: -13.8},
#    "Sex": {"male": -1.6,"female": 9.9},
#    "MaritalStatus": {"single": -1.4,"married": 0.6,"otros": 9.7},
#    "VehiclePrice": {"less than 20000": -41,"20000 to 290000": 7.8,"30000 to 39000": 7.1,"more than 69000": -9,"otros": -5.8},
#    "Deductible": {300: -54,400: -72,500: -89.9,700: -125.9},
#    "DaysPolicyAccident": {"more than 30": 0.1,"otros": -6.1},
#    "DaysPolicyClaim": {"more than 30": 0,"otros": 0.2},
#    "PastNumberOfClaims": {"more than 4": 38.2,1: 5,"2 to 4": -1.1,"none": -15.3},
#    "AgeOfVehicle": {"more than 7": 10,"7 years": 8.8,"6 years": -8.8,"otros": -16.6,"5 years": -21.9},
#    "AgeOfPolicyHolder": {"51 to 65": 24.2,"41 to 50": 16.3,"36 to 40": -2.2,"31 to 35": -7.5,"otros": -8.2},
#    "PoliceReportFiled": {"otros": 47,"no": -0.8},
#   "WitnessPresent": {"no": 0,"otros": 0},
#    "AgentType": {"otros": 109.2,"external": -1},
#    "NumberOfSuppliments": {"more than 5": 20.6,"3 to 5": 0.3,"none": -5.5,"1 to 2": -10.2},
#    "AddressChangeClaim": {"no change": 2.3,"otros": -22.9},
#    "NumberOfCars": {"1 vehicle": 0,"otros": 0.1},
#    "Year": {1994: 86.3,1995: 86.4,1996: 86.4}
#}
puntos_dict = {
    "Month": {
        "nov": 26.5,
        "dec": 19.1,
        "apr": 9.1,
        "jul": 7.3,
        "oct": 5.7,
        "jun": 2.5,
        "sep": -3.0,
        "feb": -4.9,
        "may": -6.7,
        "aug": -8.0,
        "jan": -9.7,
        "mar": -18.3
    },
    "WeekOfMonth": {
        1: -4.3,
        2: -8.6,
        3: -12.8,
        4: -17.1,
        5: -21.4
    },
    "DayOfWeek": {
        "thursday": 4.3,
        "wednesday": 2.3,
        "tuesday": 1.9,
        "friday": 0.6,
        "monday": -0.6,
        "sunday": -3.3,
        "saturday": -4.8
    },
    "Make": {
        "toyota": 42.2,
        "mazda": 40.2,
        "honda": 19.0,
        "chevrolet": 13.4,
        "pontiac": 6.7,
        "otros": 3.2
    },
    "AccidentArea": {
        "urban": 2.4,
        "rural": -16.6
    },
    "DayOfWeekClaimed": {
        "monday": 2.9,
        "tuesday": 2.5,
        "wednesday": 1.0,
        "thursday": -0.8,
        "friday": -1.2,
        "otros": -1.3
    },
    "MonthClaimed": {
        "nov": 21.5,
        "jul": 20.7,
        "dec": 20.4,
        "oct": 10.9,
        "jun": 6.2,
        "apr": 0.1,
        "feb": 0.1,
        "sep": -5.3,
        "may": -10.9,
        "jan": -11.1,
        "mar": -12.0,
        "aug": -18.0
    },
    "WeekOfMonthClaimed": {
        1: -3.3,
        2: -6.6,
        3: -10.0,
        4: -13.3,
        5: -16.6
    },
    "Sex": {
        "male": -1.0,
        "female": 6.1
    },
    "MaritalStatus": {
        "single": -0.2,
        "married": 0.3,
        "otros": 1.4
    },
    "VehiclePrice": {
        "less than 20000": 35.2,
        "20000 to 290000": 8.2,
        "30000 to 39000": 7.4,
        "more than 69000": -9.4,
        "otros": -11.5
    },
    "Deductible": {
        300: -36.0,
        400: -48.0,
        500: -60.1,
        700: -84.1
    },
    "DaysPolicyAccident": {
        "more than 30": 0.1,
        "otros": -7.3
    },
    "DaysPolicyClaim": {
        "more than 30": 0.1,
        "otros": -4.7
    },
    "PastNumberOfClaims": {
        "more than 4": 37.2,
        1: 4.9,
        "2 to 4": -1.1,
        "none": -14.9
    },
    "AgeOfVehicle": {
        "more than 7": 10.5,
        "7 years": 9.5,
        "6 years": 8.5,
        "otros": -8.0,
        "5 years": -20.2
    },
    "AgeOfPolicyHolder": {
        "51 to 65": 20.5,
        "41 to 50": 13.9,
        "36 to 40": -1.6,
        "31 to 35": -6.1,
        "otros": -9.9
    },
    "PoliceReportFiled": {
        "otros": 40.0,
        "no": -0.7
    },
    "WitnessPresent": {
        "no": 0,
        "otros": 0
    },
    "AgentType": {
        "otros": 98.6,
        "external": -0.9
    },
    "NumberOfSuppliments": {
        "more than 5": 16.9,
        "3 to 5": 0.3,
        "none": -4.5,
        "1 to 2": -8.4
    },
    "AddressChangeClaim": {
        "no change": 4.0,
        "otros": -36.4
    },
    "NumberOfCars": {
        "1 vehicle": 0,
        "otros": 0
    },
    "Year": {
        1994: 68.6,
        1995: 68.6,
        1996: 68.7
    }
}


# Crear la API
app = FastAPI(title="API Scorecard Fraude")

# Función para calcular el score a partir de la scorecard
def calcular_score(datos: dict) -> dict:
    resultado_detalle = []
    score_total = 0

    for var, valor in datos.items():
        valor_normalizado = valor

        # Si es enum, obtener su valor real
        if isinstance(valor_normalizado, Enum):
            valor_normalizado = valor_normalizado.value

        # Para claves numéricas convertimos a int
        if var in ["WeekOfMonth", "WeekOfMonthClaimed", "Year", "Deductible"]:
            try:
                valor_normalizado = int(valor_normalizado)
            except Exception:
                pass

        # Para strings limpiar espacios y pasar a minúsculas (si aplica)
        if isinstance(valor_normalizado, str):
            valor_normalizado = valor_normalizado.strip().lower()

        # Buscar puntos en el diccionario
        puntos_var = 0
        categoria_usada = None
        if var in puntos_dict:
            if valor_normalizado in puntos_dict[var]:
                puntos_var = puntos_dict[var][valor_normalizado]
                categoria_usada = valor_normalizado
            else:
                if "otros" in puntos_dict[var]:
                    puntos_var = puntos_dict[var]["otros"]
                    categoria_usada = "otros"
                else:
                    puntos_var = 0
                    categoria_usada = "sin coincidencia"
        else:
            puntos_var = 0
            categoria_usada = "variable no definida"

        score_total += puntos_var

        resultado_detalle.append({
            "Variable": var,
            "Categoria_Introducida": valor,
            "Categoria_Usada": categoria_usada,
            "Puntos": puntos_var
        })

    return {
        "score_total": score_total,
        "detalle": resultado_detalle
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los headers
)

@app.get("/")
def raiz():
    return {"mensaje": "API Scorecard Fraude funcionando. Usa POST /predecir/ para calcular el score."}


@app.post("/predecir/")
def predecir_fraude(datos: ClienteDatos):
    datos_dict = datos.dict()
    resultado = calcular_score(datos_dict)
    riesgo = "Alto" if resultado["score_total"] > 600 else "Bajo"

    return {
        "score": resultado["score_total"],
        "nivel_riesgo": riesgo,
        "detalle_variables": resultado["detalle"]
    }
