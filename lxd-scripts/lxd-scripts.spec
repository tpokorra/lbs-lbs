%global __python %{__python3}

Name:           lxd-scripts
Version:        0.4.0
Release:        %{release}%{?dist}
Summary:        Scripts for creating LXD containers

License:        LGPLv2+
URL:            http://www.lightbuildserver.org
Source0:        https://github.com/tpokorra/%{name}/archive/master.tar.gz

BuildArch:      noarch
Requires:       lxd lxd-client lxc-utils gpg libvirt tar rsync net-tools debootstrap crontabs

%description
This package provides some scripts useful for creating LXD containers.
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
* Fri Mar 06 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.4.0-0
- initial build of lxd-scripts
