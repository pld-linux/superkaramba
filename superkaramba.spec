Summary:	Little interactive widgets on KDE desktop
Summary(pl):	Ma³e interaktywne widgety na pulpicie KDE
Name:		superkaramba
Version:	0.33
Release:	1.4
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/netdragon/%{name}-%{version}.tar.gz
# Source0-md5:	132d094a8e35383c757aaf5739fcb856
# Scripts widely used by superkaramba theme creators
Source1:	http://www.efd.lth.se/~d98hk/karamba/scripts/scripts.tar.gz
# Source1-md5:	94f0620854df678c4e7908679f139a78
#
# Here go modules, aka themes.
#
# szPieG theme
# http://szpieg.gda.pl/ - made by Marcin Ciunelis <martin@ds.pg.gda.pl>
Source2:	szPieG-%{name}-0.1.tar.gz
# Source2-md5:	2336bd718ccf5deb06204e97248eeae0
# tuxbar-pzoom theme
Source3:	tuxbar-pzoom-0.17g.tar.gz
# Source3-md5:	04089c070215693833f2c5da7d8af8d2
# OSXDocker theme
Source4:	OSXDocker.tar.bz2
# Source4-md5:	fb3a5175f55b582a7c123390ed3b5c66
# news_pl created by Maciej "maciunio" Paczesny <maciunio(at)ask-bsi.org>
Source5:	http://www.kde-look.org/content/files/6186-PNM4.tar.gz
# Source5-md5:	ba311930d90daf6b4c591d25d837a9b8
Source6:	6186-PNM3-themefile
# TubeClock theme
Source7:	TubeClock.tar.bz2
# Source7-md5:	ced8e1f6772bc0ed224971d3bbd9ec4e
Patch0:		%{name}-src-configfix.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-gcc34.patch
URL:		http://netdragon.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	libxml2-progs
BuildRequires:	%{__perl}
BuildRequires:	python-devel >= 2.2
BuildRequires:	xmms-devel
Requires:	perl-libwww
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
SuperKaramba is a tool that allows anyone to easily create and run
little interactive widgets on a KDE desktop.

%description -l pl
SuperKaramba to narzêdzie pozwalaj±ce na ³atwe tworzenie i
uruchamianie ma³ych interaktywnych widgetów na pulpicie KDE.

%package scripts
Summary:	Scripts for superkaramba
Summary(pl):	Skrypty dla widgetu superkaramba
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description scripts
Scripts for superkaramba.

%description scripts -l pl
Skrypty dla widgetu superkaramba.

%package theme-OSXDocker
Summary:	OSXDocker theme for %{name}
Summary(pl):	Motyw OSXDocker dla widgetu %{name}
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-scripts = %{version}-%{release}
Obsoletes:	superkaramba-themes-OSXDocker

%description theme-OSXDocker
OSXDocker theme for %{name}.

%description theme-OSXDocker -l pl
Motyw OSXDocker dla widgetu %{name}.

%package theme-szPieG
Summary:	szPieG theme for %{name}
Summary(pl):	Motyw szPieG dla widgetu %{name}
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-scripts = %{version}-%{release}
Obsoletes:	superkaramba-themes-szPieG

%description theme-szPieG
szPieG theme for %{name}.

%description theme-szPieG -l pl
Motyw szPieG dla widgetu %{name}.

%package theme-tuxbar
Summary:	tuxbar theme for %{name}
Summary(pl):	Motyw tuxbar dla widgetu %{name}
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-scripts = %{version}-%{release}
Obsoletes:	superkaramba-themes-tuxbar

%description theme-tuxbar
tuxbar theme for %{name}.

%description theme-tuxbar -l pl
Motyw tuxbar dla widgetu %{name}.

%package theme-PNM4
Summary:	Polish News Module 4 theme for %{name}
Summary(pl):	Motyw Polish News Module 4 dla widgetu %{name}
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-scripts = %{version}-%{release}
Obsoletes:	superkaramba-themes-PNM4

%description theme-PNM4
Polish News Module 4 theme for %{name}.

%description theme-PNM4 -l pl
Motyw Polish News Module 4 dla widgetu %{name}.

%package theme-TubeClock
Summary:	TubeClock theme for %{name}
Summary(pl):	Motyw zegara lampowego dla widgetu %{name}
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-scripts = %{version}-%{release}

%description theme-TubeClock
Tube clock theme for %{name}.

%description theme-TubeClock -l pl
Motyw zegara lampowego dla widgetu %{name}.

