# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String, Table
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Customer(Base):
    __tablename__ = 'Customer'

    CPR = Column(INTEGER(11), primary_key=True)
    Name = Column(String(45))
    Email = Column(String(45))
    PhoneNumber = Column(INTEGER(11))


class Producer(Base):
    __tablename__ = 'Producer'

    CVR = Column(INTEGER(11), primary_key=True)
    Name = Column(String(45))
    PhoneNumber = Column(INTEGER(11))
    Adress = Column(String(45))

    Supplier = relationship('Supplier', secondary='Producer_has_Supplier')


class Statistic(Base):
    __tablename__ = 'Statistics'

    idStatistics = Column(INTEGER(11), primary_key=True)
    CustomerCount = Column(INTEGER(11))
    ArtistCustomerCount = Column(INTEGER(11))
    SessionCount = Column(INTEGER(11))
    AppliedInkColorCount = Column(INTEGER(11))


class Supplier(Base):
    __tablename__ = 'Supplier'

    CVR = Column(INTEGER(11), primary_key=True)
    Name = Column(String(45))
    PhoneNumber = Column(String(45))
    Adress = Column(String(45))

'''
t_appointmenttattooview = Table(
    'appointmenttattooview', metadata,
    Column('DateTime', DateTime),
    Column('SessionLenght', INTEGER(11)),
    Column('CustomerName', String(45)),
    Column('TattooparlotName', String(75)),
    Column('ArtistName', String(45)),
    Column('Description', String(200)),
    Column('PlacementOnBody', String(45))
)'''


class Ink(Base):
    __tablename__ = 'Ink'

    BatchNumber = Column(INTEGER(11), primary_key=True, nullable=False)
    Brand = Column(String(45))
    ColorCode = Column(String(15))
    ExperationDate = Column(DateTime)
    Price = Column(INTEGER(11))
    Producer_CVR = Column(ForeignKey('Producer.CVR'), primary_key=True, nullable=False, index=True)

    Producer = relationship('Producer')
    Tattoo = relationship('Tattoo', secondary='Tattoo_has_Ink')


t_Producer_has_Supplier = Table(
    'Producer_has_Supplier', metadata,
    Column('Producer_CVR', ForeignKey('Producer.CVR'), primary_key=True, nullable=False, index=True),
    Column('Supplier_CVR', ForeignKey('Supplier.CVR'), primary_key=True, nullable=False, index=True)
)


class Tattooparlor(Base):
    __tablename__ = 'Tattooparlor'

    CVR = Column(INTEGER(11), primary_key=True, nullable=False)
    Name = Column(String(75))
    Adress = Column(String(45))
    PhoneNumber = Column(INTEGER(11))
    Email = Column(String(45))
    Statistics_idStatistics = Column(ForeignKey('Statistics.idStatistics'), primary_key=True, nullable=False, index=True)
    Supplier_CVR = Column(ForeignKey('Supplier.CVR'), primary_key=True, nullable=False, index=True)

    Statistic = relationship('Statistic')
    Supplier = relationship('Supplier')


class Artist(Base):
    __tablename__ = 'Artist'

    CPR = Column(INTEGER(11), primary_key=True)
    Name = Column(String(45))
    PhoneNumber = Column(INTEGER(11))
    Email = Column(String(45))
    Price = Column(INTEGER(11))
    Tattooparlor_CVR = Column(ForeignKey('Tattooparlor.CVR'), nullable=False, index=True)

    Tattooparlor = relationship('Tattooparlor')


t_Parlor_has_Ink = Table(
    'Parlor_has_Ink', metadata,
    Column('Ink_batchnumber', ForeignKey('Ink.BatchNumber'), index=True),
    Column('Parlor_storageID', ForeignKey('Tattooparlor.CVR'), index=True),
    Column('Quantity', INTEGER(11))
)


class Appointment(Base):
    __tablename__ = 'Appointment'

    idAppointment = Column(INTEGER(11), primary_key=True, nullable=False)
    DateTime = Column(DateTime)
    SessionLenght = Column(INTEGER(11))
    Customer_CPR = Column(ForeignKey('Customer.CPR'), primary_key=True, nullable=False, index=True)
    Tattooparlor_CVR = Column(ForeignKey('Tattooparlor.CVR'), primary_key=True, nullable=False, index=True)
    Artist_CPR = Column(ForeignKey('Artist.CPR'), nullable=False, index=True)

    Artist = relationship('Artist')
    Customer = relationship('Customer')
    Tattooparlor = relationship('Tattooparlor')


class Tattoo(Base):
    __tablename__ = 'Tattoo'

    idTattoo = Column(INTEGER(11), primary_key=True, nullable=False)
    Description = Column(String(200))
    PlacementOnBody = Column(String(45))
    Appointment_idAppointment = Column(ForeignKey('Appointment.idAppointment'), primary_key=True, nullable=False, index=True)

    Appointment = relationship('Appointment')


t_Tattoo_has_Ink = Table(
    'Tattoo_has_Ink', metadata,
    Column('Tattoo_idTattoo', ForeignKey('Tattoo.idTattoo'), primary_key=True, nullable=False, index=True),
    Column('Ink_BatchNumber', ForeignKey('Ink.BatchNumber'), primary_key=True, nullable=False, index=True)
)
