Summary:	superkaramba - little interactive widgets on KDE desktop
Summary(pl):	superkaramba - ma³e interaktywne widgety na pulpicie KDE
Name:		superkaramba
Version:	0.26
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/netdragon/%{name}-%{version}.tar.gz
# Source0-md5:	68bf76ad1f0e5baee6e98c9611defb74
# Scripts widely used by superkaramba theme creators
Source1:	http://www.efd.lth.se/~d98hk/karamba/scripts/scripts.tar.gz
# Source1-md5:	94f0620854df678c4e7908679f139a78
#
#
# Here go modules, aka themes.
#
# szPieG theme
# http://szpieg.gda.pl/  - made by Marcin Ciunelis <martin@ds.pg.gda.pl>
Source2:	szPieG-%{name}-0.1.tar.gz
# Source2-md5:	2336bd718ccf5deb06204e97248eeae0
# tuxbar-pzoom theme
Source3:	tuxbar-pzoom-0.17g.tar.gz
# Source3-md5:	04089c070215693833f2c5da7d8af8d2
# OSXDocker theme
Source4:	OSXDocker.tar.bz2
# Source4-md5:	fb3a5175f55b582a7c123390ed3b5c66
# news_pl created by Maciej "maciunio" Paczesny <maciunio(at)ask-bsi.org>
Source5:	http://www.kdelook.org/content/files/6186-PNM3.tar.gz
# Source5-md5:	755d56e6173e7d88d1ca61fb5d2a14fb
Patch0:		%{name}-themes-PNM3-theme.patch


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
SuperKaramba to narzêdzie pozwalaj±ce na ³atwe tworzenie i
uruchamianie ma³ych interaktywnych widgetów na pulpicie KDE.

%package scripts
Summary:        Scripts for %{name}
Summary(pl):    Skrypty dla widgetu %{name}
Group:          X11/Applications
Requires:       %{name}

%description scripts
Scripts for %{name}.

%description scripts -l pl
Skrypty dla widgetu {%name}.


%package themes
Summary:	Themes for %{name}
Summary(pl):	Motywy dla widgetu %{name}
Group:		X11/Applications
Requires:	%{name}
Requires:	%{name}-scripts
Obsoletes: 	%{name}-themes-OSXDocker
Obsoletes: 	%{name}-themes-szPieG
Obsoletes: 	%{name}-themes-tuxbar
Obsoletes: 	%{name}-themes-PNM3

%description themes
Themes for %{name}.

%description themes -l pl
Motywy dla widgetu %{name}.

OSXDocker
%package themes-OSXDocker
Summary:        OSXDocker theme for %{name}
Summary(pl):    Motyw OSXDocker dla widgetu %{name}
Group:          X11/Applications
Requires:       %{name}
Requires:       %{name}-scripts
Obsoletes:      %{name}-themes

%description themes-OSXDocker
OSXDocker theme for %{name}.

%description themes-OSXDocker -l pl
Motyw OSXDocker dla widgetu %{name}.

%package themes-szPieG
Summary:        szPieG theme for %{name}
Summary(pl):    Motyw szPieG dla widgetu %{name}
Group:          X11/Applications
Requires:       %{name}
Requires:       %{name}-scripts
Obsoletes:      %{name}-themes

%description themes-szPieG
szPieG theme for %{name}.

%description themes-szPieG -l pl
Motyw szPieG dla widgetu %{name}.

%package themes-tuxbar
Summary:        tuxbar theme for %{name}
Summary(pl):    Motyw tuxbar dla widgetu %{name}
Group:          X11/Applications
Requires:       %{name}
Requires:       %{name}-scripts
Obsoletes:      %{name}-themes

%description themes-tuxbar
tuxbar theme for %{name}.

%description themes-tuxbar -l pl
Motyw tuxbar dla widgetu %{name}.

%package themes-PNM3
Summary:        Polish News Module 3 theme for %{name}
Summary(pl):    Motyw Polish News Module 3 dla widgetu %{name}
Group:          X11/Applications
Requires:       %{name}
Requires:       %{name}-scripts
Obsoletes:      %{name}-themes

%description themes-PNM3
Polish News Module 3 theme for %{name}.

