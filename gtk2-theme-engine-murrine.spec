Summary:	murrine theme
Name:		gtk2-theme-engine-murrine
Version:	0.10
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://cimi.netsons.org/media/download_gallery/murrine/murrine-%{version}.tar.bz2
# Source0-md5:	a114aa2f452c508b9524399ec598554f
Source1:	http://cimi.netsons.org/media/download_gallery/MurrineThemePack.tar.bz2
# Source1-md5:	ac4388fcd24180843a6de24db3200d9a
URL:		http://cimi.netsons.org/pages/murrine.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Murrine" is an Italian word meaning the glass artworks done by
Venicians glass blowers. They're absolutely wonderful and colorful.
Murrine has this object to provide the ability to make your desktop
look like a "Murrina", which is the Italian singular of the name
"Murrine".

%prep
%setup -q -n murrine-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-animation
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.{a,la}

cd $RPM_BUILD_ROOT%{_datadir}/themes
tar jxvf %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/themes/*
