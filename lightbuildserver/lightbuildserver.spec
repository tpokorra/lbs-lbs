%global __python %{__python3}

Name:           lightbuildserver
Version:        0.1.0
Release:        1%{?dist}
Summary:        Build packages for various Linux distributions and run nightly jobs

License:        LGPLv2+
URL:            http://www.lightbuildserver.org
Source0:        https://github.com/SolidCharity/LightBuildServer/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:        %{name}-nginx.conf
Source2:        %{name}-uwsgi.ini
Source3:        %{name}-init.sh

BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       python3
Requires:       python3-bottle
Requires:       python3-PyYAML
Requires:       uwsgi-plugin-python3
Requires:       nginx

%description
LightBuildServer for building rpm and deb packages and running other jobs too, using Docker containers.

%package docker
Summary:        Scripts for creating docker containers for the LightBuildServer
Requires:       docker-io

%description docker
This package provides some scripts useful for creating docker containers.
They are needed by LightBuildServer to build on various Linux Distributions.

%package lxc
Summary:        Scripts for creating LXC containers for the LightBuildServer
Requires:       lxc lxc-extra lxc-templates gpg libvirt

%description lxc
This package provides some scripts useful for creating LXC containers.
They are needed by LightBuildServer to build on various Linux Distributions.

%prep
%setup -q -n %{name}-%{version}

%build
# Nothing to build

%install
install -dm 755 %{buildroot}%{_datadir}/%{name}

# install content
for d in $(find . -mindepth 1 -maxdepth 1 -type d ); do
    cp -a "$d" %{buildroot}%{_datadir}/%{name}
done
cp config-sample.yml %{buildroot}%{_datadir}/%{name}/config.yml
rm %{buildroot}%{_datadir}/%{name}/web/*.sh
mv %{buildroot}%{_datadir}/%{name}/docker-scripts %{buildroot}%{_datadir}
mv %{buildroot}%{_datadir}/%{name}/lxc-scripts %{buildroot}%{_datadir}

# initial config
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/nginx/conf.d/%{name}.conf
install -Dpm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/uwsgi.d/%{name}.ini
install -Dpm 755 %{SOURCE3} %{buildroot}%{_datadir}/%{name}-init.sh

%files
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config.yml
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/*.py
%dir %{_datadir}/%{name}/lib/__pycache__
%{_datadir}/%{name}/lib/__pycache__/*.pyo
%{_datadir}/%{name}/lib/__pycache__/*.pyc
%dir %{_datadir}/%{name}/web
%{_datadir}/%{name}/web/*.py
%dir %{_datadir}/%{name}/web/__pycache__
%{_datadir}/%{name}/web/__pycache__/*.pyo
%{_datadir}/%{name}/web/__pycache__/*.pyc
%dir %{_datadir}/%{name}/web/ext/bootbox
%{_datadir}/%{name}/web/ext/bootbox/*
%dir %{_datadir}/%{name}/web/css
%{_datadir}/%{name}/web/css/*.css
%dir %{_datadir}/%{name}/web/views
%{_datadir}/%{name}/web/views/*.tpl
%{_sysconfdir}/nginx/conf.d/%{name}.conf
%{_sysconfdir}/uwsgi.d/%{name}.ini

%files docker
%dir %{_datadir}/docker-scripts/Dockerfiles
%{_datadir}/docker-scripts/Dockerfiles/Dockerfile.*
%{_datadir}/docker-scripts/Readme.md
%{_datadir}/docker-scripts/*.sh

%files lxc
%dir %{_datadir}/lxc-scripts
%{_datadir}/lxc-scripts/*.sh
%{_datadir}/lxc-scripts/*.tpl
%{_datadir}/lxc-scripts/*.patch
%{_datadir}/lxc-scripts/Readme.md

%changelog
* Thu Jun 18 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.1.0-1
- Initial package for LightBuildServer
