# make changes in SSH configuration file

file_line { 'Declare the identity file':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  }

file_line { 'Turn off the passwd':
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  }