%description themes-tuxbar -l pl
Motyw Polish News Module 3 dla widgetu %{name}.


%prep
%setup -q -a1 -a2 -a3 -a4 -a5
%patch0 -p1

%build
#%{__perl} -pi -e "s@/home/maciunio/karamba/DynBar/script@%{_datadir}/themes/news_pl/script@" \
#		news_pl.theme/*.theme
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
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install -d $RPM_BUILD_ROOT%{_datadir}/themes
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba

install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/OSXDocker
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/OSXDocker/Icons

install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/szPieG/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/szPieG/Pics
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/szPieG/script

install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/tuxbar
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/tuxbar/pics

install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/pics
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/01_www.linuxnews.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/02_www.7thguard.net/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/03_www.kde.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/04_www.jabberpl.org/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/05_www.mozillapl.org/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/06_www.openoffice.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/07_www.linux.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/08_www.linuxfan.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/09_www.rwo.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/10_www.idg.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/11_linuxweb.linuxindex.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/12_www.rp.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/13_www.gazeta.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/14_www.wp.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/15_www.foto.magicshop.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/16_media.netpr.pl/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/17_www.medialink.pl/



#	   $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/{OSXDocker/Icons,news_pl/{Pics/ikony,script},szPieG/{Pics,script}} \
#	   $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/tuxbar/pics
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install src/karamba.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities

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

