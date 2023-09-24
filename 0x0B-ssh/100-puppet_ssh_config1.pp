# make changes in SSH configuration file


file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/badr',
  line   => '    PasswordAuthentication no',
  }
