from sqlalchemy.orm import Session

from StudentManagementSystem.Model.Country import CountryModel
from StudentManagementSystem.Service.CountryService import countryApiClient

class CountryController:
    @staticmethod
    def get_countries( db: Session, skip: int, limit: int) -> list[dict]:
        return db.query(CountryModel).offset(skip).limit(limit).all()

    @staticmethod
    def get_states(country_code: str) -> list[dict]:
        country = countryApiClient()
        return country.getStates(country_code)

    @staticmethod
    def sync_countries(db: Session) -> list[CountryModel]:
        countries = countryApiClient().getCountries()
        saved_countries = []

        for country_data in countries:
            country = (
                db.query(CountryModel)
                .filter(CountryModel.name == country_data["name"])
                .first()
            )
            if country is None:
                country = CountryModel(name=country_data["name"])
                db.add(country)

            for field in (
                "capital",
                "continent",
                "coordinate",
                "currency",
                "description",
                "population",
                "phone_code",
                "timezones",
            ):
                setattr(country, field, country_data[field])
            saved_countries.append(country)

        db.commit()
        for country in saved_countries:
            db.refresh(country)
        return saved_countries