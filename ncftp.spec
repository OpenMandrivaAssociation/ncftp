Summary:	An improved FTP client
Name:		ncftp
Version:	3.2.5
Release:	2
Group:		Networking/File transfer
URL:		http://www.ncftp.com/
BuildRequires:	pkgconfig(ncursesw)
License:	Artistic
Source0:	ftp://ftp.ncftp.com/ncftp/ncftp-%{version}-src.tar.bz2
Patch0:		ncftp-confirm.patch
Patch3:		ncftp-3.0.3-resume.patch
Patch5:		ncftp-3.1.9-suspend.patch
# requested by Yura Gusev <elendal@w4technology.com>
# adapted to 3.1.1 from http://www.fefe.de/ncftp/ncftp-3.0-EPLF.diff
# It will allow ncftp to work with publicfile. http://publicfile.org/
Patch7:		ncftp-3.1.1-EPLF.diff
Patch8:		ncftp-3.2.3-fix-help-cmd.patch

%description
Ncftp is an improved FTP client.  Ncftp's improvements include support
for command line editing, command histories, recursive gets, automatic
anonymous logins and more.

%prep
%setup -q
%patch0 -p0 -b .confirm~ 
%patch3 -p1 -b .resume~
%patch5 -p1 -b .suspend~
%patch7 -p0 -b .eplf̈~
%patch8 -p1 -b .help~

%build
%configure	--enable-signals \
		--enable-ipv6
%make

%install
%makeinstall_std

rm doc/*indows.txt

%files
%doc doc/*.txt README.txt
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Thu Dec 27 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.2.5-2
- cleanups

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 3.2.5-1mdv2011.0
+ Revision: 675873
- New version 3.2.5

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.3-3
+ Revision: 666599
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.3-2mdv2011.0
+ Revision: 606812
- rebuild

* Fri Jan 01 2010 Funda Wang <fwang@mandriva.org> 3.2.3-1mdv2010.1
+ Revision: 484836
- New version 3.2.3

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.2.2-4mdv2010.0
+ Revision: 426224
- rebuild

* Mon Feb 16 2009 Luiz Fernando Capitulino <lcapitulino@mandriva.com> 3.2.2-3mdv2009.1
+ Revision: 341069
- Make help command work

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.2-2mdv2009.1
+ Revision: 317478
- rediffed some fuzzy patches

* Tue Aug 12 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.2-1mdv2009.0
+ Revision: 271193
- 3.2.2
- bunzipped the patches
- new ipv6 patch

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.2.0-4mdv2009.0
+ Revision: 223335
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 3.2.0-3mdv2008.1
+ Revision: 153278
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 27 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.2.0-1mdv2008.0
+ Revision: 31793
- new release: 3.2.2
- update P6
- be sure to wipe out buildroot at the beginning of %%install
- Import ncftp



* Mon Sep 18 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 3.1.9-4mdv2007.0
- Rebuild

* Wed Mar 08 2006 Pascal Terjan <pterjan@mandriva.org> 3.1.9-3mdk
- Add ipv6 support from kame (P6)
- mkrel
- don't ship docs about usage under windows

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 3.1.9-2mdk
- Rebuild

* Sun Jun 12 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 3.1.9-1mdk
- 3.1.9
- regenerate P5

* Wed Jul 21 2004 Pascal Terjan <pterjan@mandrake.org> 3.1.8-1mdk
- 3.1.8

* Fri Apr 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.1.7-1mdk
- 3.1.7

* Fri Feb 20 2004 David Baudens <baudens@mandrakesoft.com> 3.1.6-4mdk
- Remove menu entry

* Sun Nov 16 2003 Pascal Terjan <CMoi@tuxfamily.org> 3.1.6-3mdk
- disable patches 6 and 8 (ipv6 support). Looks like it breaks ipv4 data
  connections when not in passive mode.

* Fri Nov 14 2003 Pascal Terjan <CMoi@tuxfamily.org> 3.1.6-2mdk
- ipv6 patch is back

* Wed Oct 15 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.1.6-1mdk
- 3.1.6 (closes #6110)
- regenerated P1
- don't bzip2 icons in src.rpm
- cleanups

* Sun Jun 15 2003 Stefan van der Eijk <stefan@eijk.nu> 3.1.5-3mdk
- BuildRequires

* Thu Jan 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.1.5-2mdk
- build release

* Thu Oct 24 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.1.5-1mdk
- new release

* Thu Jul 25 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.1.4-1mdk
- new release
- gcc-3.2 rebuild

* Tue May 07 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.1.3-2mdk
- Automated rebuild in gcc3.1 environment

* Thu Apr 04 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.1.3-1mdk
- new release

* Sun Jan 20 2002 Yves Duret <yduret@mandrakesoft.com> 3.1.1-2mdk
- added patch7 to add support to publicfile.org 
  requested by Yura Gusev <elendal@w4technology.com>

* Sun Jan 20 2002 Yves Duret <yduret@mandrakesoft.com> 3.1.1-1mdk
- version 3.1.1
- rediff patch1 ncftp-DESTDIR.patch
- remove patch6 ipv6 support
- png icons, fix menu entry
- spec clean up, more globbing, more macros
- new %%doc section, fix doc permissions

* Sat Nov 10 2001 Yves Duret <yduret@mandrakesoft.com> 3.0.4-1mdk
- version 3.0.4
- removed patch merged upstream
- readded ipv6 patch & support

* Sun Sep 30 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 3.0.3-4mdk
- RH patch merge (suspend, crash patch).

* Thu Aug 30 2001 David BAUDENS <baudens@mandrakesoft.com> 3.0.3-3mdk
- Use new icons

* Mon Jul 16 2001 Yves Duret <yduret@mandrakesoft.com> 3.0.3-2mdk
- rebuild
- Default to auto-resume=yes (rh #28705) by patch3

* Tue May  1 2001 Yves Duret <yduret@mandrakesoft.com> 3.0.3-1mdk
- version 3.0.3 for general usage
- added ipv6 support (patch2)
- spec clean up: globing for %%files, typo
- added URL tag

* Wed Dec 20 2000 Yves Duret <yduret@mandrakesoft.com> 3.0.2-2mdk
- use %%make macro
- fixed some file's permission
- fixed menu entry
- added a large icon

* Thu Oct 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.2-1mdk
- 3.0.2.

* Fri Sep 29 2000 Daouda Lo <daouda@mandrakesoft.com> 3.0.1-8mdk
- icons should be tranparents.

* Fri Sep 29 2000 Daouda Lo <daouda@mandrakesoft.com> 3.0.1-7mdk
- add icons
 
* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.0.1-6mdk
- automatically added BuildRequires

* Mon Jul 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.0.1-4mdk
- use new macros in post and postun scripts

* Thu Jul 06 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 3.0.1-3mdk.ipv6
- IPv6 support

* Sun Jun 04 2000 David BAUDENS <baudens@mandrakesoft.com> 3.0.1-3mdk
- Fix and use a real %%doc

* Wed Apr  5 2000 Denis Havlik <denis@mandrakesoft.com> 3.0.1-2mdk
- fixed source path

* Mon Apr  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0.1-1mdk
- Add menu.
- Change license to Artistic.
- spec-helper purification.
- Upgrade groups.
- 3.0.1 final (correct a lot of bugs).

* Fri Jan  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0beta21-4mdk
- sed 's/1/True/'

* Wed Jan  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0beta21-3mdk
- Oxygen Release.
- Disble confirmation in exit by default.
