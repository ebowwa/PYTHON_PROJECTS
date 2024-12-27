from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Dict

class AgreementQuery(BaseModel):
  receiving_institution_id: int
  sending_institution_id: int
  academic_year_id: int
  category_code: Optional[str] = None
  major: str
  major_code: str

class ArticulationAgreement(BaseModel):
  id: int
  receiving_institution_name: str
  sending_institution_name: str
  agreement_details: str
  
class AgreementDetail(BaseModel):
  agreement_id: str
  receiving_institution: str
  sending_institution: str
  agreement_date: Optional[str] = None

class Institution(BaseModel):
  ID: int
  Name: str
