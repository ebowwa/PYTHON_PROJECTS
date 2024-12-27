from pydantic import BaseModel
from typing import Optional  # Add this import line

class AgreementQuery(BaseModel):
  receiving_institution_id: int
  sending_institution_id: int
  academic_year_id: int
  category_code: Optional[str] = None