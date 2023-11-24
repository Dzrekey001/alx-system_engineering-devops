#Using Puppet, create a manifest that kills a process named killmenow
exec {'kill':
commad   => 'pkill -f killmenow',
provider => shell,
}
