# Workaround duplicate symbols
#global optflags %{optflags} -fcommon

Summary:	An improved FTP client
Name:		ncftp
Version:	3.2.9
Release:	1
Group:		Networking/File transfer
License:	Artistic
Url:		https://www.ncftp.com/
Source0:	https://www.ncftp.com/public_ftp/ncftp/ncftp-%{version}-src.tar.gz
Patch0:		ncftp-confirm.patch
Patch5:		ncftp-3.1.9-suspend.patch
# requested by Yura Gusev <elendal@w4technology.com>
# adapted to 3.1.1 from http://www.fefe.de/ncftp/ncftp-3.0-EPLF.diff
# It will allow ncftp to work with publicfile. http://publicfile.org/
Patch7:		ncftp-3.1.1-EPLF.diff
Patch8:		ncftp-3.2.3-fix-help-cmd.patch
BuildRequires:	pkgconfig(ncursesw)

%description
Ncftp is an improved FTP client.  Ncftp's improvements include support
for command line editing, command histories, recursive gets, automatic
anonymous logins and more.

%prep
%autosetup -p1

%build
%configure \
	--enable-signals \
	--enable-ipv6
%make STRIPFLAG="" STRIP="true"

%install
%makeinstall_std STRIPFLAG="" STRIP="true"

rm doc/*indows.txt

%files
%doc doc/*.txt README.txt
%{_bindir}/*
%{_mandir}/*/*
