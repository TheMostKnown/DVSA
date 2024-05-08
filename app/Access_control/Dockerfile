FROM ubuntu:latest

RUN apt-get update && apt-get install -y apache2 php libapache2-mod-php php-mysql

RUN echo "127.0.0.1       fileuploadersteam.sne" >> /etc/hosts

COPY ./file /var/www/html

RUN chown -R www-data:www-data /var/www/html

RUN a2enmod rewrite

EXPOSE  80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]