#!/usr/bin/perl

open INPUTFILE, "< doc.kml" or die "ha ha only serious\n";

$x = 0;

while (<INPUTFILE>) {
    if (/styleUrl/) {
        print "      <styleUrl>#LineStyle$x</styleUrl>\n";
        $x++;
        if ($x == 6) { $x = 0; }
    } else {
        print;
    }
}
