# Schiffe_Versenken 
## Prüfungsaufgabe Programmentwurf GL-Informatik 1 (TEA23) der Studenten: Tom Gluth, Edgar Malinowsky und Johannes Rudolph

### Link zum GitHub Repository:
https://github.com/UnknownEdgar/Schiffe_Versenken

### Allgemeines
Das Programm stellt das Spiel "Schiffe versenken" dar und ermöglicht es zwei lokalen Spielern dieses per Konsolenein- und ausgabe zu spielen.
Die erforderlichen Aktionen und eventuelle Fehleingaben bzw. Regelverstöße der Spieler werden dabei durch die Konsole ausgegeben und die Spieler werden durch das Spiel geleitet.
Sobald ein Spieler das Spiel gewonnen hat, werden beide Spieler (Spieler 1 und Spieler 2) gefragt, ob sie eine weitere Runde spielen wollen.

### Symbole des Spiels

           X = Treffer                                      in roter Farbe
           O = daneben / Barriere der Schiffplatzierung     in blauer / grauer Farbe
           # = Schiff                                       in grüner Farbe

### Spielereingaben / Spielablauf

Das Spiel wird durch Ausführen des Programmes schiffe_versenken.py gestartet. (Möglicherweise müssen davor noch die Programme aufbau.py, ausgabe.py und converter.py initialisiert werden, damit alle Module ordentlich funktionieren)

Wird das Spiel gestartet, so werden die Spieler der Reihenfolge nach (1, dann 2) gefragt wo sie ihre Schiffe platzieren möchten.
Die Regeln bei der Eingabe der Schiffe sind wie folgt:
        
    - Zur Verfügung stehen 1 Schlachtschiff (5 Felder), 2 Kreuzer (4 Felder), 3 Zerstörer (3 Felder), 4 U-Boote (2 Felder)
    - Die Schiffe werden nacheinander in der oben angegebenen Reihenfolge platziert. Das aktuell zu platzierende Schiff wird zusätzlich in der Konsole ausgegeben.
    - Bei der Platzierung eines Schiffs muss das obere/linke Feld des Schiffs und dessen Orientierung vertikal/horizontal angegeben werden.
    - Das entsprechende Feld wird über die Eingabe der Spalte (A-J) und anschließender Eingabe der Zeile (1-10) angegeben.
    - Die Schiffe dürfen ausschließlich vertikal mit Eingabe der Zahl 1 bei entsprechender Fragestellung, oder horizontal mit Eingabe der Zahl 0 auf dem Spielfeld platziert werden.
    - Schiffe dürfen nicht überlappend platziert werden und müssen mindestens ein Feld Abstand zum nächsten Schiff aufweisen. Entsprechende Barrieren werden bei der Platzierung ausgegeben.
    - Teile des Schiffs können das Spielfeld nicht verlassen, sodass bei der Eingabe genug Platz für das Schiff berücksichtigt werden muss.
    - Wurden ein oder mehrere Schiffe platziert und möchten noch abgeändert werden, so kann das gesamte eigene Spielfeld nach Eingabe der Orientierung des Schiffs mit der Eingabe der Zahl 8 zurückgesetzt
    werden. Dies geht allerdings nur vor der Platzierung des letzten verfügbaren Schiffs eines Spielers.
    
Wurden alle Schiffe durch die Spieler platziert, so beginnt das Spiel.
Zuerst wird Spieler 1 aufgefordert auf das Feld des Gegners zu schießen. Der Schuss wird ebenfalls über die Eingabe der Spalte (A-J) und anschließender Eingabe der Zeile (1-10) realisiert.
Hat der aktive Spieler getroffen, so darf er erneut schießen. Ging sein Schuss daneben, so ist der andere Spieler an der Reihe.
In beiden Fällen werden die Schüsse im Schussfeld des aktiven Spielers angezeigt und ebenfalls im Feld des Gegners eingetragen.

Jeder der Spieler erhält nach seinem Schuss die Möglichkeit sein eigenes Feld per Eingabe von 0 - nein oder 1 - ja nochmal anzusehen.
Der aktive Spieler wird jeweils vor der Abfrage des Schusses in der Konsole angegeben.

Bei jedem Spielerwechsel wird durch das Drücken einer beliebigen Taste abgefragt, dass der aktive Spieler sein Schussfeld bzw. sein eigenes Feld gesehen hat und bereit ist das Spiel an den Gegner zu übergeben.
Die Schusssequenz endet, sobald einer der Spieler alle Schiffe seines Gegners versenkt hat.

Sobald ein Spieler das Spiel für sich entschieden hat, wird dies durch die Konsole ausgegeben.
Darauf folgt die Möglichkeit per Konsoleneingabe 0 - nein oder 1 - ja eine weitere Runde zu spielen oder das Programm zu beenden. 





