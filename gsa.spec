Summary: 	Greenbone Security Assistant
Name:		gsa
Version:	2.0.1
Release:	2
Source0:		http://wald.intevation.org/frs/download.php/561/greenbone-security-assistant-%version.tar.gz
Patch0:		greenbone-security-assistant-2.0.1-build.patch
Group:		System/Configuration/Networking
Url:		https://www.openvas.org
License:	GPLv2+
BuildRequires:	cmake
BuildRequires:	openvas-devel >= 4.0
BuildRequires:	libmicrohttpd-devel >= 0.9.8
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
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
export LDFLAGS="-lopenvas_base -lopenvas_misc"
%cmake -DSYSCONFDIR=%{_sysconfdir}
%make

%install
%makeinstall_std -C build

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/openvas/gsad_log.conf
%{_sbindir}/gsad
%{_mandir}/man8/gsad.8.*
%{_datadir}/openvas/gsa


%changelog
* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 649869
- BR xslt
- import gsa

