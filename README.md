# ✉️ Notification CRUD App

A minimal Django CRUD app for sending and listing **Email** and **SMS** notifications.

---

## 🧩 Features

- Two notification types: **Email** and **SMS**
- Different form fields for each type
- Simple interface to submit notification data
- Submitted notifications are listed below the form
- No login required (demo setup)

---

## 📑 How It Works

1. **Select Type**: Click **Email** or **SMS** button  
2. **Fill Form**:  
    - For Email, enter recipient email (`@gmail.com`), subject, and body  
    - For SMS, enter mobile number, and message body  
3. **Submit**:  
    - Submitted notification is saved (Create)
    - All notifications are visible in a table (Read)
    - Add edit/delete features for Update/Delete

---

## 🖥️ UI Overview

- Email/SMS selection buttons  
- Dynamic form changes fields based on type  
- Table displays all notifications with details (ID, Type, Email/Mobile, Subject/Body, Action)  
- "No notification found" message for empty list

---

## 📝 Demo Table Layout

| ID | Type   | Email/Mobile      | Subject | Body       | Action    |
|----|--------|-------------------|---------|------------|-----------|
| 1  | Email  | xyz@gmail.com     | Hello   | Test mail  | Edit/Delete|
| 2  | SMS    | 9876543210        |         | Test sms   | Edit/Delete|

---

## 📚 Tech Stack

- Django (backend, routing, models)
- HTML & CSS (basic styling)
- No authentication/authorization for demo
