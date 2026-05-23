#stage-1 - bulder
FROM python:3.11-slim AS builder
WORKDIR /app
RUN pip install --prefix=/install fastapi uvicorn redis


#stag-2 - runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py .
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port","8000"]


