from sentence_transformers import SentenceTransformer
import numpy as np

tickets = [
"Cannot connect to office WiFi",
"Laptop battery not charging",
"Email login not working",
"Printer not responding",
"VPN connection failing",
"Computer running very slow",
"Software installation error",
"Keyboard not working properly",
"Internet disconnecting frequently",
"Unable to access company portal"
]

model = SentenceTransformer('all-MiniLM-L6-v2')

ticket_embeddings = model.encode(tickets)

print("Smart Duplicate Ticket Detector")

query = input("Enter new support ticket: ")

query_embedding = model.encode([query])

similarity = np.dot(ticket_embeddings, query_embedding.T)

best_match = tickets[np.argmax(similarity)]

print("Similar existing ticket:", best_match)
