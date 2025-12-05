# 📜 Certificate Generator Dashboard

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Production-success.svg)

**Advanced system for automatic PDF certificate generation from Google Docs/Slides templates with a professional web interface**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Reviews](#-client-reviews)

</div>

---

## 🌟 Overview

A comprehensive and integrated system for automatically generating certificates from Google Docs or Google Slides templates, with full support for Arabic and English variables, and a modern web interface for operation management.

### ⚡ Performance
- **High Speed**: Up to 500 certificates/minute (with 10 service accounts)
- **Parallel Processing**: Automatic distribution across multiple service accounts
- **Smart Retry**: Automatic retry for failed certificates

## ⚙️ Requirements

- Python 3.8+
- Google Service Accounts (5-10 accounts recommended for optimal performance)
- Google Drive Shared Folder

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/mohamed-alawy/certificate-dashboard.git
cd certificate-dashboard
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
.\venv\Scripts\activate  # On Windows
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Add Service Accounts
- Create service accounts from Google Cloud Console
- Download JSON files and save them in the project folder
- Name them as: `service-account-1.json`, `service-account-2.json`, etc.
- See `example-service-account.json` for the required format

### 5. Run the Application
```bash
python app.py
```

Open browser at: `http://localhost:5000`

## 🚀 Deployment on Server

### Quick Method
```bash
# Run in background
nohup python app.py > app.log 2>&1 &
```

### With Systemd (Recommended)
Create file `/etc/systemd/system/certificate-dashboard.service`:
```ini
[Unit]
Description=Certificate Generator Dashboard
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/certificate-dashboard
ExecStart=/path/to/certificate-dashboard/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl enable certificate-dashboard
sudo systemctl start certificate-dashboard
sudo systemctl status certificate-dashboard
```

## 📝 Usage

### Web Interface

1. **Select Template**
   - Choose a Google Docs or Google Slides template
   - Template must contain variables in format `<<VARIABLE>>`
   - Example: `<<Name>>`, `<<Date>>`, `<<Course Name>>`

2. **Select Folder**
   - Choose Google Drive folder to save final certificates (PDF)

3. **Select Google Sheet**
   - Choose a spreadsheet containing trainee data
   - System will automatically detect:
     - Name column (searches for "name" or "اسم")
     - Link column (creates "Certificate Link" column if not found)

4. **Start Generation**
   - Click "Start Generation"
   - System will process all names without links
   - Track progress through the interface

### Auto-Watch Mode
- Enable "Auto-Watch" to automatically process new names
- Checks spreadsheet every 30 seconds (customizable)
- Perfect for live events

## 🔧 Features

### ⚡ High Performance
- **Parallel Processing**: Automatic distribution across multiple service accounts
- **Speed**: Up to 50 certificates/minute per account
- **Smart Retry**: Automatic retry for failed certificates

### 🧹 Automatic Name Cleaning
System automatically removes titles and prefixes:
- **Arabic**: استاذ، دكتور، مهندس، محامي، الأستاذ، الدكتور, etc.
- **English**: Dr, Eng, Mr, Mrs, Prof, Captain, etc.
- **Customizable**: Add or remove words from the list

### 📄 Comprehensive Template Support
- ✅ **Google Docs**: Text documents
- ✅ **Google Slides**: Presentations
- 🔍 **Auto-Detection**: Automatically recognizes template type

### 🔤 Advanced Variable Support
- **Variable Format**: `<<VARIABLE>>`
- **Arabic Support**: `<<الاسم>>`, `<<التاريخ>>`
- **English Support**: `<<NAME>>`, `<<DATE>>`
- **Space Support**: `<<اسم المتدرب>>`, `<<Course Name>>`

### 👁️ Monitoring and Tracking
- **Live Dashboard**: Real-time progress tracking
- **Detailed Logs**: Track all operations
- **Statistics**: Total, Completed, Failed, Speed

## 📂 Project Structure

```
certificate-dashboard/
├── app.py                          # Main Flask + SocketIO server
├── templates/
│   └── index.html                  # User interface (SPA)
├── requirements.txt                # Dependencies
├── .gitignore                      # Files excluded from Git
├── example-service-account.json    # Service account example
├── service-account-*.json          # Service accounts (not in Git)
└── README.md                       # This file
```

## 🔐 Security and Privacy

- ✅ **Protected Service Files**: `.gitignore` prevents uploading service accounts
- ✅ **Limited Permissions**: Service accounts only have Drive permissions
- ✅ **No Local Storage**: No sensitive data saved locally
- ✅ **HTTPS Ready**: Can run behind Nginx with SSL

## 🐛 Troubleshooting

### Service Accounts Not Working?
```bash
# Verify files are loaded correctly
ls -la *.json

# Check file permissions
chmod 600 *.json
```

### Slow Generation?
- Add more service accounts (5-10 recommended)
- Check Google API limits for accounts

### Permission Errors?
- Ensure template and folders are shared with all service accounts
- Check read/write permissions

### Service Not Working?
```bash
# Check logs
tail -50 app.log

# Check processes
ps aux | grep python

# Restart
pkill -f 'python.*app.py'
python app.py
```

## 🎯 Use Cases

- 📜 **Training Course Certificates**: Generate thousands of certificates for trainees
- 🏆 **Recognition Certificates**: Thank you and appreciation certificates for employees
- 🎓 **Graduation Certificates**: University or school certificates
- 📋 **Bulk Documents**: Any document requiring individual data customization

## 🤝 Contributing

Contributions are welcome! Open an Issue or Pull Request.

## 📄 License

MIT License - Use freely in personal and commercial projects

## ⭐ Client Reviews

### 5/5 Stars Rating on Mostaql

> **Excellent experience with a professional developer**
> 
> Dealt with complete professionalism and flexibility. Engineer Mohamed executed the project with high precision and was responsive to all modifications and additional requirements.
> 
> **Highlights:**
> - ✅ Precise requirements implementation
> - ✅ Fast and continuous communication
> - ✅ High code quality
> - ✅ Post-delivery support
> - ✅ Flexibility in modifications
> 
> **Result:** A complete system working with high efficiency that saved us hours of manual work.
> 
> Highly recommend working with him! 👍
> 
> — **Client from Mostaql Platform** | [Review Link](https://mostaql.com/u/mohamed_alawy/reviews/9436518)

---

<div align="center">

**Made with ❤️ in Egypt**

If you like this project, don't forget to give it a ⭐

[Contact me on Mostaql](https://mostaql.com/u/mohamed_alawy) • [GitHub](https://github.com/mohamed-alawy)

</div>
