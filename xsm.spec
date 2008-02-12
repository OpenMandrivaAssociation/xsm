Name: xsm
Version: 1.0.1
Release: %mkrel 6
Summary: X Session Manager
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

Patch1: 0001-Remove-build-dependency-on-rsh-or-similar-program.patch

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

%patch1 -p1

%build
autoreconf -ifs
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xsm
%{_libdir}/X11/xsm/system.xsm
%{_datadir}/X11/app-defaults/XSm
%{_mandir}/man1/xsm.1*
