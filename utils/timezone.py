from datetime import datetime
import pytz

def convert_ist_to_timezone(dt_ist: datetime, target_timezone: str) -> datetime:
    ist = pytz.timezone("Asia/Kolkata")
    target = pytz.timezone(target_timezone)
    dt_ist = ist.localize(dt_ist)
    return dt_ist.astimezone(target)