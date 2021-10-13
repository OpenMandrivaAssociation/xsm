Name: xsm
Version: 1.0.4
Release: 3
Summary: X Session Manager
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRequires: pkgconfig(xaw7)
BuildRequires: pkgconfig(xt)
BuildRequires: x11-util-macros >= 1.0.1
#BuildRequires: netkit-rsh

%description
Xsm is a session manager. A session is a group of applications, each of which
has a particular state. xsm allows you to create arbitrary sessions - for
example, you might have a "light" session, a "development" session, or an
"xterminal" session. Each session can have its own set of applications. Within
a session, you can perform a "checkpoint" to save application state, or a
"shutdown" to save state and exit the session. When you log back in to the
system, you can load a specific session, and you can delete sessions you no
longer want to keep.

Some session managers simply allow you to manually specify a list of
applications to be started in a session. xsm is more powerful because it lets
you run applications and have them automatically become part of the session. On
a simple level, xsm is useful because it gives you this ability to easily
define which applications are in a session. The true power of xsm, however, can
be taken advantage of when more and more applications learn to save and restore
their state.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xsm
%{_sysconfdir}/X11/xsm/system.xsm
%{_datadir}/X11/app-defaults/XSm
%{_mandir}/man1/xsm.1*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-10mdv2011.0
+ Revision: 671368
- mass rebuild

* Mon Sep 27 2010 Thierry Vignaud <tv@mandriva.org> 1.0.2-9mdv2011.0
+ Revision: 581483
- remove patch 1 (merged upstream)
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-8mdv2010.1
+ Revision: 524469
- rebuilt for 2010.1

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.1-7mdv2009.1
+ Revision: 366728
- BR rsh
- no more autoreconf needed

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-7mdv2009.0
+ Revision: 226085
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-6mdv2008.1
+ Revision: 166808
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 154308
- Remove build dependency on rsh or similar program.
- Updated BuildRequires and resubmit package.
- Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 74985
- do not hardcode X11 extension!!!
- do not hardcode lzma extension!!!


* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 21:04:00 (59510)
- rebuild to fix libXaw.so.8 dependency

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:09:04 (31709)
- fill in a few more missing descriptions

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

