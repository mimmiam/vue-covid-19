from fastapi import FastAPI , Request
from fastapi.middleware.cors import CORSMiddleware

# uvicorn main:app --reload --host 0.0.0.0 --port 8000 --workers 4

class PatientToDay:
    case_new: int
    case_infected_check_point: int
    case_infected_community: int
    case_from_foreign_no_q: int
    case_from_foreign_in_q: int


class ReceivedTreatment:
    case_new: int
    case_total: int
    case_in_treatment: int
    percentage: float


class PatientStatistics:
    total_case: int
    total_case_domestic: int
    total_case_check_point: int
    total_case_from_foreign: int
    total_case_in_q: int


class DiedSatatistics:
    total_died: int
    case_new_died: int
    percentage: float


class RegionStatistics:
    bkk_and_nearby: int
    north_region: int
    central_region: int
    esan_region: int
    south: int


class CoviceResult:
    DataDate: str
    PatientToDay: PatientToDay
    ReceivedTreatment: ReceivedTreatment
    PatientStatistics: PatientStatistics
    RegionStatistics: RegionStatistics
    DiedSatatistics: DiedSatatistics


app = FastAPI()
temp_result = CoviceResult()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def mock_date() -> CoviceResult:
    temp_result.PatientToDay = PatientToDay()
    temp_result.ReceivedTreatment = ReceivedTreatment()
    temp_result.PatientStatistics = PatientStatistics()
    temp_result.RegionStatistics = RegionStatistics()
    temp_result.DiedSatatistics = DiedSatatistics()

    temp_result.DataDate = '9 มีนาคม 2564'
    temp_result.PatientToDay.case_new = 60
    temp_result.PatientToDay.case_infected_check_point = 22
    temp_result.PatientToDay.case_infected_community = 21
    temp_result.PatientToDay.case_from_foreign_no_q = 2
    temp_result.PatientToDay.case_from_foreign_in_q = 15

    temp_result.ReceivedTreatment.case_new = 74
    temp_result.ReceivedTreatment.case_total = 25851
    temp_result.ReceivedTreatment.case_in_treatment = 565
    temp_result.ReceivedTreatment.percentage = 97.55

    temp_result.PatientStatistics.total_case = 26501
    temp_result.PatientStatistics.total_case_domestic = 23623
    temp_result.PatientStatistics.total_case_check_point = 14709
    temp_result.PatientStatistics.total_case_from_foreign = 2878
    temp_result.PatientStatistics.total_case_in_q = 2257

    temp_result.DiedSatatistics.total_died = 85
    temp_result.DiedSatatistics.case_new_died = 0
    temp_result.DiedSatatistics.percentage = 0.32

    temp_result.RegionStatistics.bkk_and_nearby = 3958
    temp_result.RegionStatistics.north_region = 504
    temp_result.RegionStatistics.central_region = 21020
    temp_result.RegionStatistics.esan_region = 191
    temp_result.RegionStatistics.south = 828

    return temp_result

@app.middleware("http")
async def mock_data_root(request: Request, call_next):
    await mock_date()
    return await call_next(request)

@app.get("/api/v1/covid")
async def read_root() -> CoviceResult:
    return temp_result

@app.get("/api/v1/covid/PatientToDay")
async def read_PatientToDay() -> PatientToDay:
    return temp_result.PatientToDay

@app.get("/api/v1/covid/ReceivedTreatment")
async def read_ReceivedTreatment() -> ReceivedTreatment:
    return temp_result.ReceivedTreatment    

@app.get("/api/v1/covid/PatientStatistics")
async def read_PatientStatistics() -> PatientStatistics:
    return temp_result.PatientStatistics    

@app.get("/api/v1/covid/DiedSatatistics")
async def read_DiedSatatistics() -> DiedSatatistics:
    return temp_result.DiedSatatistics    

@app.get("/api/v1/covid/RegionStatistics")
async def read_RegionStatistics() -> RegionStatistics:
    return temp_result.RegionStatistics        