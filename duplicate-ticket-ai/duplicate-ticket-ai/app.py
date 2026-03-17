from sentence_transformers import SentenceTransformer
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load tickets
with open("tickets.txt", "r") as f:
    tickets = [line.strip() for line in f.readlines()]

# Convert tickets to vectors
ticket_vectors = model.encode(tickets)

print("Smart Duplicate Ticket Detector")
print()

new_ticket = input("Enter new support ticket: ")

# Convert new ticket to vector
new_vector = model.encode([new_ticket])[0]

# Calculate similarity
similarities = np.dot(ticket_vectors, new_vector) / (
    np.linalg.norm(ticket_vectors, axis=1) * np.linalg.norm(new_vector)
)

best_match_index = np.argmax(similarities)

print()
print("Most similar existing ticket:")
print(tickets[best_match_index])