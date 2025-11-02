run:
	@cd .. && uvicorn workout_api.main:app --reload --port 8001

create-migrations:
	@PYTHONPATH=..:$$PYTHONPATH alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=..:$$PYTHONPATH alembic upgrade head