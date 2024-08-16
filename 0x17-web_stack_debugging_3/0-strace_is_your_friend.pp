# Fixes a WordPress file with wrong filename
file { '/var/www/html':
ensure => 'directory',
}

file { '/var/www/html/wp-settings.php':
  ensure  => 'present',
  content => '<?php /* Placeholder content */ ?>',
  require => File['/var/www/html'],
}

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
  require => File['/var/www/html/wp-settings.php'],
}
