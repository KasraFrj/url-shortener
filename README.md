# 🔗 URL Shortener API

A fast and lightweight URL shortening service built with **FastAPI**, **PostgreSQL**, and **Redis** caching.

---

## ✨ Features

- 🔗 **URL Shortening** — Convert long URLs into 6-character short codes
- ⚡ **Redis Caching** — Frequently accessed URLs are cached for faster redirects
- 📊 **Click Tracking** — Track how many times each short link has been clicked
- 📄 **Auto Documentation** — Interactive Swagger UI at `/docs`

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Cache | Redis |
| Server | Uvicorn |

---

## 📁 Project Structure

```
url-shortener/
├── app/
│   ├── main.py          # App entry point & routes
│   ├── database.py      # DB connection & session
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database & cache operations
│   └── redis_client.py  # Redis connection
├── requirements.txt
└── .env
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- Redis

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/KasraFrj/url-shortener.git
cd url-shortener

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Linux/Mac: source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/url_shortener
REDIS_HOST=localhost
REDIS_PORT=6379
```

### Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

---

## 📖 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/shorten` | Create a short URL |
| GET | `/{short_code}` | Redirect to original URL |
| GET | `/stats/{short_code}` | Get click stats for a short URL |

> 📝 Full interactive documentation available at `http://localhost:8000/docs`

---

## ⚡ How Caching Works

When a short URL is accessed for the first time, the original URL is fetched from PostgreSQL and stored in Redis with a **1-hour expiry**. Subsequent requests are served directly from Redis, making redirects significantly faster.

```
Request → Check Redis → Hit? → Redirect (fast)
                      → Miss? → Query PostgreSQL → Cache in Redis → Redirect
```

---

## 📬 Contact

**Kasra** — [@KasraFrj](https://github.com/KasraFrj)
