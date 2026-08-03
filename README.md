# 🛡️ Phishing URL Detection System

A Python-based phishing URL analysis tool that identifies suspicious indicators in URLs and generates a detailed security risk assessment report.

This project analyzes multiple security parameters including URL structure, SSL certificates, DNS information, WHOIS domain intelligence, and VirusTotal reputation data to determine the risk level of a URL.

The goal of this project is to understand practical cybersecurity concepts such as phishing analysis, threat intelligence, security automation, and SOC analyst workflows.

---

## 🚀 Features

### 🔍 URL Feature Analysis

- URL parsing and validation
- HTTPS usage detection
- Long URL detection
- `@` symbol detection
- Multiple subdomain detection
- IP address detection inside URLs

### 🔐 SSL Certificate Analysis

- SSL certificate validation
- Certificate issuer information
- Certificate expiry details
- SSL error handling

### 🌐 DNS Analysis

- DNS resolution checking
- IP address extraction
- DNS failure detection

### 📅 Domain Intelligence

- WHOIS availability checking
- Domain age analysis
- Domain expiry information
- WHOIS error handling

### 🛡️ Threat Reputation Analysis

- VirusTotal API integration
- Malicious engine detection
- Suspicious engine detection
- Harmless engine count retrieval

### 📊 Risk Assessment

- Weighted risk scoring system
- Multiple security indicators combined
- LOW / MEDIUM / HIGH risk classification
- Detailed terminal-based security report

---

# 🏗️ Project Structure

```
Phishing-URL-Detection-System/

│
├── main.py                 # Main application workflow
├── parser.py               # URL parsing logic
├── validator.py            # URL validation
├── url_features.py         # URL-based phishing indicators
├── ssl_check.py            # SSL certificate analysis
├── dns_check.py            # DNS resolution analysis
├── domain_info.py          # WHOIS domain information
├── reputation.py            # VirusTotal reputation analysis
├── risk_engine.py          # Risk scoring and classification
├── report.py               # Final report generation
│
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

---

# 🧰 Technologies Used

- Python 3
- Regular Expressions
- urllib.parse
- SSL/TLS modules
- Socket programming
- DNS resolution
- WHOIS lookup
- VirusTotal API
- Requests
- python-dotenv

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/rawatsaransh/Phishing-URL-Detection-System.git
```

Navigate into the project directory:

```bash
cd Phishing-URL-Detection-System
```

---

## 2. Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

---

## 3. Configure VirusTotal API

Create a file named:

```
.env
```

inside the project directory.

Add your VirusTotal API key:

```env
VIRUSTOTAL_API_KEY=YOUR_API_KEY_HERE
```

⚠️ Do not upload your `.env` file to GitHub.

---

## 4. Run the Application

Execute:

```bash
python main.py
```

---

# 🔄 Working Flow

```
User Input URL

        ↓

URL Parsing & Validation

        ↓

URL Feature Extraction

        ↓

SSL Certificate Check

        ↓

DNS Resolution Check

        ↓

WHOIS Domain Analysis

        ↓

VirusTotal Reputation Check

        ↓

Risk Score Calculation

        ↓

Security Report Generation
```

---

# 📊 Risk Scoring

The system calculates a risk score based on multiple security indicators.

| Risk Score | Classification |
|------------|----------------|
| 0 - 5 | 🟢 LOW |
| 6 - 15 | 🟡 MEDIUM |
| 16+ | 🔴 HIGH |

---

# 🖥️ Example Output

Example phishing URL analysis:

```
PHISHING URL DETECTION REPORT

URL                   : http://google.com@evil.com/login
Domain                : evil.com

Overall Risk          : HIGH
Risk Score            : 17


URL FEATURES

HTTPS Used            : No
Contains @ Symbol     : Yes
Long URL              : Yes


SSL INFORMATION

SSL Certificate       : Valid


DNS INFORMATION

DNS Resolution        : Success


VIRUS-TOTAL REPUTATION

Malicious Engines     : 5
Suspicious Engines    : 2


FINAL RESULT

WARNING: This URL appears to be HIGH RISK.
Avoid visiting or entering sensitive information.
```

---

# 🧠 Detection Methodology

The system follows a heuristic-based detection approach.

Instead of depending on a single parameter, multiple security indicators are analyzed together:

- Suspicious URL patterns
- URL manipulation techniques
- Missing HTTPS
- SSL certificate status
- DNS behavior
- Domain information
- Threat intelligence reputation

These indicators are converted into a risk score to classify the URL.

---

# ⚠️ Limitations

- A valid SSL certificate does not guarantee that a website is trustworthy.
- WHOIS information may not be available for every domain.
- VirusTotal analysis requires an API key.
- Risk scoring is based on predefined security rules and heuristics.
- This tool is not a replacement for enterprise phishing detection systems.

---

# 🔮 Future Improvements

Possible enhancements:

- PDF and HTML report generation
- Web-based dashboard
- Batch URL scanning
- Additional threat intelligence sources
- Machine learning-based phishing detection
- Database integration for scan history

---

# 🎯 Project Objective

This project was developed to explore practical cybersecurity concepts:

- Blue Team operations
- SOC analyst workflows
- Threat intelligence
- Security automation
- Phishing analysis
- Defensive security techniques

---

# 📜 Disclaimer

This project is created for educational and defensive cybersecurity purposes only.

Do not scan or analyze websites without proper authorization.

---

# 📄 License

This project is licensed under the MIT License.
