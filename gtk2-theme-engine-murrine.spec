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
Source2:	http://www.kernow-webhosting.com/~bvc/theme/gtk/murrine/Murrina-Aqua.tar.gz
# Source2-md5:	f1daafb69654ca3abe9dbebcd227a073
Source3:	http://www.kernow-webhosting.com/~bvc/theme/gtk/murrine/Murrina-Blu.tar.gz
# Source3-md5:	0e41b76df35bc0fa4f29b23f3ee60944
Source4:	http://www.kernow-webhosting.com/~bvc/theme/gtk/murrine/Murrina-Graphite.tar.gz
# Source4-md5:	fcb8b7bd0bcb33f3318cd284368f817c
Source5:	http://www.kernow-webhosting.com/~bvc/theme/gtk/murrine/Murrina-Green.tar.gz
# Source5-md5:	09d97f235fd74025561814a84c7ee38c
Source6:	http://www.kernow-webhosting.com/~bvc/theme/gtk/murrine/Murrina-M.tar.gz
# Source6-md5:	3852de905831954515fe78b3e547d28d
Source7:	http://www.kernow-webhosting.com/~bvc/theme/gtk/murrine/Murrina-Olive.tar.gz
# Source7-md5:	90857970e2d3637ec1701b802c02b28a
Source8:	http://www.kernow-webhosting.com/~bvc/theme/gtk/murrine/Murrina-Pink.tar.gz
# Source8-md5:	00fbc05769c5ac157bbd08b8a32934f8
Source9:	http://www.kernow-webhosting.com/~bvc/theme/gtk/murrine/Murrina-Purple.tar.gz
# Source9-md5:	6d20378ca02cc6383d721c52e5e0ff48
Source10:	http://www.kernow-webhosting.com/~bvc/theme/gtk/murrine/MurrinaStyle.tar.gz
# Source10-md5:	86f26b4f1ebb4d1625ce54bbe4599015
Source11:	http://cimi.netsons.org/media/download_gallery/MurrinaGilouche.tar.bz2
# Source11-md5:	70189ec03e792c3138741d4eb5b198f8
Source12:	http://www.gnome-look.org/content/files/44430-MurrinaLoveGray.tar.bz2
# Source12-md5:	240563e3b35e3df5f3c1e9ecb03c44a6
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
tar zxvf %{SOURCE2}
tar zxvf %{SOURCE3}
tar zxvf %{SOURCE4}
tar zxvf %{SOURCE5}
tar zxvf %{SOURCE6}
tar zxvf %{SOURCE7}
tar zxvf %{SOURCE8}
tar zxvf %{SOURCE9}
tar zxvf %{SOURCE10}
tar jxvf %{SOURCE11}
tar jxvf %{SOURCE12}

# TODO: add to some package
rm LoveGray.cgwdtheme

find . -name '*~' -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/themes/*
