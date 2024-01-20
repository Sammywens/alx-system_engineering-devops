# set up your client SSH configuration file so
# that you can connect to a server without typing a password.

include stdlib

file_line {'PasswordAuthentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
}

file_line {'IdentityFile':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile /root/.ssh/school',
  match  => '^IdentityFile',
}
