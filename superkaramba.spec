# TODO:
# - separate themes into subpackages
Summary:	superkaramba - little interactive widgets on KDE desktop
Summary(pl):	superkaramba - ma³e interaktywne widgety na pulpicie KDE
Name:		superkaramba
Version:	0.25
Release:	0.4
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/netdragon/%{name}-%{version}.tar.gz
# news_pl created by Maciej "maciunio" Paczesny <maciunio(at)ask-bsi.org>
Source1:	news_pl.theme.tar.gz
Source2:	OSXDocker.tar.bz2
# http://szpieg.gda.pl/  - made by Marcin Ciunelis <martin@ds.pg.gda.pl>
Source3:	szPieG-%{name}-0.1.tar.gz
URL:		http://netdragon.sourceforge.net/
BuildRequires:	kdelibs-devel > 3.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	libart_lgpl-static
BuildRequires:	libxml2-progs
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

%prep
%setup -q -a1 -a2 -a3

%build

perl -pi -e "s/\/home\/maciunio\/karamba\/DynBar\/script/\/usr\/share\/themes\/news_pl\/script/" \
		news_pl.theme/*.theme
perl -pi -e "s/\/home\/genneth\/files\/Aqua/\/usr\/share\/pixmaps\/crystalsvg/" \
		OSXDocker/Conf.py

cd src
moc karamba.h > karamba.moc
cd ..
#rm -f missing
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
%{__make} -f Makefile.cvs
LDFLAGS="-lpython2.2"; export LDFLAGS


%configure2_13 \
	--with-pythondir=/usr/lib/python2.2 \
	--with-extra-includes=/usr/include/python2.2
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities \
	   $RPM_BUILD_ROOT%{_datadir}/themes/{OSXDocker/Icons,news_pl/{Pics/ikony,script},szPieG/{Pics,script}} 

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/*.desktop
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
%attr(755,root,root) %{_datadir}/themes/szPieG/*
