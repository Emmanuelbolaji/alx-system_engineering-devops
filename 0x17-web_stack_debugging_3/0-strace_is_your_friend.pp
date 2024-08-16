# Fixes a WordPress file with wrong filename
exec { 'fix-wordpress':
    command => 'sed -i s/phpp/php/g /var/ww/html/wp-settings.php',
    path    => '/usr/bin/:bin',
}
