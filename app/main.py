from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field
import uuid
from typing import List, Optional

app = FastAPI()

# Skema Input
class PengirimanIn(BaseModel):
    no_resi: str = Field(..., pattern=r"^JKT\d{7}$", description="Nomor resi dengan pola JKT0000000")
    berat_kg: float = Field(..., gt=0, le=50, description="Berat paket dalam kg (maksimal 50kg)")

# Skema Output (berbeda dari Input, id dibuat oleh server)
class PengirimanOut(PengirimanIn):
    id: str

# In-memory database untuk keperluan testing
db_pengiriman = {}

@app.post("/api/pengiriman", status_code=status.HTTP_201_CREATED, response_model=PengirimanOut)
def create_pengiriman(pengiriman: PengirimanIn, response: Response):
    new_id = str(uuid.uuid4())
    # Generate schema output
    data = PengirimanOut(id=new_id, **pengiriman.model_dump())
    db_pengiriman[new_id] = data
    
    # Header Location wajib untuk status 201 Created
    response.headers["Location"] = f"/api/pengiriman/{new_id}"
    return data

@app.get("/api/pengiriman", response_model=List[PengirimanOut])
def get_all_pengiriman(skip: int = 0, limit: int = 10, search: Optional[str] = None):
    results = list(db_pengiriman.values())
    
    # Filter by search
    if search:
        search_lower = search.lower()
        results = [
            item for item in results
            if search_lower in item.no_resi.lower()
        ]
    
    # Pagination
    return results[skip : skip + limit]

@app.get("/api/pengiriman/{id}", response_model=PengirimanOut)
def get_pengiriman_by_id(id: str):
    if id not in db_pengiriman:
        raise HTTPException(status_code=404, detail="Data Pengiriman tidak ditemukan")
    return db_pengiriman[id]