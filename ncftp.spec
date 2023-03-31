# Workaround duplicate symbols
%global optflags %{optflags} -fcommon

Summary:	An improved FTP client
Name:		ncftp
Version:	3.2.6
Release:	6
Group:		Networking/File transfer
License:	Artistic
Url:		http://www.ncftp.com/
Source0:	ftp://ftp.ncftp.com/ncftp/ncftp-%{version}-src.tar.xz
Patch0:		ncftp-confirm.patch
Patch3:		ncftp-3.0.3-resume.patch
Patch5:		ncftp-3.1.9-suspend.patch
# requested by Yura Gusev <elendal@w4technology.com>
# adapted to 3.1.1 from http://www.fefe.de/ncftp/ncftp-3.0-EPLF.diff
# It will allow ncftp to work with publicfile. http://publicfile.org/
Patch7:		ncftp-3.1.1-EPLF.diff
Patch8:		ncftp-3.2.3-fix-help-cmd.patch
Patch9:		ncftp-3.1.5-pmeter.patch
BuildRequires:	pkgconfig(ncursesw)

%description
Ncftp is an improved FTP client.  Ncftp's improvements include support
for command line editing, command histories, recursive gets, automatic
anonymous logins and more.

%prep
%setup -q
%patch0 -p0 -b .confirm~ 
%patch3 -p1 -b .resume~
%patch5 -p1 -b .suspend~
%patch7 -p1 -b .epl~
%patch8 -p1 -b .help~
%patch9 -p1 -b .pmeter~

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
