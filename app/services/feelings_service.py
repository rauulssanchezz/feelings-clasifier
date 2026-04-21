from app.config.ia.configuration import ia_client
from app.schemas.feelings_schemas import FeelingsWeeklyReport

async def feelings_weekly_clasification(feelingsWeeklyReport: FeelingsWeeklyReport):
    content = f"Lunes: {feelingsWeeklyReport.monday}, Martes: {feelingsWeeklyReport.tuesday}, Miercoles: {feelingsWeeklyReport.wednesday}, Jueves: {feelingsWeeklyReport.thursday}, Viernes: {feelingsWeeklyReport.friday}, Sabado: {feelingsWeeklyReport.sunday}, Domingo: {feelingsWeeklyReport.saturday}"
    system_prompt = "Eres un analista de sentimientos experto. Analiza los diferentes sentimientos a lo largo de los dias de la semana y haz un resumen e indica la tendencia, intenta tambien predecir como se va a sentir la semana que viene si no cambia su rutina."

    content = await ia_client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": content,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return content.choices[0].message.content