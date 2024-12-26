## **🚀 O'rnatish va ishga tushirish**

Quyidagi bosqichlar orqali loyihani mahalliy mashinangizda ishga tushiring:

### **1. Muhitni sozlash**

Loyiha uchun talab qilinadigan barcha paketlarni o'rnatish uchun virtual muhit yarating va faollashtiring:
```bash
python -m venv .venv
source .venv/bin/activate   # Windows uchun: .venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Migratsiyalarni qo'llash**

Django migratsiyalarini ishlatib, ma'lumotlar bazasini sozlang:
```bash
python manage.py migrate
```

### **4. Superuser yaratish**

Admin panelga kirish uchun superuser yarating:
```bash
python manage.py createsuperuser
```

### **5. Loyihani ishga tushirish**

Mahalliy serverni ishga tushiring:
```bash
python manage.py runserver
```
Mahalliy serveringiz quyidagi URL manzilida ishga tushadi: http://localhost:8000

## **🔑 Muhim sozlamalar**

Loyiha .env faylidan foydalanadi. Quyida .env.example faylidan foydalanib o'z .env faylingizni yarating



