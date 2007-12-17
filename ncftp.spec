%define name 		ncftp
%define version		3.2.0
%define release		%mkrel 1
%define _localstatedir	/var

Summary:	An improved FTP client
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group: 		Networking/File transfer
URL:		http://www.ncftp.com/
BuildRequires:	ncurses-devel
License:	Artistic
Source0:	ftp://ftp.ncftp.com/ncftp/ncftp-%{version}-src.tar.bz2
Patch0:		ncftp-confirm.patch.bz2 
Patch1:		ncftp-3.1.6-DESTDIR.patch.bz2
Patch3: 	ncftp-3.0.3-resume.patch.bz2
Patch5:		ncftp-3.1.9-suspend.patch.bz2
# P6 from ftp://ftp.kame.net/pub/kame/misc
Patch6:		ncftp-320-v6-20061109b.diff.gz
Patch7:		ncftp-3.1.1-EPLF.diff.bz2
# yves 3.1.1-1mdk
# requested by Yura Gusev <elendal@w4technology.com>
# adapted to 3.1.1 from http://www.fefe.de/ncftp/ncftp-3.0-EPLF.diff
# It will allow ncftp to work with publicfile. http://publicfile.org/


%description
Ncftp is an improved FTP client.  Ncftp's improvements include support
for command line editing, command histories, recursive gets, automatic
anonymous logins and more.

%prep

%setup -q
%patch0 -p0 -b .confirm 
%patch1 -p1
%patch3 -p1 -b .res
%patch5 -p1 -b .suspend
%patch6 -p1 -b .ipv6
%patch7 -p1 -b .eplf

%build
%configure --enable-signals --enable-ipv6
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}
%makeinstall BINDIR=$RPM_BUILD_ROOT%{_bindir} 

# yves - 3.1.1-1mdk - fix doc perm
find doc -type f -exec chmod 0644 {} \;

rm -f doc/*windows.txt

%clean
rm -fr %{buildroot};

%files
%defattr(-,root,root)
%doc doc/*.txt README.txt README.v6
%{_bindir}/*
%{_mandir}/*/*
