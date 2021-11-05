from typing import List, Optional
from pydantic import BaseModel
import datetime

# TO support creation and update APIs
class CreateAndUpdateAppointment(BaseModel):
    DateTime = datetime
    SessionLenght = int
    Customer_CPR = int
    Tattooparlor_CVR =int
    Artist_CPR = int


# TO support list and get APIs
class Appointment(CreateAndUpdateAppointment):
    idAppointment: int

    class Config:
        orm_mode = True


# To support list cars API
class PaginatedAppointmentInfo(BaseModel):
    limit: int
    offset: int
    data: List[Appointment]