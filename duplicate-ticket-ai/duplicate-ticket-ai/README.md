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
