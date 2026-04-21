from pydantic import BaseModel

class FeelingsWeeklyReport(BaseModel):
    monday: str
    tuesday: str
    wednesday: str
    thursday: str
    friday: str
    sunday: str
    saturday: str