# Cazuri de test: login (saucedemo.com)

## TC-02: Login cu câmpul de parolă gol
- Precondiții: Utilizatorul standard_user există
- Pași:
  1. Deschid pagina de login.
  2. Scriu standard_user în câmpul de utilizator.
  3. Las câmpul de parolă necompletat.
  4. Apăs Login.
- Rezultat așteptat: mesaj de eroare pentru parolă lipsă, utilizatorul rămâne pe pagina de login.
- Rezultat obținut: Epic sadface: Password is required
- Status: Pass

## TC-03: Login cu câmpul de username gol
- Precondiții: Parola secret_sauce este validă pentru conturile de test
- Pași:
  1. Deschid pagina de login.
  2. Scriu secret_sauce în câmpul de parolă.
  3. Las câmpul de username necompletat.
  4. Apăs Login.
- Rezultat așteptat: mesaj de eroare pentru username lipsă, utilizatorul rămâne pe pagina de login.
- Rezultat obținut: Epic sadface: Username is required
- Status: Pass
