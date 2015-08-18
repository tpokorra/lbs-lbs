%global __python %{__python3}

Name:           lightbuildserver
Version:        0.2.2
Release:        %{release}%{?dist}
Summary:        Build packages for various Linux distributions and run nightly jobs

License:        LGPLv2+
URL:            http://www.lightbuildserver.org
Source0:        https://github.com/SolidCharity/LightBuildServer/archive/master.tar.gz
Source1:        %{name}-nginx.conf
Source2:        %{name}-uwsgi.ini
Source3:        %{name}-init.sh
Source4:        %{name}-cron.sh

BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       python3
Requires:       python3-bottle
Requires:       python3-PyYAML
Requires:       uwsgi-plugin-python3
Requires:       nginx
Requires:       sqlite
Requires:       tar
Requires:       rsync
Requires:       wget
Requires:       crontabs

%description
LightBuildServer for building rpm and deb packages and running other jobs too, using Docker and LXC containers.

%prep
%setup -q -n LightBuildServer-master

%build
# Nothing to build

%install
install -dm 755 %{buildroot}%{_datadir}/%{name}
install -dm 755 %{buildroot}%{_sharedstatedir}/%{name}
install -dm 700 %{buildroot}%{_sharedstatedir}/%{name}/db
install -dm 700 %{buildroot}%{_sharedstatedir}/%{name}/src
install -dm 700 %{buildroot}%{_sharedstatedir}/%{name}/logs
install -dm 755 %{buildroot}%{_sharedstatedir}/%{name}/repos
install -dm 755 %{buildroot}%{_sharedstatedir}/%{name}/tarballs

# install content
for d in $(find . -mindepth 1 -maxdepth 1 -type d ); do
    cp -a "$d" %{buildroot}%{_datadir}/%{name}
done
rm %{buildroot}%{_datadir}/%{name}/web/*.sh
rm -Rf %{buildroot}%{_datadir}/%{name}/docker-scripts
rm -Rf %{buildroot}%{_datadir}/%{name}/lxc-scripts

# initial config
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/nginx/conf.d/%{name}.conf
install -Dpm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/uwsgi.d/%{name}.ini
install -Dpm 644 config-sample.yml %{buildroot}%{_sysconfdir}/%{name}/config.yml
install -Dpm 755 %{SOURCE3} %{buildroot}%{_datadir}/%{name}/init.sh
install -Dpm 755 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/cron.sh

%files
%defattr(-,uwsgi,uwsgi,-)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/init.sh
%{_datadir}/%{name}/cron.sh
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
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/config.yml
%dir %{_sharedstatedir}/%{name}
%dir %{_sharedstatedir}/%{name}/db
%dir %{_sharedstatedir}/%{name}/src
%dir %{_sharedstatedir}/%{name}/logs
%dir %{_sharedstatedir}/%{name}/repos
%dir %{_sharedstatedir}/%{name}/tarballs

%changelog
* Tue Aug 18 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.2.2-0
- new release 0.2.2, with cronjob for processing the build queue

* Fri Aug 14 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.2.0-0
- new release 0.2.0, with sqlite for saving the state

* Wed Jul 08 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.1.0-2
- build the lxc and docker scripts packages in separate spec files

* Thu Jun 18 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.1.0-1
- Initial package for LightBuildServer
