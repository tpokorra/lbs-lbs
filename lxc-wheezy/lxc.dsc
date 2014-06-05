-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA1

Format: 3.0 (quilt)
Source: lxc
Binary: lxc, lxc-stuff, lxc-dbg, lxc-dev
Architecture: linux-any all
Version: 1.0.3-2
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
 d8412cfe750cfcf4f5b57351bf4d6db1506fe23b 492288 lxc_1.0.3.orig.tar.xz
 4800db30dc5c84806412ee93e0ed986e590e9804 48396 lxc_1.0.3-2.debian.tar.xz
Checksums-Sha256: 
 0831f636bd1acc3bd9ee680563b19fbdd9a504f63a48d810659f12b98114a807 492288 lxc_1.0.3.orig.tar.xz
 e84467f0173c4f5d6b84daa53ee96d185ebd3988e814280119dc7776135f1531 48396 lxc_1.0.3-2.debian.tar.xz
Files: 
 93f3d010ea0aae27d5317fe9de167b8a 492288 lxc_1.0.3.orig.tar.xz
 5b62701d0f82a92e98458ff0988dbcd6 48396 lxc_1.0.3-2.debian.tar.xz

-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1

iEYEARECAAYFAlOLbicACgkQ+C5cwEsrK547bACg0IdNTpzd1/3VpNE5NBM6KacA
fOYAoJ5i4pvW/q/pmRh0zl9JciaDS4wp
=HgS/
-----END PGP SIGNATURE-----
