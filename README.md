# 📚 University Library - MongoDB & Python Demo

Αυτό το repository περιέχει ένα εκπαιδευτικό παράδειγμα για την εκμάθηση της **MongoDB** (NoSQL βάση δεδομένων) και τη διασύνδεσή της με την **Python**. 

Δημιουργήθηκε για τις ανάγκες παρουσίασης σε φοιτητές, επιδεικνύοντας πώς στήνουμε μια βάση σε Docker, πώς εισάγουμε δεδομένα και πώς εκτελούμε queries μέσω κώδικα.

---

## 🛠️ Προαπαιτούμενα

Για να τρέξετε αυτό το project τοπικά στον υπολογιστή σας, θα χρειαστείτε:
1. [Docker](https://www.docker.com/) και Docker Compose
2. [MongoDB Compass](https://www.mongodb.com/products/compass) (Προαιρετικά, για γραφική διαχείριση της βάσης)
3. [Python 3](https://www.python.org/downloads/)

---

## 🚀 Οδηγίες Εγκατάστασης & Εκτέλεσης

### Βήμα 1: Εκκίνηση της MongoDB με Docker
Η βάση δεδομένων τρέχει μέσα σε ένα Docker container. Ανοίξτε το τερματικό σας στον φάκελο του project και εκτελέστε:

```bash
docker-compose up -d
```

Αυτό θα κατεβάσει το image της MongoDB και θα σηκώσει τη βάση με τα εξής στοιχεία:
* **Host/Πόρτα:** `localhost:27017`
* **Username:** `admin`
* **Password:** `secret`

### Βήμα 2: Σύνδεση στη Βάση
Μπορείτε να συνδεθείτε στη βάση με δύο τρόπους:

**Τρόπος Α: Μέσω Τερματικού (mongosh)**
Για να τρέξετε queries απευθείας μέσα στο container, εκτελέστε:
```bash
docker exec -it my-mongodb mongosh -u admin -p secret
```

**Τρόπος Β: Μέσω Γραφικού Περιβάλλοντος (MongoDB Compass)**
1. Ανοίξτε το **MongoDB Compass**.
2. Δημιουργήστε νέα σύνδεση με το παρακάτω Connection String:
   ```text
   mongodb://admin:secret@localhost:27017/
   ```

### Βήμα 3: Εισαγωγή Δεδομένων
Μέσα από το mongosh ή το Compass:
1. Δημιουργήστε μια νέα βάση δεδομένων με όνομα `university_library`.
2. Δημιουργήστε δύο collections: `books` και `members`.
3. Εισάγετε τα JSON δεδομένα του μαθήματος μέσα στα αντίστοιχα collections (στο Compass χρησιμοποιήστε την επιλογή **Insert Document**).

### Βήμα 4: Προετοιμασία Περιβάλλοντος Python (Virtual Environment)
Για να απομονώσουμε τις βιβλιοθήκες, δημιουργούμε ένα εικονικό περιβάλλον.

**Σε Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Σε Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

Στη συνέχεια, εγκαθιστούμε τις απαραίτητες βιβλιοθήκες:
```bash
pip install -r requirements.txt
```

### Βήμα 5: Εκτέλεση του Κώδικα
Αφού έχετε ενεργοποιήσει το εικονικό περιβάλλον και έχετε εισάγει τα δεδομένα στη βάση, μπορείτε να τρέξετε το Python script:

```bash
python library_query.py
```
Το script θα ελέγξει δυναμικά αν υπάρχουν η βάση και το collection, και θα τυπώσει όλα τα βιβλία που έχουν 5 ή περισσότερα διαθέσιμα αντίτυπα.

---

## 🧹 Καθαρισμός (Cleanup)
Όταν τελειώσετε την ενασχόλησή σας με το project:
1. Απενεργοποιήστε το περιβάλλον Python τρέχοντας: 
   ```bash
   deactivate
   ```
2. Σταματήστε και διαγράψτε το container της βάσης τρέχοντας:
   ```bash
   docker-compose down -v
   ```