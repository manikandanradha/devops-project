FROM python:3.9-alpine AS builder
RUN apk add --no-cache gcc musl-dev
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt
FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "python_script.py"]