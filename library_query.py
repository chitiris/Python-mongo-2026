from pymongo import MongoClient

def main():
    # 1. Σύνδεση με τη MongoDB
    connection_string = "mongodb://admin:secret@localhost:27017/"
    client = MongoClient(connection_string)

    db_name = "LibraryExample"
    collection_name = "books"

    print("=== Έλεγχος Σύνδεσης και Δομής ===")

    # 2. Έλεγχος αν υπάρχει η βάση δεδομένων
    # Ζητάμε από τον client μια λίστα με όλες τις βάσεις
    available_dbs = client.list_database_names()
    if db_name in available_dbs:
        print(f"[OK] Η βάση δεδομένων '{db_name}' βρέθηκε!")
    else:
        print(f"[ΠΡΟΣΟΧΗ] Η βάση '{db_name}' δεν βρέθηκε στις υπάρχουσες βάσεις: {available_dbs}")
        print("Θυμήσου: Στη MongoDB, η βάση δημιουργείται πραγματικά μόνο όταν μπει το πρώτο δεδομένο!")

    # Επιλέγουμε τη βάση
    db = client[db_name]

    # 3. Έλεγχος αν υπάρχει το collection
    # Ζητάμε από τη βάση μια λίστα με όλα τα collections της
    available_collections = db.list_collection_names()
    if collection_name in available_collections:
        print(f"[OK] Το collection '{collection_name}' βρέθηκε!")
    else:
        print(f"[ΠΡΟΣΟΧΗ] Το collection '{collection_name}' δεν βρέθηκε στα υπάρχοντα: {available_collections}")

    print("==================================\n")

    # Επιλέγουμε το collection
    books_collection = db[collection_name]

    # 4. Ορισμός και Εκτέλεση του ερωτήματος (Query)
    query = { "available_copies": { "$gte": 5 } } #$gte = Greater Than or Equal
    #{"author": "George Orwell" }
    #{ "available_copies": { "$gte": 5 } }
    
    print("Αναζήτηση για βιβλία με 5 ή περισσότερα αντίτυπα...\n")
    print("-" * 50)
    
    results = books_collection.find(query)

    # 5. Εμφάνιση των αποτελεσμάτων
    count = 0
    for book in results:
        count += 1
        title = book.get("title", "Άγνωστος Τίτλος")
        author = book.get("author", "Άγνωστος Συγγραφέας")
        copies = book.get("available_copies", 0)
        
        print(f"Τίτλος: {title}")
        print(f"Συγγραφέας: {author}")
        print(f"Διαθέσιμα Αντίτυπα: {copies}")
        print("-" * 50)

    print(f"\nΒρέθηκαν συνολικά {count} βιβλία.")

if __name__ == "__main__":
    main()