Summary:	superkaramba - little interactive widgets on KDE desktop
Summary(pl):	superkaramba - ma�e interaktywne widgety na pulpicie KDE
Name:		superkaramba
Version:	0.26
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/netdragon/%{name}-%{version}.tar.gz
# Source0-md5:	68bf76ad1f0e5baee6e98c9611defb74
# news_pl created by Maciej "maciunio" Paczesny <maciunio(at)ask-bsi.org>
Source1:	news_pl.theme.tar.gz
# Source1-md5:	c92aa676f6f5eb57828febfd738d99b8
Source2:	OSXDocker.tar.bz2
# Source2-md5:	fb3a5175f55b582a7c123390ed3b5c66
# http://szpieg.gda.pl/  - made by Marcin Ciunelis <martin@ds.pg.gda.pl>
Source3:	szPieG-%{name}-0.1.tar.gz
# Source3-md5:	2336bd718ccf5deb06204e97248eeae0
Source4:	tuxbar-pzoom-0.17g.tar.gz
# Source4-md5:	04089c070215693833f2c5da7d8af8d2
URL:		http://netdragon.sourceforge.net/
BuildRequires:	kdelibs-devel > 3.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	libart_lgpl-static
BuildRequires:	libxml2-progs
BuildRequires:	%{__perl}
BuildRequires:	python-devel > 2.2
BuildRequires:	python-libs > 2.2
BuildRequires:	python-modules > 2.2
BuildRequires:	xmms-devel
Requires:	perl-libwww
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SuperKaramba is a tool that allows anyone to easily create and run
little interactive widgets on a KDE desktop.

%description -l pl
SuperKaramba to narz�dzie pozwalaj�ce na �atwe tworzenie i
uruchamianie ma�ych interaktywnych widget�w na pulpicie KDE.

%package themes
Summary:	Themes for %{name}
Summary(pl):	Motywy dla SuperKaramby
Group:		X11/Applications
Requires:	%{name}
Obsoletes:	%{name} < %{name}-0.4

%description themes
Themes for %{name}.

%description themes -l pl
Motywy dla SuperKaramby.

%prep
%setup -q -a1 -a2 -a3 -a4

%build
%{__perl} -pi -e "s@/home/maciunio/karamba/DynBar/script@%{_datadir}/themes/news_pl/script@" \
		news_pl.theme/*.theme
%{__perl} -pi -e "s@/home/genneth/files/Aqua@%{_pixmapsdir}/crystalsvg@" \
		OSXDocker/Conf.py

moc src/karamba.h -o src/karamba.moc
#rm -f missing
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
#%{__make} -f Makefile.cvs
LDFLAGS="-lpython2.2"; export LDFLAGS

%configure \
	--with-pythondir=/usr/lib/python2.2 \
	--with-extra-includes=/usr/include/python2.2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities \
	   $RPM_BUILD_ROOT%{_datadir}/themes/{OSXDocker/Icons,news_pl/{Pics/ikony,script},szPieG/{Pics,script}} \
	   $RPM_BUILD_ROOT%{_datadir}/themes/tuxbar/pics

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install src/karamba.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities

# Themes
install news_pl.theme/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/news_pl
install news_pl.theme/Pics/*.png $RPM_BUILD_ROOT%{_datadir}/themes/news_pl/Pics
install news_pl.theme/Pics/ikony/*.png $RPM_BUILD_ROOT%{_datadir}/themes/news_pl/Pics/ikony
install news_pl.theme/script/* $RPM_BUILD_ROOT%{_datadir}/themes/news_pl/script

install OSXDocker/OSXDocker.* $RPM_BUILD_ROOT%{_datadir}/themes/OSXDocker
install OSXDocker/Conf* $RPM_BUILD_ROOT%{_datadir}/themes/OSXDocker
install OSXDocker/Icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/OSXDocker/Icons
install OSXDocker/Buttons.txt $RPM_BUILD_ROOT%{_datadir}/themes/OSXDocker

install szPieG/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/szPieG
install szPieG/Pics/*.* $RPM_BUILD_ROOT%{_datadir}/themes/szPieG/Pics
install szPieG/script/*.* $RPM_BUILD_ROOT%{_datadir}/themes/szPieG/script

install tuxbar/tuxbar.* $RPM_BUILD_ROOT%{_datadir}/themes/tuxbar
install tuxbar/pics/*.png $RPM_BUILD_ROOT%{_datadir}/themes/tuxbar/pics

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/*.desktop

%files themes
%dir %{_datadir}/themes/news_pl
%dir %{_datadir}/themes/news_pl/Pics
%dir %{_datadir}/themes/news_pl/Pics/ikony
%dir %{_datadir}/themes/news_pl/script
%{_datadir}/themes/news_pl/*.theme
%{_datadir}/themes/news_pl/Pics/*.png
%{_datadir}/themes/news_pl/Pics/ikony/*
%attr(755,root,root) %{_datadir}/themes/news_pl/script/*

%dir %{_datadir}/themes/OSXDocker
%dir %{_datadir}/themes/OSXDocker/Icons
%{_datadir}/themes/OSXDocker/*.*
%{_datadir}/themes/OSXDocker/Icons/*.png

%dir %{_datadir}/themes/szPieG
%dir %{_datadir}/themes/szPieG/Pics
%dir %{_datadir}/themes/szPieG/script
%{_datadir}/themes/szPieG/*.*
%{_datadir}/themes/szPieG/Pics/*.*
%attr(755,root,root) %{_datadir}/themes/szPieG/script/*

%dir %{_datadir}/themes/tuxbar
%dir %{_datadir}/themes/tuxbar/pics
%{_datadir}/themes/tuxbar/tuxbar.*
%{_datadir}/themes/tuxbar/pics/*.png
