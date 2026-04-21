from fastapi import APIRouter, Body
from app.services import feelings_service as service
from app.schemas.feelings_schemas import FeelingsWeeklyReport

router = APIRouter(prefix="/feelings")

@router.post(path="/")
async def feelings_weekly_clasification(feelings_weekly_report: FeelingsWeeklyReport = Body()):
    return await service.feelings_weekly_clasification(feelingsWeeklyReport=feelings_weekly_report)