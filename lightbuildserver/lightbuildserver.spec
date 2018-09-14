%global __python %{__python3}

Name:           lightbuildserver
Version:        0.6.0
Release:        %{release}%{?dist}
Summary:        Build packages for various Linux distributions and run nightly jobs

License:        LGPLv2+
URL:            http://www.lightbuildserver.org
Source0:        https://github.com/SolidCharity/LightBuildServer/archive/master.tar.gz
Source1:        %{name}-nginx.conf
Source2:        %{name}-uwsgi.ini
Source3:        %{name}-init.sh
Source4:        %{name}-cron.sh
Source5:        %{name}-logrotate

BuildArch:      noarch

%if 0%{?rhel} >= 7
BuildRequires:  python34-devel
Requires:       python34
Requires:       python34-bottle
Requires:       python34-PyYAML
Requires:       python34-mysql
Requires:       python34-requests
Requires:       python34-copr
Requires:       uwsgi-plugin-python34

%else
BuildRequires:  python3-devel
Requires:       python3
Requires:       python3-bottle
Requires:       python3-PyYAML
Requires:       python3-mysql
Requires:       python3-copr
Requires:       uwsgi-plugin-python3
%endif

Requires:       uwsgi-logger-file
Requires:       nginx
Requires:       sqlite
Requires:       mariadb-server
Requires:       tar
Requires:       rsync
Requires:       wget
Requires:       crontabs
Requires:       rpm-build

%description
LightBuildServer for building rpm and deb packages and running other jobs too, using Docker and LXC containers.

%prep
%setup -q -n LightBuildServer-master

%build
%if 0%{?rhel} >= 8 || 0%{?fedora} >= 24
# compile the py files
%{__python} -m compileall -l web
%{__python} -m compileall -l lib
%endif

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
rm -Rf %{buildroot}%{_datadir}/%{name}/dply
rm -Rf %{buildroot}%{_datadir}/%{name}/test

# initial config
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/nginx/conf.d/%{name}.conf
install -Dpm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/uwsgi.d/%{name}.ini
install -Dpm 644 config-sample.yml %{buildroot}%{_sysconfdir}/%{name}/config.yml
install -Dpm 755 %{SOURCE3} %{buildroot}%{_datadir}/%{name}/init.sh
install -Dpm 755 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/cron.sh
install -Dpm 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

%files
%defattr(-,uwsgi,uwsgi,-)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/init.sh
%{_datadir}/%{name}/cron.sh
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/*.py
%dir %{_datadir}/%{name}/lib/__pycache__

# for python <= 3.5, still include the pyo files
%if 0%{?rhel} >= 8 || 0%{?fedora} >= 24
%else
%{_datadir}/%{name}/lib/__pycache__/*.pyo
%{_datadir}/%{name}/web/__pycache__/*.pyo
%endif

%{_datadir}/%{name}/lib/__pycache__/*.pyc
%dir %{_datadir}/%{name}/web
%{_datadir}/%{name}/web/*.py
%dir %{_datadir}/%{name}/web/__pycache__
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
%config(noreplace) %{_sysconfdir}/%{name}/config.yml
%dir %{_sharedstatedir}/%{name}
%dir %{_sharedstatedir}/%{name}/db
%dir %{_sharedstatedir}/%{name}/src
%dir %{_sharedstatedir}/%{name}/logs
%dir %{_sharedstatedir}/%{name}/repos
%dir %{_sharedstatedir}/%{name}/tarballs
%defattr(-,root,root,-)
%{_sysconfdir}/logrotate.d/%{name}

%changelog
* Sat Dec 23 2017 Timotheus Pokorra <tp@tbits.net> - 0.6.0-0
- new release 0.6

* Sat Dec 31 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.5.0-0
- new release 0.5

* Thu Dec 15 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.4.0-0
- new release 0.4

* Wed Sep 28 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.3.0-0
- new release 0.3

* Thu Nov 26 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.2.5-0
- new release 0.2.5

* Mon Sep 28 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.2.4-0
- new release 0.2.4, with some fixes, and logrotate

* Fri Aug 21 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.2.3-0
- new release 0.2.3, with fix for cancelling hanging builds

* Tue Aug 18 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.2.2-0
- new release 0.2.2, with cronjob for processing the build queue

* Fri Aug 14 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.2.0-0
- new release 0.2.0, with sqlite for saving the state

* Wed Jul 08 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.1.0-2
- build the lxc and docker scripts packages in separate spec files

* Thu Jun 18 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.1.0-1
- Initial package for LightBuildServer
