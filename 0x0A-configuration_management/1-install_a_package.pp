# Install flask and required packages

# Install python 3.8.10
package { 'python3.8':
  ensure => '3.8.10',
}

# Install pip
package { 'python3-pip':
  ensure => present,
}

# Install an especific version of flask (2.1.0) 
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

# Install Werkzeug 2.1.1
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}
