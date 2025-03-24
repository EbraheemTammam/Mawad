from pydantic import BaseModel
from datetime import datetime, time, timedelta
from uuid import UUID
from settings import logger

class WorkDay(BaseModel):
    id: UUID
    date: datetime
    start_time: time
    end_time: time
    break_hours: timedelta
    work_hours: timedelta
    driver_name: str
    notes: str

    @property
    def weekday(self) -> str:
        # Map weekday (0 = Monday, 6 = Sunday) to Arabic names
        weekdays = [
            "الإثنين",  # Monday
            "الثلاثاء", # Tuesday
            "الأربعاء", # Wednesday
            "الخميس",   # Thursday
            "الجمعة",   # Friday
            "السبت",    # Saturday
            "الأحد"     # Sunday
        ]
        return weekdays[self.date.weekday()]

    @classmethod
    def from_db_row(cls, row):
        try:
            logger.debug(f"Converting row: {row}")
            start_time_str = row[2]
            end_time_str = row[3]
            if len(start_time_str.split(":")) == 2:
                start_time_str += ":00"
            if len(end_time_str.split(":")) == 2:
                end_time_str += ":00"
            return cls(
                id=UUID(row[0]),
                date=datetime.fromisoformat(row[1]),
                start_time=datetime.strptime(start_time_str, "%H:%M:%S").time(),
                end_time=datetime.strptime(end_time_str, "%H:%M:%S").time(),
                break_hours=timedelta(hours=row[4]),
                work_hours=timedelta(hours=row[5]),
                driver_name=row[6],
                notes=row[7]
            )
        except Exception as e:
            logger.error(f"Error converting row {row}: {e}")
            raise
