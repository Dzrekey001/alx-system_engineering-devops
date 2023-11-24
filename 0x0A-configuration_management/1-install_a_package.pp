# Using Puppet to install flask from pip`3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
