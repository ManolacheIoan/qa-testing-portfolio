ID: BUG-02
Titlu: Câmpul Last Name nu acceptă text în pasul de checkout pentru problem_user
Mediu: Safari 17, macOS Sonoma
Date de test: problem_user / secret_sauce
Precondiții: utilizator logat, cu cel puțin un produs în coș
Pași:
1. Mă loghez cu problem_user / secret_sauce.
2. Adaug un produs în coș.
3. Deschid coșul și apăs Checkout.
4. Scriu Ion în First Name.
5. Încerc să scriu Popescu în Last Name.
6. Scriu 805300 în Zip/Postal Code.
7. Apăs Continue.
Rezultat așteptat: Last Name acceptă text și comanda poate continua.
Rezultat obținut: Last Name nu acceptă text, iar la Continue apare "Error: Last Name is required". Utilizatorul nu poate trece de checkout.
Severitate: mare
Prioritate: urgentă
Dovadă: de adăugat
Status: Nou
