.\" knocker man page
.\" Process this file with: groff -man -Tascii
.\" man page originally written by  Gabriele Giorgetti <g.gabriele79@genie.it>
.TH KNOCKER 1 "MAY 24, 2002"
.SH NAZWA
knocker \- �atwy w u�yciu skaner port�w
.SH SK�ADNIA
.B \fBknocker\fR --host <komputer>
[\fIOPCJE\fR]
.SH OPIS
.B knocker 
jest prostym i �atwym w u�yciu skanerem port�w TCP napisanym w C, zdolnym analizowa� komputery i wszystkie inne dzia�aj�ce na nich us�ugi.
.SH OPCJE
.TP
\fB\-H\fr, \fB\-\-host\fR
nazwa lub adres IP komputera do skanowania
.TP
\fB\-P\fr, \fB\-\-port\fR
numer portu do skanowania (tylko pojedyncze porty)
.TP
\fB\-SP\fr, \fB\-\-start-port\fR
numer portu od kt�rego ma si� zacz�� skanowanie 
.TP
\fB\-EP\fr, \fB\-\-end-port\fR
numer portu na kt�rym ma si� zako�czy� skanowanie
.TP
\fB\-\-last-host\fR
u�ywanie ostatnio skanowanego komputera jako celu
.TP
\fB\-\-last-scan\fR
ponowne wykonywanie ostatniego skanowania port�w
.TP
\fB\-q\fr, \fB\-\-quiet\fR
wy��czenie wy�wietlania wynik�w w terminalu i nie zapisywanie pliku logu
.TP
\fB\-lf\fr, \fB\-\-logfile <plik logu>\fR
zapisywanie wyniku do pliku logu
.TP
\fB\-nf\fr, \fB\-\-no-fency\fR
wy��czenie ozdobnego wyj�cia
.TP
\fB\-nc\fr, \fB\-\-no-colors\fR
wy��czenie kolorowe wyj�cie
.TP
\fB\-\-configure\fR
dopuszczanie konfiguracji u�ytkownika
.TP
\fB\-h\fR, \fB\-\-help\fR
wy�wietlanie pomocy
.TP
\fB\-v\fR, \fB\-\-version\fR
wy�wietlanie informacji o wersji
.SH PRZYK�ADY
.LP
Standardowe uruchomienie programu:
.LP
knocker --host 192.168.0.1
.LP
Okre�lanie zakresu port�w do skanowania:
.LP
knocker --host komputer --start-port 1 --end-port 2600
.LP
lub
.LP
knocker -H komputer -SP 1 -EP 2600
.LP
Skanowanie pojedynczego portu:
.LP
knocker -H komputer --port 21
.LP
Uruchomienie bez u�ywania kolorowego terminala (je�eli tw�j terminal nie wspiera kolor�w):
.LP
knocker --host 192.168.0.1 --no-colors
.LP
Uruchomienie programu w tle i zapisanie wynik�w do pliku logu:
.LP
knocker --host 192.168.0.1 --quiet &
.LP
.LP
.SH DOST�PNO��   
Wcze�niejsze wersje tego programu mo�na znale�� na
http://knocker.sourceforge.net
.SH B��DY
Zobacz plik BUGS w celu zapoznania si� z list� znanych b��d�w.
Je�eli znajdziesz nowe skontaktuj si� z <g.gabriele79@genie.it>
.SH AUTOR
knocker zosta� napisany przez Gabriele Giorgetti <g.gabriele79@genie.it>
.SH COPYRIGHT
Copyright \(co 2001,2002 Gabriele Giorgetti
.br
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
