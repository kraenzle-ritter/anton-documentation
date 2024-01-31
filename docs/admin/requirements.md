# Server Requirements

Anton v.0.27.0 is a [Laravel](https://laravel.com/) Version 9 Application.

- [Ubuntu](https://ubuntu.com/)[^OS] 20.04 oder 22.04 LTS
- [PHP](https://www.php.net/) >=8.2
- [MySQL](https://www.mysql.com/de/) >=8.0.35 (or Maria DB >= 10.2.7)
- [Apache](https://httpd.apache.org/) 2.4 (mod_rewrite, .htaccess)
- PHP-Extensions
    - OpenSSL PHP Extension
    - PDO PHP Extension
    - Mbstring PHP Extension
    - Tokenizer PHP Extension
    - XML PHP Extension
    - Ctype PHP Extension
    - Tokenizer PHP Extension
    - JSON PHP Extension
    - BCMath PHP Extension
    - ext-imagick PHP Extension
    - ext-sodium
- [composer](https://getcomposer.org)
- [ssh](https://www.openssh.com/) access
- [git](https://git-scm.com/)
- email (e.g. sendmail)
- [ffmpeg](https://www.ffmpeg.org/), [gs](https://www.ghostscript.com/), [poppler-utils](https://poppler.freedesktop.org/), [imagemagick](https://imagemagick.org/)
- [supervisor](http://supervisord.org/)

[^OS]: Other Operating Systems of the Linux or Unix-Family should also do the trick.
<!--
[^mysql]: MariaDB is not tested and is not recommended at the moment, because of its [JSON Implementation](https://elephantdolphin.blogspot.com/2018/11/a-tale-of-two-json-implementations.html).
-->
