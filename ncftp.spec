%define _localstatedir /var

Summary:	An improved FTP client
Name:		ncftp
Version:	3.2.3
Release:	%mkrel 2
Group: 		Networking/File transfer
URL:		http://www.ncftp.com/
BuildRequires:	ncurses-devel
License:	Artistic
Source0:	ftp://ftp.ncftp.com/ncftp/ncftp-%{version}-src.tar.bz2
Patch0:		ncftp-confirm.patch
Patch3: 	ncftp-3.0.3-resume.patch
Patch5:		ncftp-3.1.9-suspend.patch
# P6 from ftp://ftp.kame.net/pub/kame/misc
Patch6:		ncftp-323-v6-20091109.diff
Patch7:		ncftp-3.1.1-EPLF.diff
Patch8:		ncftp-3.2.3-fix-help-cmd.patch
# yves 3.1.1-1mdk
# requested by Yura Gusev <elendal@w4technology.com>
# adapted to 3.1.1 from http://www.fefe.de/ncftp/ncftp-3.0-EPLF.diff
# It will allow ncftp to work with publicfile. http://publicfile.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Ncftp is an improved FTP client.  Ncftp's improvements include support
for command line editing, command histories, recursive gets, automatic
anonymous logins and more.

%prep

%setup -q
%patch0 -p0 -b .confirm 
%patch3 -p0 -b .resume
%patch5 -p1 -b .suspend
%patch6 -p1 -b .ipv6
%patch7 -p0 -b .eplf
%patch8 -p1 -b .help

%build
%configure \
    --enable-signals \
    --enable-ipv6
%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}

%makeinstall_std

# yves - 3.1.1-1mdk - fix doc perm
find doc -type f -exec chmod 0644 {} \;

rm -f doc/*windows.txt

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc doc/*.txt README.txt README.v6
%{_bindir}/*
%{_mandir}/*/*
