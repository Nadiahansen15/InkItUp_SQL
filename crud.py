from typing import List
from sqlalchemy.orm import Session
from inkitup_sql.models import Appointment
from inkitup_sql.schemas import CreateAndUpdateAppointment

# Function to get list of car info
def get_all_apointments(session: Session, limit: int, offset: int) -> List[Appointment]:
    return session.query(Appointment).offset(offset).limit(limit).all()
