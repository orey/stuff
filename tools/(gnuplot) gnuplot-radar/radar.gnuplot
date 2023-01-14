set angles degrees
  set polar
  set grid polar 120.
  unset border
  unset param

  set style data filledcurves 
  set style fill solid 0.5

  set datafile separator ","

  set xtics axis nomirror
  set ytics axis nomirror
  set yrange [-45:45]
  set xrange [-45:45]
  set size square
  set title "Radar chart"

  plot 'data.csv' using 1:2 notitle, '' using 1:3 notitle, '' using 1:4 notitle
  