# Install a specific version of Flask (2.1.0)
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  command  => '/usr/bin/pip3', # Specify the path to pip3 executable
}

