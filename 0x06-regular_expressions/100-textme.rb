#!/usr/bin/env ruby
$f1 = ARGV[0].scan(/from:(.\w*?)\]/).join
$f2 = ARGV[0].scan(/to:(.\w*?)\]/).join
$f3 = ARGV[0].scan(/flags:(.*?)\]/).join
puts $f1 + "," + $f2 + "," + $f3
