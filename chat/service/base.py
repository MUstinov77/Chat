from fastapi.exceptions import HTTPException
from sqlalchemy import delete, select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession


class BaseService:
    def __init__(self, session: AsyncSession, model):
        self.session = session
        self.model = model


    async def create(self, values: dict):
        record = self.model(**values)
        self.session.add(record)
        await self.session.commit()
        return record

    async def retrieve_one(self, obj_id: int, *args, **kwargs):
        query = select(self.model).where(self.model.id == obj_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def retrieve_all(self):
        query = select(self.model)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def retrieve_all_by_field(self, field, field_value):
        query = select(self.model).where(field == field_value) # noqa
        result = await self.session.execute(query)
        return result.scalars().all()

    async def update(self, obj_id: int, values: dict):
        query = (
            update(self.model)
            .where(self.model.id == obj_id)
            .values(**values)
            .returning(self.model)
        )
        result = await self.session.execute(query)
        return result.scalars().one()

    async def delete(self, obj_id: int):
        query = delete(self.model).where(self.model.id == obj_id).returning(self.model)
        result = await self.session.execute(query)
        return result.scalars().one()

    async def create_instance(self, values: dict):
        try:
            record = await self.create(values)
            await self.session.commit()
            return record
        except SQLAlchemyError:
            await self.session.rollback()
            raise HTTPException(
                status_code=500,
                detail="Error while creating instance",
            )

    async def update_instance(self, obj_id: int, values: dict):
        try:
            record = await self.update(obj_id, values)
            await self.session.commit()
            return record
        except SQLAlchemyError:
            await self.session.rollback()
            raise HTTPException(
                status_code=500,
                detail="Error while updating instance",
            )

    async def delete_instance(self, obj_id: int):
        try:
            record = await self.delete(obj_id)
            await self.session.commit()
            return record
        except SQLAlchemyError:
            await self.session.rollback()
            raise HTTPException(
                status_code=500,
                detail="Error while deleting instance",
            )