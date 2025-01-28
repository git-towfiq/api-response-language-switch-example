# API Response Language Switch

This Django project provides API responses with **dynamic language translation**, supporting:
- **Custom Translations** stored in the database
- **LLM-Based Translations** (OpenAI, Claude, Mistral, Llama)
- **Field-Specific Translation** for selective API fields

## 🚀 Features
✅ **Dynamic language translation** via `lang` query param  
✅ **Supports multiple LLM providers** (`openai`, `anthropic`, `mistral`, `llama`)  
✅ **Custom translations API** to store user-defined translations  
✅ **Bulk import translations via command**  
✅ **Django REST Framework (DRF) API**  

---

## 🛠️ Setup Instructions

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo/api-response-language-switch-example.git
cd api-response-language-switch-example
```

### **2. Create & Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure `.env` File**
Create a `.env` file in the root directory and add:
```ini
DEBUG=True
SECRET_KEY=your_secret_key

# Database Config (SQLite / PostgreSQL)
DATABASE_URL=sqlite:///db.sqlite3

# LLM API Keys
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
MISTRAL_API_KEY=your_mistral_api_key
LLAMA_API_KEY=your_llama_api_key
```

### **5. Run Migrations**
```bash
python manage.py migrate
```

### **6. Create a Superuser**
```bash
python manage.py createsuperuser
```

### **7. Start the Server**
```bash
python manage.py runserver
```
> **API will be available at**: `http://127.0.0.1:8000/api/example-app/v1/`

---

## 🔥 API Endpoints

### **1. Add Custom Translations**
#### 📌 **Endpoint:** `POST /api/example-app/v1/translations/`
```json
{
    "key": "welcome",
    "language": "fr",
    "message": "Bienvenue"
}
```
**cURL Command**
```bash
curl -X POST http://127.0.0.1:8000/api/example-app/v1/translations/ \
     -H "Content-Type: application/json" \
     -d '{"key": "welcome", "language": "fr", "message": "Bienvenue"}'
```

---

### **2. Get API Response with Translation**
#### 📌 **Endpoint:** `GET /api/example-app/v1/example-endpoint/?lang=fr&llm_provider=openai`
```bash
curl -X GET "http://127.0.0.1:8000/api/example-app/v1/example-endpoint/?lang=fr&llm_provider=openai"
```
📌 **Response (French Translation)**
```json
{
    "success": true,
    "statusCode": 200,
    "message": "Opération réussie",
    "data": {
        "title": "Bienvenue sur notre plateforme",
        "description": "Ceci est une description de démonstration"
    }
}
```

---

### **3. Import Bulk Translations from JSON**
#### 📌 **Run the following command to import translations**
```bash
python manage.py load_translations translations.json
```
✅ **Example `translations.json`**
```json
[
    {"key": "welcome", "language": "fr", "message": "Bienvenue"},
    {"key": "success", "language": "es", "message": "Éxito"}
]
```

---

### **4. Use Other LLM Providers for Translation**
You can dynamically select **OpenAI, Anthropic (Claude), Mistral, or Llama**.

#### **Using Mistral**
```bash
curl -X GET "http://127.0.0.1:8000/api/example-app/v1/example-endpoint/?lang=de&llm_provider=mistral"
```

#### **Using Claude**
```bash
curl -X GET "http://127.0.0.1:8000/api/example-app/v1/example-endpoint/?lang=es&llm_provider=anthropic"
```

---

## 📂 Project Structure
```
api-response-language-switch-example/
│── config/                     # Django project configuration
│── apps/example_app/           # Main app containing API views
│   ├── api/v1/                 # API versioning
│   │   ├── urls.py             # API v1 routes
│   │   ├── views.py            # API logic
│   ├── middleware.py           # Translation middleware
│   ├── models.py               # Database models (Translation)
│   ├── serializers.py          # DRF serializers
│   ├── utils/                  # Utility functions
│   │   ├── response_formatter.py  # Response formatting with translation
│   │   ├── llm_service.py      # LLM translation service
│── requirements.txt            # Dependencies
│── manage.py                   # Django entry point
│── README.md                   # Documentation
│── .env                        # Environment variables
```

---

## 🛠️ **Development & Debugging**
### **Run Server in Debug Mode**
```bash
python manage.py runserver --settings=config.settings.dev
```

---

## 🚀 **Contributing**
We welcome contributions! Feel free to submit issues, feature requests, or pull requests.

---