%prep
%setup -q -a1 -a2 -a3 -a4 -a5 -a7
%patch0 -p1
%patch1 -p1
%patch2 -p1

#%{__perl} -pi -e "s@/home/maciunio/karamba/DynBar/script@%{_datadir}/themes/news_pl/script@" \
#		news_pl.theme/*.theme
%{__perl} -pi -e "s@/home/genneth/files/Aqua@%{_pixmapsdir}/crystalsvg@" \
		OSXDocker/Conf.py

%{__perl} -pi -e 's@(python_libdirs=).*@$1"%{_libdir} /usr/share"@' configure

%build
cp %{_datadir}/automake/config.sub admin
kde_htmldir="%{_htmldir}"; export kde_htmldir

moc src/karamba.h -o src/karamba.moc
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
#%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/OSXDocker/Icons \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/szPieG/{Pics,script} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/tuxbar/pics \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/pics \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/01_www.linuxnews.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/02_www.7thguard.net \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/03_www.kde.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/04_www.jabberpl.org \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/05_www.mozillapl.org \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/06_www.openoffice.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/07_www.linux.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/08_www.linuxfan.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/09_www.rwo.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/10_www.idg.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/11_linuxweb.linuxindex.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/12_www.rp.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/13_www.gazeta.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/14_www.wp.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/15_www.foto.magicshop.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/16_media.netpr.pl \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/17_www.medialink.pl

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/lo16-app-karamba.png $RPM_BUILD_ROOT%{_pixmapsdir}
install src/lo32-app-karamba.png $RPM_BUILD_ROOT%{_pixmapsdir}

# Scripts

install scripts/* $RPM_BUILD_ROOT%{_bindir}

# Themes
#install news_pl.theme/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/news_pl
#install news_pl.theme/Pics/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/news_pl/Pics
#install news_pl.theme/Pics/ikony/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/news_pl/Pics/ikony
#install news_pl.theme/script/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/news_pl/script

install OSXDocker/OSXDocker.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/OSXDocker
install OSXDocker/Conf* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/OSXDocker
install OSXDocker/Icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/OSXDocker/Icons
install OSXDocker/Buttons.txt $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/OSXDocker

install szPieG/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/szPieG
install szPieG/Pics/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/szPieG/Pics
install szPieG/script/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/szPieG/script

install tuxbar/tuxbar.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/tuxbar
install tuxbar/pics/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/tuxbar/pics

install PNM4/pics/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/pics
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/PNM4.theme
install PNM4/PNM4.py $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4
install PNM4/install $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4
#install PNM4/news/01_www.linuxnews.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/01_www.linuxnews.pl
#install PNM4/news/02_www.7thguard.net/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/02_www.7thguard.net
#install PNM4/news/03_www.kde.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/03_www.kde.pl
#install PNM4/news/04_www.jabberpl.org/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/04_www.jabberpl.org
#install PNM4/news/05_www.mozillapl.org/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/05_www.mozillapl.org
#install PNM4/news/06_www.openoffice.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/06_www.openoffice.pl
#install PNM4/news/07_www.linux.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/07_www.linux.pl
#install PNM4/news/08_www.linuxfan.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/08_www.linuxfan.pl
#install PNM4/news/09_www.rwo.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/09_www.rwo.pl
#install PNM4/news/10_www.idg.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/10_www.idg.pl
#install PNM4/news/11_linuxweb.linuxindex.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/11_linuxweb.linuxindex.pl
#install PNM4/news/12_www.rp.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/12_www.rp.pl
#install PNM4/news/13_www.gazeta.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/13_www.gazeta.pl
#install PNM4/news/14_www.wp.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/14_www.wp.pl
#install PNM4/news/15_www.foto.magicshop.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/15_www.foto.magicshop.pl
#install PNM4/news/16_media.netpr.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/16_media.netpr.pl
#install PNM4/news/17_www.medialink.pl/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/17_www.medialink.pl
cp -r PNM4/news/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/
#touch $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM4/news/*/newstemp

