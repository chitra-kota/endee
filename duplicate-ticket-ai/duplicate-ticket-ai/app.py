from sentence_transformers import SentenceTransformer
import endee

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read existing tickets
with open("tickets.txt", "r") as f:
    tickets = [line.strip() for line in f.readlines()]

# Convert tickets to vectors
embeddings = model.encode(tickets)

# Create Endee database
db = endee.Database("ticket_db")

# Insert tickets into Endee vector database
for i, vector in enumerate(embeddings):
    db.insert(
        id=i,
        vector=vector,
        metadata={"ticket": tickets[i]}
    )

print("Smart Duplicate Ticket Detector")

# Get new ticket from user
query = input("Enter new support ticket: ")

# Convert query to vector
query_vector = model.encode([query])[0]

# Search similar ticket in Endee
results = db.search(query_vector, top_k=1)

print("Similar existing ticket:", results[0]["metadata"]["ticket"])
