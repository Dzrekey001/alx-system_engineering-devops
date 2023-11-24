#Using Puppet, create a manifest that kills a process named killmenow
exec {'kill':
  command => 'pkill -f killmenow',
  path    => '/bin:/usr/bin',
  user    => 'root',
  onlyif  => 'pgrep -f killmenow',
}
