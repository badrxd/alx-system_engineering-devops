# edit max open files number
exec { 'change_number':
  command  => 'sed -i "s|ULIMIT=\"-n 15\"|ULIMIT=\"-n 4000\"|" /etc/default/nginx',
  provider => 'shell',
}
-> exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => 'shell',
}
