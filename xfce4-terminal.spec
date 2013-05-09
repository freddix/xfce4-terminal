%define		xfce_version	4.10.0

Summary:	X Terminal Emulator
Name:		xfce4-terminal
Version:	0.6.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-terminal/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	d5cdb302bd770c9f2d30262c26639006
Patch0:		%{name}-freddix.patch
URL:		http://www.os-cillation.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	exo-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	ncurses-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
BuildRequires:	vte2-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminal is a lightweight and easy to use terminal emulator for the
X windowing system, with some new ideas and features that makes it
unique among X terminal emulators.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--enable-dbus
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	docdir="%{_datadir}/xfce4/help/%{name}/html"

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xfce4/terminal
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/%{name}.1*

