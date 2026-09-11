# schemas/country.py
import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

class CountryBase(BaseModel):
    name: str
    capital: str | None = None
    phone_code: str | None = None
    continent: str | None = None
    currency: str | None = None
    coordinate: dict[str, float] | None = None
    description: str | None = None
    population: float | None = None
    timezones: list[str] | None = None
    is_active: bool = True


class CountryExternalRead(BaseModel):
    name: str
    capital: str | None = None
    continent: str | None = None
    coordinate: dict[str, float] | None = None
    currency: str | None = None
    description: str | None = None
    population: float | None = None
    phone_code: str | None = None
    timezones: list[str] = []


class CountryExternalResponse(BaseModel):
    message: str
    countries: list[CountryExternalRead]


class CountrySyncResponse(BaseModel):
    message: str
    countries: list["CountryRead"]


class CountryCreate(CountryBase):
    created_by: uuid.UUID | None = None
    updated_by: uuid.UUID | None = None


class CountryUpdate(BaseModel):
    name: str | None = None
    code: str | None = None
    phone_code: str | None = None
    continent: str | None = None
    currency: str | None = None
    is_active: bool | None = None
    updated_by: uuid.UUID | None = None


class CountryRead(CountryBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    created_by: uuid.UUID | None
    updated_by: uuid.UUID | None
    created_at: datetime
    updated_at: datetime