%global __python %{__python3}

Name:           lxc-scripts
Version:        0.3.0
Release:        %{release}%{?dist}
Summary:        Scripts for creating LXC containers

License:        LGPLv2+
URL:            http://www.lightbuildserver.org
Source0:        https://github.com/tpokorra/%{name}/archive/master.tar.gz

BuildArch:      noarch
Requires:       lxc lxc-templates lxc-extra gpg libvirt tar rsync net-tools debootstrap crontabs

%description
This package provides some scripts useful for creating LXC containers.
They manage the network, and the tunneling and websites routed through nginx.

%prep
%setup -q -n %{name}-master

%build
# Nothing to build

%install
install -dm 755 %{buildroot}%{_datadir}/%{name}

cp -a * %{buildroot}%{_datadir}/%{name}

%files
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.sh
%{_datadir}/%{name}/*.tpl
%{_datadir}/%{name}/Readme.md

%changelog
* Fri Mar 08 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.3.0-0
- drop patches for Fedora containers
* Fri Nov 10 2017 Timotheus Pokorra <tp@tbits.net> - 0.2.0-1
- Requires now lxc-extra for listcontainers.sh
* Fri Jul 10 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.1.0-4
- Some fixes for Fedora 22 and CentOS7 host
* Mon Jun 22 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.1.0-1
- Initial package
