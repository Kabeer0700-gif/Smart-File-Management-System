# Smart File Management System (SFMS)

## Overview

Smart File Management System (SFMS) is a Python-based application designed to automate file organization, duplicate detection, file searching, report generation, and storage management. The system scans directories recursively, categorizes files based on their extensions, identifies duplicate files using hashing techniques, and generates detailed reports for efficient file management.

This project demonstrates practical usage of Python's file handling capabilities, object-oriented programming principles, data structures, exception handling, JSON configuration, logging, and database integration.

---

## Features

### Directory Scanning

* Recursively scan directories and subdirectories.
* Collect file metadata:

  * File Name
  * Extension
  * Size
  * Creation Date
  * Modification Date
  * Absolute Path

### File Organization

* Automatically classify files into categories:

  * Images
  * Documents
  * Videos
  * Audio
  * Archives
  * Programs
  * Others
* Move files into their respective folders.

### Duplicate File Detection

* Detect duplicate files using SHA-256 hashing.
* Display duplicate groups.
* Option to remove duplicate files safely.

### Search Engine

Search files using:

* File Name
* File Extension
* File Size Range
* Date Range

### Statistics Dashboard

Generate statistics including:

* Total Number of Files
* Category-wise Distribution
* Total Storage Usage
* Largest File
* Smallest File

### Recycle Bin Management

* Safe deletion of files.
* Restore deleted files to original location.
* Permanent file removal option.

### Report Generation

Generate reports in:

* TXT Format
* CSV Format

### Logging System

Track all activities such as:

* File Organization
* Duplicate Removal
* Directory Scanning
* File Restoration

### Configuration Management

Customize file categories using JSON configuration files.

---

## Technologies Used

* Python 3.x
* pathlib
* hashlib
* shutil
* logging
* json
* csv
* sqlite3
* object-oriented programming

---

## Project Structure

```text
SmartFileManagementSystem/
│
├── main.py
│
├── managers/
│   ├── file_manager.py
│   ├── organize_manager.py
│   ├── duplicate_manager.py
│   ├── search_manager.py
│   ├── recycle_manager.py
│
├── models/
│   └── file_info.py
│
├── reports/
│   └── report_generator.py
│
├── database/
│   └── sfms.db
│
├── config/
│   └── config.json
│
├── logs/
│   └── system.log
│
├── recycle_bin/
│
└── data/
```

---

## System Architecture

```text
User
 │
 ▼
FileManager
 │
 ├── Organizer
 │
 ├── DuplicateFinder
 │
 ├── SearchEngine
 │
 ├── StatisticsManager
 │
 └── ReportGenerator
```

---

## Class Responsibilities

### FileInfo

Represents metadata of a file.

### FileManager

Handles directory scanning and metadata collection.

### Organizer

Classifies and organizes files into folders.

### DuplicateFinder

Detects duplicate files using file hashes.

### SearchEngine

Provides advanced file searching functionality.

### StatisticsManager

Calculates storage and file statistics.

### ReportGenerator

Generates CSV and TXT reports.

### RecycleBinManager

Manages deleted files and restoration.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/SmartFileManagementSystem.git
cd SmartFileManagementSystem
```

### Run Project

```bash
python main.py
```

---

## Example Workflow

1. User selects a directory.
2. System scans all files recursively.
3. Metadata is collected and stored.
4. Files are categorized automatically.
5. Duplicate files are detected.
6. Reports are generated.
7. User can search, organize, delete, or restore files.

---

## Future Enhancements

* GUI using Tkinter or PyQt
* Drag-and-drop file management
* Cloud storage integration
* Real-time directory monitoring
* Multi-threaded scanning
* AI-based file categorization
* Data visualization dashboard

---

## Learning Outcomes

This project helps developers gain practical experience with:

* File Handling
* Pathlib Library
* Object-Oriented Programming
* Exception Handling
* JSON Processing
* Logging
* SQLite Databases
* Hashing Algorithms
* Software Design Principles
* Modular Programming

---

## License

This project is developed for educational and learning purposes.
