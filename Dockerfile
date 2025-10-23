# ---- Base ----
FROM python:3.12-slim

# ---- System deps ----
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# ---- Workdir ----
WORKDIR /app

# ---- Python deps ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy source ----
COPY app ./app
COPY model ./model

# ---- Expose (optional, Render ignores) ----
EXPOSE 5000

# ---- Run: Use $PORT if set (Render), else 5000 (local) ----
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-5000}"]