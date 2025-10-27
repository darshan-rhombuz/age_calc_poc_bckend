

```markdown
# 🧮 Age Calculator Backend API

A lightweight **Flask-based backend API** that calculates a person's **exact age in years, months, and days** from their Date of Birth (DOB).  
Built as part of a full-stack POC demonstrating API design, validation, and deployment on **Render (free tier)** for production use.

---

## 🚀 Features

- Calculate exact **age in years, months, days**
- Return **next birthday** and **days remaining**
- Handles leap years correctly (e.g., Feb 29)
- Validation for:
  - Date format (`YYYY-MM-DD`)
  - Invalid or future dates
  - DOB before 1900
- Includes a `/health` endpoint for service monitoring
- CORS enabled for frontend integration
- Ready for production deployment (via `gunicorn` + Render)

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend Framework | Flask (Python 3.13) |
| Server | Gunicorn |
| CORS | Flask-CORS |
| Hosting | Render (Free Tier) |
| API Format | REST (JSON) |

---

## 📂 Project Structure

```

age_calc_poc_bckend/
│
├── app.py                # Main Flask app file
├── requirements.txt      # Dependencies list
├── Procfile              # Gunicorn start command
└── README.md             # Project documentation

````

---

## 🔗 API Endpoints

### **1. Health Check**
**GET** `/api/health`

**Response:**
```json
{
  "status": "healthy",
  "service": "age-calculator-api",
  "version": "1.0.0"
}
````

---

### **2. Calculate Age**

**POST** `/api/calculate-age`

#### Request Body:

```json
{
  "dob": "1995-06-15"
}
```

#### Response:

```json
{
  "years": 30,
  "months": 4,
  "days": 12,
  "total_months": 364,
  "total_days": 11072,
  "next_birthday": "June 15, 2026 (217 days)",
  "dob": "June 15, 1995"
}
```

#### Error Examples:

```json
{ "error": "Invalid date format. Use YYYY-MM-DD" }
{ "error": "Date of birth cannot be in the future" }
{ "error": "Date of birth must be after 1900" }
```

---

## ⚙️ Local Setup (VS Code)

### **1️⃣ Clone Repository**

```bash
git clone https://github.com/<your-username>/age_calc_poc_bckend.git
cd age_calc_poc_bckend
```

### **2️⃣ Create Virtual Environment**

```bash
python -m venv myenv
source myenv/Scripts/activate      # (Windows PowerShell)
# or
source myenv/bin/activate          # (Mac/Linux)
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Run Locally**

```bash
python app.py
```

Flask will start on:
👉 `http://127.0.0.1:5000`

Test:

```
http://127.0.0.1:5000/api/health
```

---

## 🌐 Deploying on Render (Free Tier)

### **1️⃣ Push your code to GitHub**

```bash
git init
git add .
git commit -m "Initial commit - Flask Age Calculator API"
git branch -M main
git remote add origin https://github.com/<your-username>/age_calc_poc_bckend.git
git push -u origin main
```

### **2️⃣ Add `Procfile` (important)**

File: **Procfile**

```
web: gunicorn app:app
```

> If your file name is different (e.g., `main.py`), use:
>
> ```
> web: gunicorn main:app
> ```

---

### **3️⃣ Deploy to Render**

1. Go to [https://render.com](https://render.com)
2. Click **“New Web Service”**
3. Connect your GitHub repo
4. Set:

   * **Environment:** `Python 3`
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn app:app`
5. Deploy 🎉

---

### **4️⃣ Verify Deployment**

Visit:

```
https://<your-app-name>.onrender.com/api/health
```

You should see:

```json
{
  "status": "healthy",
  "service": "age-calculator-api",
  "version": "1.0.0"
}
```

---

## 🧩 Frontend Integration (React Example)

Your deployed backend (Render) can be consumed by any frontend.

Example React code:

```javascript
const API_URL = "https://age-calc-poc-bckend.onrender.com/api/calculate-age";

async function calculateAge(dob) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ dob })
  });
  const data = await response.json();
  console.log(data);
}
```

---

## 🔒 CORS Note

Flask-CORS is enabled globally:

```python
from flask_cors import CORS
CORS(app)
```

This allows cross-origin requests from your frontend (local or hosted).

---

## 🧑‍💻 Author

**Darshan Agrawal**


---

## 🧾 Requirements Summary

| Dependency | Version |
| ---------- | ------- |
| Flask      | 3.1.2   |
| Flask-CORS | 4.0.0   |
| Gunicorn   | 23.0.0  |
| Python     | 3.13+   |

---

**✅ Final Deployment URL:**
👉 [https://age-calc-poc-bckend.onrender.com](https://age-calc-poc-bckend.onrender.com)

```

