Summary:	superkaramba - little interactive widgets on KDE desktop
Summary(pl):	superkaramba - ma³e interaktywne widgety na pulpicie KDE
Name:		superkaramba
Version:	0.26
Release:	0.1
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
# news_pl created by Maciej "maciunio" Paczesny <maciunio(at)ask-bsi.org>
Source2:	news_pl.theme.tar.gz
# Source2-md5:	d41d8cd98f00b204e9800998ecf8427e
Source3:	OSXDocker.tar.bz2
# Source3-md5:	fb3a5175f55b582a7c123390ed3b5c66
# http://szpieg.gda.pl/  - made by Marcin Ciunelis <martin@ds.pg.gda.pl>
Source4:	szPieG-%{name}-0.1.tar.gz
# Source4-md5:	2336bd718ccf5deb06204e97248eeae0
Source5:	tuxbar-pzoom-0.17g.tar.gz
# Source5-md5:	04089c070215693833f2c5da7d8af8d2
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
Obsoletes:      %{name} < %{name}-0.4

%description scripts
Scripts for %{name}.

%description scripts -l pl
Skrypty dla widgetu {%name}.


%package themes
Summary:	Themes for %{name}
Summary(pl):	Motywy dla widgetu %{name}
Group:		X11/Applications
Requires:	%{name}
Obsoletes:	%{name} < %{name}-0.4

%description themes
Themes for %{name}.

%description themes -l pl
Motywy dla widgetu %{name}.

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
	   $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/{OSXDocker/Icons,news_pl/{Pics/ikony,script},szPieG/{Pics,script}} \
	   $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/tuxbar/pics

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install src/karamba.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities

# Scripts

install scripts/* $RPM_BUILD_ROOT%{_bindir}

# Themes
install news_pl.theme/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/news_pl
install news_pl.theme/Pics/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/news_pl/Pics
install news_pl.theme/Pics/ikony/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/news_pl/Pics/ikony
install news_pl.theme/script/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/news_pl/script

install OSXDocker/OSXDocker.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/OSXDocker
install OSXDocker/Conf* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/OSXDocker
install OSXDocker/Icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/OSXDocker/Icons
install OSXDocker/Buttons.txt $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/OSXDocker

install szPieG/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/szPieG
install szPieG/Pics/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/szPieG/Pics
install szPieG/script/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/szPieG/script

install tuxbar/tuxbar.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/tuxbar
install tuxbar/pics/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/tuxbar/pics

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
%dir %{_datadir}/themes/superkaramba/news_pl
%dir %{_datadir}/themes/superkaramba/news_pl/Pics
%dir %{_datadir}/themes/superkaramba/news_pl/Pics/ikony
%dir %{_datadir}/themes/superkaramba/news_pl/script
%{_datadir}/themes/superkaramba/news_pl/*.theme
%{_datadir}/themes/superkaramba/news_pl/Pics/*.png
%{_datadir}/themes/superkaramba/news_pl/Pics/ikony/*
%attr(755,root,root) %{_datadir}/themes/superkaramba/news_pl/script/*

%dir %{_datadir}/themes/superkaramba/OSXDocker
%dir %{_datadir}/themes/superkaramba/OSXDocker/Icons
%{_datadir}/themes/superkaramba/OSXDocker/*.*
%{_datadir}/themes/OSXDocker/Icons/*.png

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
