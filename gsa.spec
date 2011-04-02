Summary: 	Greenbone Security Assistant
Name:		gsa
Version:	2.0.1
Release:	%mkrel 1
Source:		http://wald.intevation.org/frs/download.php/561/greenbone-security-assistant-%version.tar.gz
Patch0:		greenbone-security-assistant-2.0.1-build.patch
Group:		System/Configuration/Networking
Url:		http://www.openvas.org
License:	GPLv2+
BuildRoot:	%{_tmppath}/%name-%{version}-root
BuildRequires:	cmake
BuildRequires:	openvas-devel >= 4.0
BuildRequires:	libmicrohttpd-devel >= 0.9.8
BuildRequires:	libxslt-devel
BuildRequires:	libxml2-devel
BuildRequires:	glib2-devel
BuildRequires:	gnutls-devel
BuildRequires:	xsltproc

%description
The Greenbone Security Assistant is a web application that
connects to the OpenVAS Manager and OpenVAS Administrator
to provide for a full-featured user interface for
vulnerability management.

%prep
%setup -q -n greenbone-security-assistant-%version
%patch0 -p0 -b .build

sed -i -e 's#-Werror##' `grep -rl Werror *|grep CMakeLists.txt`

%build
%cmake -DSYSCONFDIR=%{_sysconfdir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/openvas/gsad_log.conf
%{_sbindir}/gsad
%{_mandir}/man8/gsad.8.*
%{_datadir}/openvas/gsa
