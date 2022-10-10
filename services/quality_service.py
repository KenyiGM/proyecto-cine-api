from sqlalchemy.orm import Session
from models.quality import Quality
from schemas.quality_schema import QualityCreate, QualityUpdate, QualityUpdateByIsActive

def get_qualities(db:Session):
    return db.query(Quality).all()

def get_quality(db:Session, quality_id : int):
    return db.query(Quality).filter(Quality.id==quality_id).first()

def insert_quality(db:Session, quality:QualityCreate):
    new_quality = Quality(name = quality.name)
    db.add(new_quality)
    db.commit()
    db.refresh(new_quality)
    return new_quality

def update_quality(db:Session, quality_id:int, quality:QualityUpdate):
    edit_quality = db.query(Quality).get(quality_id)
    edit_quality.name = quality.name
    edit_quality.update_at = quality.update_at
    db.commit()
    return edit_quality

def update_quality_by_is_active(db:Session, quality_id:int, quality:QualityUpdateByIsActive):
    edit_quality           = db.query(Quality).get(quality_id)
    edit_quality.is_active = quality.is_active
    edit_quality.update_at = quality.update_at
    db.commit()
    return edit_quality

def delete_quality(db:Session, quality_id:int):
    quality = db.query(Quality).get(quality_id)
    db.delete(quality)
    db.commit()
    return "delete"