from fastapi import APIRouter, Depends, HTTPException
from services.quality_service import *
from databases.repository import get_db
from schemas.quality_schema import Quality

quality = APIRouter()

@quality.get('/quality', response_model=list[Quality])
async def get_all(db:Session = Depends(get_db)):
    return get_qualities(db)

@quality.get('/quality/{quality_id}', response_model=Quality)
async def get_one(quality_id:int , db:Session = Depends(get_db)):
    quality = get_quality(db, quality_id)
    if quality is None:
        raise HTTPException(status_code=404, detail="quality not found")
    return quality

@quality.post('/quality', response_model=Quality)
async def insert_one(quality:QualityCreate, db:Session = Depends(get_db)):
    return insert_quality(db, quality)

@quality.put('/quality/{quality_id}', response_model=Quality)
async def update_one(quality_id:int, quality:QualityUpdate, db:Session = Depends(get_db)):
    return update_quality(db, quality_id, quality)

@quality.put('/quality/{quality_id}/is_active', response_model=Quality)
async def update_one_by_is_active(quality_id:int, quality:QualityUpdateByIsActive, db:Session = Depends(get_db)):
    return update_quality_by_is_active(db, quality_id, quality)

@quality.delete('/quality/{quality_id}')
async def delete_one(quality_id:int, db:Session = Depends(get_db)):
    return delete_quality(db, quality_id)