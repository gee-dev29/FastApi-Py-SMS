from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from StudentManagementSystem.Config.database import get_db
from StudentManagementSystem.Controller.CountryController import CountryController
from StudentManagementSystem.Schema.Country import (
  CountrySyncResponse,
)
from StudentManagementSystem.Service.CountryService import countryApiClient

serviceRouter = APIRouter(prefix="/services", tags=["Services"])

@serviceRouter.get("/countries", response_model=CountrySyncResponse)
def get_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  countryController = CountryController()
  try:
    countries = countryController.get_countries(db=db, skip=skip, limit=limit)
    if(not countries):
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No countries found",
      )
    return {
      "message": "Countries retrieved successfully",
      "countries": countries,
    }
  except HTTPException:
    raise
  except Exception as error:
    raise HTTPException(
      status_code=status.HTTP_502_BAD_GATEWAY,
      detail="Country service is unavailable",
    ) from error


@serviceRouter.post("/countries/sync", response_model=CountrySyncResponse)
def sync_countries(db: Session = Depends(get_db)):
  try:
    countries = CountryController.sync_countries(db)
    return {
      "message": "Countries synchronized successfully",
      "countries": countries,
    }
  except Exception as error:
    db.rollback()
    raise HTTPException(
      status_code=status.HTTP_502_BAD_GATEWAY,
      detail="Country service is unavailable",
    ) from error


@serviceRouter.get("/countries/{country_code}/states")
def get_states(country_code: str):
  countryClient = countryApiClient()
  try:
    states = countryClient.getStates(country_code)
    return {
      "message": "States retrieved successfully",
      "states": states,
    }
  except Exception as error:
    raise HTTPException(
      status_code=status.HTTP_502_BAD_GATEWAY,
      detail="Country service is unavailable",
    ) from error