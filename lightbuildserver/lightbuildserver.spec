Name:           lightbuildserver
Version:        0.1.0
Release:        1%{?dist}
Summary:        Build packages for various Linux distributions and run nightly jobs

License:        LGPLv2+
URL:            http://www.lightbuildserver.org
Source0:        https://github.com/SolidCharity/LightBuildServer/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:        %{name}-nginx.conf
Source2:        %{name}-uwsgi.ini

BuildArch:      noarch

Requires:       python3
Requires:       python3-bottle
Requires:       python3-PyYAML
Requires:       uwsgi-plugin-python3
Requires:       nginx
Requires:       docker-io

%description
LightBuildServer for building rpm and deb packages and running other jobs too, using Docker containers.

%prep
%setup -q -n %{name}

%build
# Nothing to build

%install
install -dm 755 %{buildroot}%{_datadir}/%{name}

# install content
for d in $(find . -mindepth 1 -maxdepth 1 -type d ); do
    cp -a "$d" %{buildroot}%{_datadir}/%{name}
done
mv %{buildroot}%{_datadir}/%{name}/config-sample.yml %{buildroot}%{_datadir}/%{name}/config.yml

# initial config
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/nginx/conf.d/%{name}.conf
install -Dpm 644  %{SOURCE1} %{buildroot}%{_sysconfdir}/uwsgi.d/%{name}.ini

%files
%{buildroot}%{_datadir}/%{name}
%{_sysconfdir}/nginx/conf.d/%{name}.conf
%{_sysconfdir}/uwsgi.d/%{name}.ini

%changelog
* Thu Jun 18 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.1.0-1
- Initial package for LightBuildServer
