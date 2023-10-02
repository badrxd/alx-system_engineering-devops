#change configure nginx

exec { 'update_all':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

-> exec { 'install_nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
}

-> exec { 'add_content':
    command  => 'sudo sed -i "/listen 80 default_server;/ a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default',
    provider => shell,
}

-> exec { 'restart_server':
    command  => 'sudo service nginx restart',
    provider => shell,
}
