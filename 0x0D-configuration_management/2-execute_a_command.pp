# create a manifest that kills a process named killmenow
exex { 'killmenow':
     command => 'pkill -f killmenow'
}
