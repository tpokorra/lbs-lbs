%global __python %{__python3}

Name:           docker-scripts
Version:        0.1.0
Release:        %{release}%{?dist}
Summary:        Scripts for creating Docker containers

License:        LGPLv2+
URL:            http://www.lightbuildserver.org
Source0:        https://github.com/tpokorra/%{name}/archive/master.tar.gz

BuildArch:      noarch
Requires:       docker-io
Requires:       rsync
Requires:       tar

%description
This package provides some scripts useful for creating Docker containers.

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
%{_datadir}/%{name}/Dockerfiles/Dockerfile.*
%{_datadir}/%{name}/Readme.md

%changelog
* Mon Jun 22 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.1.0-1
- Initial package
