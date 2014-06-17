-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA1

Format: 3.0 (quilt)
Source: lxc
Binary: lxc, lxc-stuff, lxc-dbg, lxc-dev
Architecture: linux-any all
Version: 1.0.4-3
Maintainer: Daniel Baumann <mail@daniel-baumann.ch>
Uploaders: Jonas Genannt <jonas.genannt@capi2name.de>
Homepage: http://linuxcontainers.org/
Standards-Version: 3.9.5
Vcs-Browser: http://daniel-baumann.ch/gitweb/?p=debian/packages/lxc.git
Vcs-Git: git://daniel-baumann.ch/git/debian/packages/lxc.git
Build-Depends: debhelper (>= 9), dh-autoreconf, doxygen, autotools-dev, docbook2x, graphviz, libapparmor-dev, liblua5.2-dev, libcap-dev, libseccomp-dev [amd64 armhf i386], libselinux-dev, linux-libc-dev, pkg-config, python3-dev
Package-List:
 lxc deb admin optional arch=linux-any
 lxc-dbg deb debug extra arch=linux-any
 lxc-dev deb libdevel optional arch=linux-any
 lxc-stuff deb admin optional arch=all
Checksums-Sha1:
 d6e51c75eaaea552b8f63b82854a99e1da331984 390216 lxc_1.0.4.orig.tar.xz
 fc938c80914226cab8f499d681814609452cd0a1 49468 lxc_1.0.4-3.debian.tar.xz
Checksums-Sha256:
 79d337a86125f283c5af8aa137fbcd6804c099ccf41fe7cda15c8df49e5561c7 390216 lxc_1.0.4.orig.tar.xz
 9518cd57478d7ff7ae1cdc7c87be7642f58b365cea9d2e0e6a994ed8efd68f26 49468 lxc_1.0.4-3.debian.tar.xz
Files:
 60112406c83adc5e007455aeca629a19 390216 lxc_1.0.4.orig.tar.xz
 a2c590b45d3199fbb80f4782c77c79e9 49468 lxc_1.0.4-3.debian.tar.xz

-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1

iEYEARECAAYFAlOcJwUACgkQ+C5cwEsrK56eZQCfRPOsDd5P0gtspmSMBTQd5+D7
n4wAn1b5ux7JAmLidt9x3GDBLSSaYX6U
=+RfJ
-----END PGP SIGNATURE-----
