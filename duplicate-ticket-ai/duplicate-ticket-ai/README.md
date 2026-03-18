# Smart Duplicate Ticket Detector

## Project Overview
This project detects duplicate IT support tickets using semantic similarity.  
In many organizations, users submit support tickets describing the same issue in different words.  
This system helps identify similar tickets automatically so support teams can avoid duplicate work.

The project uses **Endee as a vector database** to store ticket embeddings and perform semantic similarity search.

---

## Problem Statement
Support teams often receive multiple tickets describing the same issue, such as WiFi not working or VPN connection problems.  
Because the descriptions may use different words, traditional keyword search fails to detect duplicates.

---

## Solution
This project converts ticket descriptions into **vector embeddings** using a machine learning model and stores them in a **vector database (Endee)**.  
When a new ticket is entered, the system finds the most semantically similar existing ticket.

---

## System Architecture
1. Load existing support tickets from `tickets.txt`
2. Convert each ticket into vector embeddings
3. Store embeddings in **Endee vector database**
4. Accept a new support ticket from the user
5. Convert the new ticket into a vector
6. Search the database for the most similar ticket
7. Return the closest matching ticket

---

## Technologies Used
- Python
- Sentence Transformers
- Endee Vector Database
- NumPy

---

## Project Structure
duplicate-ticket-ai/
│
├── app.py
├── streamlit_app.py
├── tickets.txt
├── requirements.txt
├── README.md
├── documentation.docx

---

## How to Run the Project

### Step 1: Install dependencies
pip install -r requirements.txt


### Step 2: Run the Streamlit application

python -m streamlit run streamlit_app.py


### Step 3: Open in browser

http://localhost:8501
---

## Example

### Input

Wifi not connecting in office


### Output

Similar existing ticket: Cannot connect to office WiFi


---

## Demo Output Screenshots

### Step 1: Application Interface


---

### Step 2: User Input
Example:
Wifi not connecting in office

<img width="1866" height="931" alt="Screenshot 2026-03-18 110117" src="https://github.com/user-attachments/assets/e4007a9b-12a1-4936-bfe6-2be90fb1ff41" />



---

### Step 3: Output Result
<img width="1860" height="882" alt="Screenshot 2026-03-18 110134" src="https://github.com/user-attachments/assets/0c57c59e-49f6-48be-82db-00fb634b524b" />


Figure 3: Duplicate Ticket Detection Result

---

## Features
- Detects duplicate tickets using semantic similarity
- Uses AI embeddings instead of keyword matching
- Simple and interactive Streamlit UI
- Demonstrates vector database usage
- Easy to extend for real-world systems

---

## Project Documentation
The complete project documentation is included in this repository:

`https://docs.google.com/document/d/1UHrwO4DpeefsUgJ56y2d-hZKmchwyJft/edit?usp=drivesdk&ouid=113187527691784958535&rtpof=true&sd=true`

---


## Benefits
- Reduces duplicate support tickets
- Saves time for support teams
- Improves issue resolution efficiency
- Demonstrates real-world AI application

---

## Future Improvements
- Integration with real helpdesk systems
- Large-scale ticket database
- Automated duplicate ticket merging
- Dashboard for monitoring issues

---

## Author
Kota Chanti Chitra Rekha  
B.Tech – Computer Science and Data Science  
Vignan's Lara Institute of Technology and Sciences  



