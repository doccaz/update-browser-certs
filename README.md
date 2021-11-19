# update-browser-certs

A script that automagically merges system CA certificates into a database compatible with Mozilla Firefox, Google Chrome and Chromium using the default systemd path monitoring mechanism.


## How does it work?

Basically, systemd on most distros already ships with a service that *monitors* /etc/pki/trust/anchors for new files. Once a new certificate is added, it automatically hashes the certificates (among other actions). We build upon this, and do the same to add the new certificates to a shared NSS database located at /etc/pki/nssdb.

Then, another systemd path monitor will check if a flag file is touched, indicating that there are recently added certificates to the database. If that's the case, systemd will start another service (as a **user instance**) to merge our global DB to the current active user's browser profiles.

## Why do we need this?

This script makes the whole process of accepting and importing new CA certificates as easy as just **placing the .pem file in /etc/pki/trust/anchors**, and **nothing else.**

