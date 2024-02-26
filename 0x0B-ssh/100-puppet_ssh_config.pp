#!/usr/bin/env bash
# A Script To Use Puppet

file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'Turn off passwd auth':
  path	=> '/etc/ssh/ssh_config',
  line	=> 'PaswordAuthentication no',
  match	=> '^#PaswordAuthentication',
}

file_line { 'Declare identity file':
  path	=> '/etc/ssh/ssh_config',
  line	=> 'IdentityFile ~/.ssh/school',
  match	=> '^#IdentityFile',
}