install PNM3/pics/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/pics
install PNM3/PNM3.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3
install PNM3/PNM3.py $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3
install PNM3/install $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3
install PNM3/01_www.linuxnews.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/01_www.linuxnews.pl/
install PNM3/02_www.7thguard.net/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/02_www.7thguard.net/
install PNM3/03_www.kde.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/03_www.kde.pl/
install PNM3/04_www.jabberpl.org/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/04_www.jabberpl.org/
install PNM3/05_www.mozillapl.org/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/05_www.mozillapl.org/
install PNM3/06_www.openoffice.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/06_www.openoffice.pl/
install PNM3/07_www.linux.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/07_www.linux.pl/
install PNM3/08_www.linuxfan.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/08_www.linuxfan.pl/
install PNM3/09_www.rwo.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/09_www.rwo.pl/
install PNM3/10_www.idg.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/10_www.idg.pl/
install PNM3/11_linuxweb.linuxindex.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/11_linuxweb.linuxindex.pl/
install PNM3/12_www.rp.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/12_www.rp.pl/
install PNM3/13_www.gazeta.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/13_www.gazeta.pl/
install PNM3/14_www.wp.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/14_www.wp.pl/
install PNM3/15_www.foto.magicshop.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/15_www.foto.magicshop.pl/
install PNM3/16_media.netpr.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/16_media.netpr.pl/
install PNM3/17_www.medialink.pl/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/PNM3/news/17_www.medialink.pl/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/*.desktop

%files scripts
%defattr(644,root,root,755)
%dir %{_bindir}/
%{_bindir}/addSite.pl
%{_bindir}/cal.pl
%{_bindir}/free.pl
%{_bindir}/k_weather.py
%{_bindir}/local_mail.pl
%{_bindir}/mails.pl
%{_bindir}/meteocosult.pl
%{_bindir}/pageChange.pl
%{_bindir}/rdf_old.pl
%{_bindir}/rdf.pl
%{_bindir}/tv4weather.pl
%{_bindir}/wcam

%files themes
%dir %{_datadir}/themes/
%dir %{_datadir}/themes/superkaramba/
#%dir %{_datadir}/themes/superkaramba/news_pl
#%dir %{_datadir}/themes/superkaramba/news_pl/Pics
#%dir %{_datadir}/themes/superkaramba/news_pl/Pics/ikony
#%dir %{_datadir}/themes/superkaramba/news_pl/script
#%{_datadir}/themes/superkaramba/news_pl/*.theme
#%{_datadir}/themes/superkaramba/news_pl/Pics/*.png
#%{_datadir}/themes/superkaramba/news_pl/Pics/ikony/*
#%attr(755,root,root) %{_datadir}/themes/superkaramba/news_pl/script/*

%dir %{_datadir}/themes/superkaramba/OSXDocker
%dir %{_datadir}/themes/superkaramba/OSXDocker/Icons
%{_datadir}/themes/superkaramba/OSXDocker/*.*
%{_datadir}/themes/superkaramba/OSXDocker/Icons/*.png

%dir %{_datadir}/themes/superkaramba/szPieG
%dir %{_datadir}/themes/superkaramba/szPieG/Pics
%dir %{_datadir}/themes/superkaramba/szPieG/script
%{_datadir}/themes/superkaramba/szPieG/*.*
%{_datadir}/themes/superkaramba/szPieG/Pics/*.*
%attr(755,root,root) %{_datadir}/themes/superkaramba/szPieG/script/*

%dir %{_datadir}/themes/superkaramba/tuxbar
%dir %{_datadir}/themes/superkaramba/tuxbar/pics
%{_datadir}/themes/superkaramba/tuxbar/tuxbar.*
%{_datadir}/themes/superkaramba/tuxbar/pics/*.png

%files themes-OSXDocker
%dir %{_datadir}/themes/superkaramba/OSXDocker
%dir %{_datadir}/themes/superkaramba/OSXDocker/Icons
%{_datadir}/themes/superkaramba/OSXDocker/*.*
%{_datadir}/themes/superkaramba/OSXDocker/Icons/*.png

%files themes-szPieG
%dir %{_datadir}/themes/superkaramba/szPieG
%dir %{_datadir}/themes/superkaramba/szPieG/Pics
%dir %{_datadir}/themes/superkaramba/szPieG/script
%{_datadir}/themes/superkaramba/szPieG/*.*
%{_datadir}/themes/superkaramba/szPieG/Pics/*.*
%attr(755,root,root) %{_datadir}/themes/superkaramba/szPieG/script/*

%files themes-tuxbar
%dir %{_datadir}/themes/superkaramba/tuxbar
%dir %{_datadir}/themes/superkaramba/tuxbar/pics
%{_datadir}/themes/superkaramba/tuxbar/tuxbar.*
%{_datadir}/themes/superkaramba/tuxbar/pics/*.png

%files themes-PNM3
%dir %{_datadir}/themes/superkaramba/PNM3
%dir %{_datadir}/themes/superkaramba/PNM3/pics
%dir %{_datadir}/themes/superkaramba/PNM3/news
%dir %{_datadir}/themes/superkaramba/PNM3/news/01_www.linuxnews.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/02_www.7thguard.net/
%dir %{_datadir}/themes/superkaramba/PNM3/news/03_www.kde.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/04_www.jabberpl.org/
%dir %{_datadir}/themes/superkaramba/PNM3/news/05_www.mozillapl.org/
%dir %{_datadir}/themes/superkaramba/PNM3/news/06_www.openoffice.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/07_www.linux.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/08_www.linuxfan.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/09_www.rwo.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/10_www.idg.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/11_linuxweb.linuxindex.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/12_www.rp.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/13_www.gazeta.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/14_www.wp.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/15_www.foto.magicshop.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/16_media.netpr.pl/
%dir %{_datadir}/themes/superkaramba/PNM3/news/17_www.medialink.pl/

%{_datadir}/themes/superkaramba/PNM3/PNM3.*
%{_datadir}/themes/superkaramba/PNM3/pics/*
%{_datadir}/themes/superkaramba/PNM3/news/01_www.linuxnews.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/02_www.7thguard.net/*.*
%{_datadir}/themes/superkaramba/PNM3/news/03_www.kde.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/04_www.jabberpl.org/*.*
%{_datadir}/themes/superkaramba/PNM3/news/05_www.mozillapl.org/*.*
%{_datadir}/themes/superkaramba/PNM3/news/06_www.openoffice.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/07_www.linux.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/08_www.linuxfan.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/09_www.rwo.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/10_www.idg.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/11_linuxweb.linuxindex.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/12_www.rp.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/13_www.gazeta.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/14_www.wp.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/15_www.foto.magicshop.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/16_media.netpr.pl/*.*
%{_datadir}/themes/superkaramba/PNM3/news/17_www.medialink.pl/*.*

%doc CHANGELOG COPYRIGHT INSTALL LICENSE PLUGIN_README README TODO
