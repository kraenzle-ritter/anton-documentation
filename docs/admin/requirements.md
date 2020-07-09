# Server Requirements

Anton is a [Laravel](https://laravel.com/) Version 6 Application.

- [Ubuntu](https://ubuntu.com/)[^OS] 16.04, 18.04 oder 20.04 LTS
- [PHP](https://www.php.net/) >= 7.3
- [MySQL](https://www.mysql.com/de/)[^mysql]>=5.7.8
- [Apache](https://httpd.apache.org/) 2.4 (mod_rewrite, .htaccess)
- PHP-Extensions
    - OpenSSL PHP Extension
    - PDO PHP Extension
    - Mbstring PHP Extension
    - Tokenizer PHP Extension
    - XML PHP PExtension
    - Ctype PHP Extension
    - Tokenizer PHP Extension
    - JSON PHP Extension
    - BCMath PHP Extension
    - ext-imagick PHP Extension
- [composer](https://getcomposer.org)
- [ssh](https://www.openssh.com/) Zugang
- [git](https://git-scm.com/)
- email (z.B. sendmail)
- [ffmpeg](https://www.ffmpeg.org/), [gs](https://www.ghostscript.com/), [poppler-utils](https://poppler.freedesktop.org/), [imagemagick](https://imagemagick.org/)
- [supervisor](http://supervisord.org/)

[^OS]: Other Operating Systems of the Linux or Unix-Family should also do the trick.
[^mysql]: MariaDB is not tested and is not recommended at the moment, because its [JSON Implementation](https://elephantdolphin.blogspot.com/2018/11/a-tale-of-two-json-implementations.html).
<!-- The '->>' Operator is actually used in Model AntonEvent.php -->
