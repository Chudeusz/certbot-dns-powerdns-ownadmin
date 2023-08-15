certbot-dns-ownadmin
============

OwnAdmin Authenticator plugin for [Certbot](https://certbot.eff.org/).

This plugin is built from the ground up and follows the development style and life-cycle
of other `certbot-dns-*` plugins found in the
[Official Certbot Repository](https://github.com/certbot/certbot).

Installation
------------

```
pip install --upgrade certbot
pip install certbot-dns-ownadmin
```

Verify:

```
$ certbot plugins --text

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
* dns-ownadmin
Description: Obtain certificates using a DNS TXT record (if you are using
OwnAdmin for DNS.)
Interfaces: Authenticator, Plugin
Entry point: dns-ownadmin = certbot_dns_ownadmin.dns_ownadmin:Authenticator

...
```

Configuration
-------------

The credentials file e.g. `~/ownadmin-credentials.ini` should look like this:

```
dns_ownadmin_api_url = https://api.mypowerdns.example.org
dns_ownadmin_api_key = AbCbASsd!@34
```

Usage
-----
```
certbot ... \
        --authenticator dns-ownadmin  \
        --dns-ownadmin-credentials ~/ownadmin-credentials.ini \
        certonly
```
