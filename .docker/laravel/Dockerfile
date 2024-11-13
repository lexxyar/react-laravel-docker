FROM php:8.2-fpm-alpine

RUN apk update

WORKDIR /var/www

###########################################
# Uncomment to use MySQL
###########################################
# Install the PHP pdo_mysql extention
# Install the PHP pdo extention
RUN docker-php-ext-install pdo pdo_mysql
###########################################

###########################################
# Uncomment to use ZIP
###########################################
RUN apk add libzip-dev
RUN docker-php-ext-install zip
###########################################

###########################################
# Uncomment to use Imagemagic (GD lib)
###########################################
#RUN apk add ghostscript
#RUN apk add php82-pecl-imagick --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community
#RUN apk --update add imagemagick imagemagick-dev
#RUN pecl install imagick
#RUN docker-php-ext-enable imagick
###########################################
RUN apk add --no-cache imagemagick-dev; \
# WARNING: imagick is likely not supported on Alpine: https://github.com/Imagick/imagick/issues/328
# https://pecl.php.net/package/imagick
# https://github.com/Imagick/imagick/commit/5ae2ecf20a1157073bad0170106ad0cf74e01cb6 (causes a lot of build failures, but strangely only intermittent ones 🤔)
# see also https://github.com/Imagick/imagick/pull/641
# this is "pecl install imagick-3.7.0", but by hand so we can apply a small hack / part of the above commit
	curl -fL -o imagick.tgz 'https://pecl.php.net/get/imagick-3.7.0.tgz'; \
	echo '5a364354109029d224bcbb2e82e15b248be9b641227f45e63425c06531792d3e *imagick.tgz' | sha256sum -c -; \
	tar --extract --directory /tmp --file imagick.tgz imagick-3.7.0; \
	grep '^//#endif$' /tmp/imagick-3.7.0/Imagick.stub.php; \
	test "$(grep -c '^//#endif$' /tmp/imagick-3.7.0/Imagick.stub.php)" = '1'; \
	sed -i -e 's!^//#endif$!#endif!' /tmp/imagick-3.7.0/Imagick.stub.php; \
	grep '^//#endif$' /tmp/imagick-3.7.0/Imagick.stub.php && exit 1 || :; \
	docker-php-ext-install /tmp/imagick-3.7.0; \
	rm -rf imagick.tgz /tmp/imagick-3.7.0

RUN docker-php-ext-enable imagick
###########################################

ADD ./.docker/laravel/custom-php.ini /usr/local/etc/php/conf.d/custom-php.ini

EXPOSE 9000