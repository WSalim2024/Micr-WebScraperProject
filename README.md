# 🌐 Micr-WebScraper Dashboard: Pro Data Acquisition Hub

## 📋 Project Overview
The **Micr-WebScraper Dashboard** is a professional-grade web application built to solve the "unstructured data" problem in modern AI workflows. Specifically designed with **RAG (Retrieval-Augmented Generation)** and **Agentic AI** in mind, this tool provides a dual-engine interface to extract both on-page text and linked documents (PDFs, DOCs, etc.) with high precision.

By implementing **Separation of Concerns**, the application allows users to target specific data types independently, minimizing noise and maximizing the quality of the data fed into LLMs like **Claude**, **Gemini**, or **ChatGPT**.

---

## 🛠 Features & Capabilities

### 1. 📄 Intelligent Text & Table Scraper
* **Heuristic DOM Extraction:** Specifically targets `<p>` tags and `<table>` structures to isolate meaningful content from webpage "noise" (menus, ads, footers).
* **Automated Table Formatting:** Utilizes Pandas to detect HTML tables and convert them into a readable, structured string format.
* **Resilient Networking:** Uses custom `User-Agent` strings and a 10-second timeout to handle server delays and basic anti-scraping filters.

### 2. 📁 Document Discovery Engine
* **Extension Matching:** Scans all anchor (`<a>`) tags for file extensions: `.pdf`, `.docx`, `.txt`, and `.csv`.
* **URL Resolution:** Employs `urllib.parse` to resolve "Relative URLs" (e.g., `/reports/data.pdf`) into "Absolute URLs" for direct download/ingestion.
* **Batch Detection:** Capable of listing multiple documents found across a single page in one execution.

### 3. 🛡 Professional "Polite" Scraping Standards
* **Rate Limiting:** Implements a mandatory `time.sleep(1)` delay between requests to prevent server overloading—an essential ethical scraping practice.
* **Comprehensive Error Handling:** Uses `try-except` blocks to catch and report HTTP errors (404, 403) and Connection Timeouts without crashing the application.

---

## 💻 Technical Architecture
The project follows a **Modular Monolith** pattern. The Flask backend acts as a "Controller," routing requests to specialized logic functions for either text processing or document identification.

* **Backend:** Python 3.10+
* **Framework:** Flask (Routing & Templating)
* **HTML Parsing:** BeautifulSoup4 (LXML engine)
* **Data Processing:** Pandas (Table extraction)
* **Networking:** Requests (with binary stream support)

---

## 🚀 Deployment & Installation Guide

### 1. Environment Setup
Clone the repository and initialize a Virtual Environment to keep the system clean:
```bash
git clone [https://github.com/YOUR_USERNAME/Micr-WebScraperProject.git](https://github.com/YOUR_USERNAME/Micr-WebScraperProject.git)
cd Micr-WebScraperProject
python -m venv venv
.\venv\Scripts\activate