# TubeClock
cp -Rf TubeClock $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_htmldir}/en/karamba
%attr(755,root,root) %{_bindir}/superkaramba
%{_desktopdir}/*.desktop
%{_pixmapsdir}/lo16-app-karamba.png
%{_pixmapsdir}/lo32-app-karamba.png
%dir %{_datadir}/apps/superkaramba
%{_datadir}/apps/superkaramba/karambaui.rc
%dir %{_datadir}/themes/superkaramba

%files scripts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/addSite.pl
%attr(755,root,root) %{_bindir}/cal.pl
%attr(755,root,root) %{_bindir}/free.pl
%attr(755,root,root) %{_bindir}/k_weather.py
%attr(755,root,root) %{_bindir}/local_mail.pl
%attr(755,root,root) %{_bindir}/mails.pl
%attr(755,root,root) %{_bindir}/meteocosult.pl
%attr(755,root,root) %{_bindir}/pageChange.pl
%attr(755,root,root) %{_bindir}/rdf_old.pl
%attr(755,root,root) %{_bindir}/rdf.pl
%attr(755,root,root) %{_bindir}/tv4weather.pl
%attr(755,root,root) %{_bindir}/wcam

%files theme-OSXDocker
%defattr(644,root,root,755)
%dir %{_datadir}/themes/superkaramba/OSXDocker
%dir %{_datadir}/themes/superkaramba/OSXDocker/Icons
%{_datadir}/themes/superkaramba/OSXDocker/*.*
%{_datadir}/themes/superkaramba/OSXDocker/Icons/*.png

%files theme-szPieG
%defattr(644,root,root,755)
%dir %{_datadir}/themes/superkaramba/szPieG
%dir %{_datadir}/themes/superkaramba/szPieG/Pics
%dir %{_datadir}/themes/superkaramba/szPieG/script
%{_datadir}/themes/superkaramba/szPieG/*.*
%{_datadir}/themes/superkaramba/szPieG/Pics/*.*
%attr(755,root,root) %{_datadir}/themes/superkaramba/szPieG/script/*

%files theme-tuxbar
%defattr(644,root,root,755)
%dir %{_datadir}/themes/superkaramba/tuxbar
%dir %{_datadir}/themes/superkaramba/tuxbar/pics
%{_datadir}/themes/superkaramba/tuxbar/tuxbar.*
%{_datadir}/themes/superkaramba/tuxbar/pics/*.png

%files theme-PNM4
%defattr(644,root,root,755)
%doc PNM4/{CHANGELOG,INSTALL,README}
%dir %{_datadir}/themes/superkaramba/PNM4
%dir %{_datadir}/themes/superkaramba/PNM4/pics
%dir %{_datadir}/themes/superkaramba/PNM4/news
%dir %{_datadir}/themes/superkaramba/PNM4/news/*
#%dir %{_datadir}/themes/superkaramba/PNM4/news/01_www.linuxnews.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/02_www.7thguard.net
#%dir %{_datadir}/themes/superkaramba/PNM4/news/03_www.kde.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/04_www.jabberpl.org
#%dir %{_datadir}/themes/superkaramba/PNM4/news/05_www.mozillapl.org
#%dir %{_datadir}/themes/superkaramba/PNM4/news/06_www.openoffice.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/07_www.linux.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/08_www.linuxfan.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/09_www.rwo.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/10_www.idg.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/11_linuxweb.linuxindex.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/12_www.rp.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/13_www.gazeta.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/14_www.wp.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/15_www.foto.magicshop.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/16_media.netpr.pl
#%dir %{_datadir}/themes/superkaramba/PNM4/news/17_www.medialink.pl
%{_datadir}/themes/superkaramba/PNM4/PNM4.*
%attr(755,root,root) %{_datadir}/themes/superkaramba/PNM4/install
#%attr(755,root,root) %{_datadir}/themes/superkaramba/PNM4/news/*/newstemp
%attr(755,root,root) %{_datadir}/themes/superkaramba/PNM4/news/*/getNews
%attr(755,root,root) %{_datadir}/themes/superkaramba/PNM4/news/*/loader
%{_datadir}/themes/superkaramba/PNM4/news/*/*.png
%{_datadir}/themes/superkaramba/PNM4/pics/*.png

%files theme-TubeClock
%defattr(644,root,root,755)
%dir %{_datadir}/themes/superkaramba/TubeClock
%dir %{_datadir}/themes/superkaramba/TubeClock/icons
%dir %{_datadir}/themes/superkaramba/TubeClock/pics
%dir %{_datadir}/themes/superkaramba/TubeClock/sounds
%{_datadir}/themes/superkaramba/TubeClock/TubeClock.*
%{_datadir}/themes/superkaramba/TubeClock/icons/*.png
%{_datadir}/themes/superkaramba/TubeClock/pics/*.png
%{_datadir}/themes/superkaramba/TubeClock/sounds/*.wav
