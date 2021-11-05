from fastapi import APIRouter, Depends, HTTPException, FastAPI
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from InkItUp_SQL.crud import get_all_apointments
from Database import get_db
#from exceptions import CarInfoException
from InkItUp_SQL.schemas import Appointment, CreateAndUpdateAppointment, PaginatedAppointmentInfo

router = APIRouter()

# Example of Class based view
@cbv(router)
class Appointments:
    session: Session = Depends(get_db)

    # API to get the list of car info
    @router.get("/apointments", response_model=PaginatedAppointmentInfo)
    def list_apointments(self, limit: int = 10, offset: int = 0):

        apointments_list = get_all_apointments(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": apointments_list}

        return response
