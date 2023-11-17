# change max open files for holberton user
exec { 'change_hard_limit':
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 65536/" /etc/security/limits.conf',
  provider => 'shell'
}
exec { 'change_soft_limit':
  command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 65536/" /etc/security/limits.conf',
  provider => 'shell'
}
