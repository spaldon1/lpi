Témy na ročníkové projekty z Logiky pre informatikov
====================================================


Editor dôkazov v Hilbertovskom kalkule
--------------------------------------

Hilbertovský dôkaz je postupnosť formúl spĺňajúca nejaké podmienky.
Naprogramujte editor, ktorý umožní vytvárať dôkaz a bude kontrolovať
jeho správnosť. Mal by mať dve úrovne kontroly. Na jednej musí používateľ
uviesť, z ktorých axióm alebo predchádzajúcich formúl nová formula vznikla.
Na druhej úrovni používateľ iba edituje formuly a editor sám zistí, či a na
základe čoho mohla formula vzniknúť.

Preferovaná je webová implementácia v HTML+JavaScript. Editor by mal
podporovať možnosť exportovať vytvorený dôkaz v nejakom jednoduchom formáte
a tak isto možnosť importovať a overiť korektnosť dôkazu v tomto formáte.

Editor pre tablá
----------------

Naprogramujte webový (HTML+JavaScript) editor pre výrokovologické tablá.
Editor umožní používateľovi vytvoriť tablo pričom kontroluje jeho správnosť.
Poskytované by mali byť dve možnosti kontroly: v prvej používateľ určí ako
a z čoho formula vznikla, v druhej editor sám zistí či a z čoho formula
mohla vzniknúť.

Editor by mal podporovať možnosť exportovať vytvorené tablo v nejakom
jednoduchom formáte a tak isto možnosť importovať a overiť korektnosť
tabla v tomto formáte.

Prekladač tablových dôkazov do Hilbertovských
---------------------------------------------

V rámci tried pre tablové dôkazy, ktoré naprogramujete na tomto predmete,
doprogramujte metódy, ktoré z uzavretého tabla vygenerujú Hilbertovský
dôkaz.

Dosadzovač (grounder)
---------------------

Vytvorte program, ktorý bude slúžiť ako „frontend“ pre SAT solver a umožní
písať formuly kvantifikované všeobecným kvantifikátorom (za splnenia určitých
podmienok).  Program ich preloží do výrokovej logiky („dosadí“ premenné), pustí
SAT solver, načíta výsledok a „dekóduje“ ho.

Napríklad pre vstup (formát vstupu nie je finálny)

    ∀r=1..8, ∀s1=1..8, ∀s2=1..8, s1!=s2: q(r,s1) → q(r,s2)

vytvorí vstup pre SAT solver zodpovedajúci 448 výrokovým formulám

    q_1_1 → q_1_2
    q_1_1 → q_1_3
    ...
    q_8_8 → q_8_7

Program by tiež mal vediet pracovať s množinami konštánt, t.j. vedieť spracovať
vstup typu:
    Ludia = { Muller, Eisman, Stirlitz }
    ∀x∈Ludia : rus(x) → spion(x)

SAT solver
----------

Naprogramujte lepší SAT solver, ako naprogramujeme na cvičeniach v druhej
polovici semestra.

Logika s rovnosťou
------------------

Naprogramujte algoritmus _kongruenčného uzáveru_,
ktorý rozhoduje vyplývanie v logike s rovnosťou.
Vstupom tohto algoritmu je množina rovnostných literálov, napr.:

    x = y, f(x) = z, f(y) = x, z != x

Výstupom je odpoveď, či je súčasne splniteľná (množina z príkladu nie je).

Integrujte algoritmus so SAT solverom, ktorý naprogramujeme na cvičeniach
v druhej polovici semestra.


