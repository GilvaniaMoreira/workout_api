from fastapi import APIRouter
from workout_api.controller.atleta import router as atleta
from workout_api.controller.categoria import router as categorias
from workout_api.controller.centro_treinamento import router as centro_treinamento

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categorias, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamento, prefix='/centros_treinamento', tags=['centros_treinamento'])