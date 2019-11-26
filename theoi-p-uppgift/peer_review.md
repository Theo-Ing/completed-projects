# Peer review av Otto Lindstam
## Uppgift 101 - Belysning av klot

## Struktur:
Koden är indelad i tre klasser och en main() metod som kallar på klasserna. Koden är uppdelad på ett strukturerat sätt där alla globala konstanter (utom en som är ett objekt baserat på en klass) ligger i början. Sedan kommer klasserna, därefter main() metoden och sist kommer ett globalt anrop till main(). Detta når i min mening kraven.

## Lagom stora:
Klasser och metoder är lagom stora och allt ligger inte i någon "jätteklass". Det finns inte heller några små metoder/funktioner som är one-liners. Detta når i min mening kraven.

## Dokumenterad:
Alla klasser, metoder och funktioner är väl dokumenterade både med kommentarer i början som förklarar programmet i sin helhet men också med små kommentarer i koden för att förklara vad stycken av kod i metoderna gör. Det finns inte ett överflöd av små kommentarer dock utan endast så koden är lätt att följa. Detta når i min mening kraven.

## Undvik globala variabler:
Inga globala variabler används. 8 stycken globala konstanter har använts. Detta når i min mening kraven.

## Undvik onödig kodupprepning:
Ingen onödig kodupprepning hittad. if-satser som är hittade verkar vara det optimala alternativet för det som behöver göras. Ser inte heller några onödiga for-loopar. Detta når i min mening kraven.

## Undvik hårdkodning:
Ingen hårdkodning upptäckt, kanske inte är relevant för denna uppgift, det som skulle kunna behöva ändras kan ändras med hjälp av en ändring av globala konstanter. Detta når i min mening kraven.

## Utskrifterna:
Användargränssnittet är lätt att förstå. Muspekaren är tydlig och det finns klar text på hur man stänger programmet eller ändrar radien av sfären. Detta når i min mening kraven.

## Namn på variabler:
Namn på funktioner, klasser och metoder är lättbegripliga. Variabelnamn är lätta att förstå med möjligt undantag för variabelnamnet p0 i Sphere() klassen (döptes om till lightDir efter feedback). x, y, z variabelnamn används men de används för koordinater så det är förväntat och optimalt. Detta når i min mening kraven.
