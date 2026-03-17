# Smart Duplicate Ticket Detector

## Project Overview
This project detects duplicate IT support tickets using semantic similarity.

Many organizations receive multiple support tickets describing the same issue in different words. This system helps identify similar tickets automatically.

## How It Works
1. Existing tickets are converted into embeddings.
2. Embeddings are compared using vector similarity.
3. When a new ticket is entered, the system retrieves the most similar existing ticket.

## Technologies Used
- Python
- Sentence Transformers
- Vector similarity search
- Endee Vector Database

## Example

New Ticket:
WiFi not connecting in office

Similar Existing Ticket:
Cannot connect to office WiFi

## Use Case
Helpdesk automation systems can use this approach to reduce duplicate tickets.
