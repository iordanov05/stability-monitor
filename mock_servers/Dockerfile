FROM python:3.12-slim
WORKDIR /mock
COPY mock_server.py .
RUN pip install fastapi uvicorn
CMD ["uvicorn", "mock_server:app", "--host", "0.0.0.0", "--port", "8080"]
