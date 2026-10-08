# Ziua 4: Playwright, locatori și verificări

## Ce e Playwright
Instrument care deschide un browser real și face din cod ce ar face un
utilizator (scrie, apasă), apoi verifică dacă rezultatul e cel așteptat.

## Ordinea locatorilor (de la cel mai bun)
1. Rol + nume (`get_by_role`): ca un om care vede "butonul Login"
2. Etichetă / placeholder (`get_by_label`, `get_by_placeholder`): câmpul după textul din el
3. Text (`get_by_text`): elementul după textul vizibil
4. CSS (`locator("#id")`): ultima variantă, se strică ușor când se schimbă codul

## Acțiune vs verificare
- Acțiune (`click`, `fill`): face ceva pe pagină
- Verificare (`expect`): confirmă că rezultatul e cel așteptat; fără ea, testul trece chiar dacă aplicația e stricată

## Test care poate pica
Am schimbat parola în "parola_gresita". Testul a picat: URL-ul real era
saucedemo.com, nu inventory, iar pagina arăta mesajul de eroare. Am pus
parola corectă la loc și a trecut. Așa știu că verificarea e reală.

## Teste scrise azi
- test_login_with_locators: se loghează și verifică că ajunge pe inventory
- test_inventory_title: după login verifică textul "Products" și cele 6 produse