# 🚀 URL Shortener with FastAPI, PostgreSQL, and Redis

یک سیستم پیشرفته و پرسرعت کوتاه‌کننده لینک (URL Shortener) که با **FastAPI** توسعه یافته و برای افزایش کارایی و سرعت از **Redis** به عنوان لایه Cache و از **PostgreSQL** به عنوان دیتابیس اصلی استفاده می‌کند. کل این اکوسیستم به صورت کاملاً ایزوله با **Docker** و **Docker Compose** ارکستره شده است.

---

## 🛠️ تکنولوژی‌های استفاده شده

* **Backend Framework:** FastAPI (Python 3.11)
* **Database:** PostgreSQL
* **Caching Layer:** Redis (Alpine-backed)
* **ORM:** SQLAlchemy
* **Containerization:** Docker & Docker Compose

---

## 🏗️ معماری و نحوه کارکرد (Workflow)

1. **ذخیره‌سازی لینک:** آدرس طولانی ارسال می‌شود، سیستم یک کد ۶ رقمی رندوم و منحصربه‌فرد تولید کرده و آن را در PostgreSQL ذخیره می‌کند.
2. **سیستم کشینگ (Cache):** هنگام درخواست ریدایرکت، سیستم ابتدا **Redis** را چک می‌کند:
   * **Cache Hit:** اگر لینک در ردیس باشد، بدون درگیر کردن دیتابیس اصلی، کاربر فوراً ریدایرکت می‌شود.
   * **Cache Miss:** اگر لینک در ردیس نباشد، از PostgreSQL خوانده شده، در ردیس کَش می‌شود (با TTL یک ساعته) و سپس ریدایرکت انجام می‌شود.
3. **آمار کلیک‌ها:** در هر بار ریدایرکت، یک واحد به تعداد `clicks` آن لینک در دیتابیس افزوده می‌شود.

---

## 🚀 راه اندازی پروژه با داکر (Quick Start)

هر کجای دنیا که هستید، بدون نیاز به نصب پایتون، پستگرس یا ردیس روی سیستم خود، می‌توانید پروژه را تنها با چند دستور ساده بالا بیاورید:

### ۱. کلون کردن پروژه
```bash
git clone [https://github.com/KasraFrj/url_shortener.git](https://github.com/KasraFrj/url_shortener.git)
cd url_shortener