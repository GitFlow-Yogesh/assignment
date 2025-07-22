# URL Shortener API

A simple and fully functional URL shortening API built using Python and Flask.  
It shortens long URLs into compact 6-character codes and supports redirection and analytics.

This was developed as part of the SDE Internship Assignment.

---

##  Tech Stack

- Python 3.8+
- Flask (for API)
- Pytest (for testing)
- In-memory storage using Python dictionaries

---

## Features

- `POST /api/shorten` – Generate a short code for any valid long URL
- `GET /<short_code>` – Redirects to the original URL
- `GET /api/stats/<short_code>` – Returns click count, creation time, and original URL
- In-memory data storage (no DB used)
- Fully tested (6 unit tests)

---

##  Getting Started

### 1. Clone or Download the Repository
```bash
git clone https://github.com/GitFlow-Yogesh/assignment.git
cd assignment
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python -m flask --app app.main run
```

The app will be live at:  
🌐 `http://localhost:5000`

---

##  API Endpoints

###  1. POST `/api/shorten`

**Description:** Create a short URL for a given long URL.

**Request Body:**
```json
{
  "url": "https://www.example.com/very/long/url"
}
```

**Response:**
```json
{
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123"
}
```

---

 2. GET `/<short_code>`

**Description:** Redirect to the original long URL.  
Returns a 302 redirect if valid, or 404 if the code doesn't exist.

---

 GET `/api/stats/<short_code>`

Description:Return analytics for the short URL.

Sample Response:
```json
{
  "url": "https://www.example.com/very/long/url",
  "clicks": 3,
  "created_at": "2025-07-22T14:30:00Z"
}



Expected Output:
```
6 passed
```

Curl Examples

```bash
# Shorten a URL
curl -X POST http://localhost:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/very/long/url"}'

# Redirect to original URL
curl -L http://localhost:5000/abc123

# Get analytics
curl http://localhost:5000/api/stats/abc123


Notes

- The app uses a Python dictionary to store data — no database is required.
- Data will reset when the app restarts (due to in-memory storage).
- All short codes are randomly generated and assumed unique.
- Basic URL validation is implemented using regex.
- The project follows clean code and separation of concerns.

---

Author

Yogesh  
Submission for SDE Internship Assignment – RetainSure  
GitHub: [GitFlow-Yogesh](https://github.com/GitFlow-Yogesh)

