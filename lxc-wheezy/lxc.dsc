Format: 3.0 (quilt)
Source: lxc
Binary: lxc, lxc-stuff, lxc-dbg, lxc-dev
Architecture: linux-any all
Version: 1.0.3~opt-1
Maintainer: Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
Uploaders: Jonas Genannt <jonas.genannt@capi2name.de>
Homepage: http://linuxcontainers.org/
Standards-Version: 3.9.5
Build-Depends: debhelper (>= 9), dh-autoreconf, doxygen, autotools-dev, docbook2x, graphviz, libapparmor-dev, liblua5.2-dev, libcap-dev, libselinux-dev, linux-libc-dev, pkg-config, python3-dev
Package-List: 
 lxc deb admin optional arch=linux-any
 lxc-dbg deb debug extra arch=linux-any
 lxc-dev deb libdevel optional arch=linux-any
 lxc-stuff deb admin optional arch=all
Files: 
 93f3d010ea0aae27d5317fe9de167b8a 492288 lxc_1.0.3.orig.tar.xz
