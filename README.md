# Omnify Fitness Studio Booking API

A simple FastAPI backend for booking fitness classes (Yoga, Zumba, HIIT) with timezone support.

---

## 🚀 Features

- List all upcoming fitness classes
- Book a spot in a class
- View all bookings by client email
- Timezone conversion (classes stored in IST, viewable in any timezone)
- Input validation and error handling
- Logging for all major actions

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```sh
   git clone https://github.com/YOUR_USERNAME/omnify-booking-api.git
   cd omnify-booking-api
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Running Tests**
   ```sh
   python -c "from database import initialize_database; initialize_database()"
   ```
   
   ```sh
   pytest tests/test_api.py
   ```
   You should see output indicating all tests have passed

6. **Run the API**
   ```sh
   uvicorn main:app --reload
   ```
   - The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Sample cURL Requests

### Get all classes (in UTC)
```sh
curl -X GET "http://127.0.0.1:8000/classes?timezone=UTC"
```

### Book a class
```sh
curl -X POST "http://127.0.0.1:8000/book" \
  -H "Content-Type: application/json" \
  -d '{"class_id": 1, "client_name": "Steve Jobs", "client_email": "steve@apple.com"}'
```

### Get bookings by email
```sh
curl -X GET "http://127.0.0.1:8000/bookings?client_email=steve@apple.com"
```

---

## Sample Postman Collection

You can use the above endpoints in Postman as follows:

- **GET** `http://127.0.0.1:8000/classes?timezone=Asia/Kolkata`
- **POST** `http://127.0.0.1:8000/book`  
  Body (JSON):
  ```json
  {
    "class_id": 1,
    "client_name": "Steve Jobs",
    "client_email": "steve@apple.com"
  }
  ```
- **GET** `http://127.0.0.1:8000/bookings?client_email=steve@apple.com`

---

## Notes

- The database is SQLite and will be created automatically on first run.
- Seed data includes Yoga, Zumba, and HIIT classes.
- All class times are stored in IST; use the `timezone` query parameter to view in your local timezone.

