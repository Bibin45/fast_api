from fastapi import APIRouter, HTTPException
from .crud import get_all_items, get_item_by_id, create_item, update_item, delete_item
from .models import TodoModel, UpdateTodoModel, ResponseModal
from fastapi.responses import JSONResponse
from typing import List
import logging
router = APIRouter()


@router.get("/todos", response_model=ResponseModal[List[TodoModel]])
async def get_items():
    try:
        items = await get_all_items()
        response_content = ResponseModal[List[TodoModel]](  # Use the ResponseModal class
            status="success",
            message="Items retrieved successfully",
            data=items
        )
       
        return response_content
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.get("/todos/{id}", response_model=TodoModel)
async def get_item(id: str):
    item = await get_item_by_id(id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/todos/create", response_model=TodoModel)
async def create_new_item(item: TodoModel):
    new_item = await create_item(item.model_dump())
    return new_item


@router.put("/todos/{id}", response_model=TodoModel)
async def update_existing_item(id: str, item: UpdateTodoModel):
    updated = await update_item(id, item.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found or nothing to update")
    return await get_item_by_id(id)


@router.delete("/todos/{id}")
async def delete_existing_item(id: str):
    deleted = await delete_item(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
