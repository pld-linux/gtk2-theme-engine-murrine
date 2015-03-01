Summary:	Murrine GTK2 engine
Summary(pl.UTF-8):	Motyw murrine
Name:		gtk2-theme-engine-murrine
Version:	0.98.2
Release:	2
License:	LGPL v2 or LGPL v3
Group:		Themes/GTK+
Source0:	http://ftp.gnome.org/pub/GNOME/sources/murrine/0.98/murrine-%{version}.tar.xz
# Source0-md5:	bf01e0097b5f1e164dbcf807f4b9745e
Source1:	http://cimi.netsons.org/media/download_gallery/MurrineThemePack.tar.bz2
# Source1-md5:	414013c22d1fb3954a5c3d09499c80b2
Source2:	http://cimi.netsons.org/media/download_gallery/MurrinaLoveGray.tar.bz2
# Source2-md5:	31ce9fce5114c1cfe471dc614de539cc
Source3:	http://cimi.netsons.org/media/download_gallery/MurrinaGilouche.tar.bz2
# Source3-md5:	65d8f1f28f9c8ed14b15ec894dd0bfc0
Source4:	http://cimi.netsons.org/media/download_gallery/MurrinaAquaIsh.tar.bz2
# Source4-md5:	e18bb191756ed1b793432f6bc7607db4
Source5:	http://cimi.netsons.org/media/download_gallery/MurrinaVerdeOlivo.tar.bz2
# Source5-md5:	7fb55d613c31a1455a9db6c121fff0bb
Source6:	http://cimi.netsons.org/media/download_gallery/MurrinaFancyCandy.tar.bz2
# Source6-md5:	5a66f3de41547a0a27f925ac8d8d8c46
Source7:	murrina-all.tar.gz
# Source7-md5:	48dc71a8f627662864e9cccdca8b5391
URL:		https://launchpad.net/murrine
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Murrine" is an Italian word meaning the glass artworks done by
Venicians glass blowers. They're absolutely wonderful and colorful.
Murrine has this object to provide the ability to make your desktop
look like a "Murrina", which is the Italian singular of the name
"Murrine".

%description -l pl.UTF-8
"Murrine" to włoskie słowo oznaczające szklane dzieła wykonywane przez
wenecjańskich dmuchaczy szkła. Są absolutnie cudowne i kolorowe.
Murrine zawiera ten obiekt, co pozwala uczynić pulpit wyglądającym jak
"Murrina" (liczba pojedyncza od nazwy "Murrine").

%prep
%setup -q -n murrine-%{version}

%{__sed} -i -e 's,AM_CONFIG_HEADER,AC_CONFIG_HEADERS,' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	--enable-animation \
	--enable-animationrtl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la

cd $RPM_BUILD_ROOT%{_datadir}/themes
tar jxf %{SOURCE1}
tar jxf %{SOURCE2}
tar jxf %{SOURCE3}
tar jxf %{SOURCE4}
tar jxf %{SOURCE5}
tar jxf %{SOURCE6}
tar zxf %{SOURCE7}

find -name '*~' -print -delete

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/gtk-engines/murrine.xml
%dir %{_datadir}/themes
%{_datadir}/themes/MurrinaAquaIsh
%{_datadir}/themes/MurrinaCandy
%{_datadir}/themes/MurrinaCappuccino
%{_datadir}/themes/MurrinaEalm
%{_datadir}/themes/MurrinaFancyCandy
%{_datadir}/themes/MurrinaGilouche
%{_datadir}/themes/MurrinaLoveGray
%{_datadir}/themes/MurrinaNeoGraphite
%{_datadir}/themes/MurrinaVerdeOlivo

# from murrina-all.tar
%{_datadir}/themes/MurrinaStyle
%{_datadir}/themes/Murrina-Aqua
%{_datadir}/themes/Murrina-Blu
%{_datadir}/themes/Murrina-Graphite
%{_datadir}/themes/Murrina-Green
%{_datadir}/themes/Murrina-Olive
%{_datadir}/themes/Murrina-Pink
%{_datadir}/themes/Murrina-Purple
