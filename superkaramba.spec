Summary:	superkaramba - little interactive widgets on KDE desktop
Summary(pl):	superkaramba - ma³e interaktywne widgety na pulpicie KDE
Name:		superkaramba
Version:	0.25
Release:	0.3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/netdragon/%{name}-%{version}.tar.gz
# news_pl created by Maciej "maciunio" Paczesny <maciunio(at)ask-bsi.org>
Source1:	news_pl.theme.tar.gz
Source2:	OSXDocker.tar.bz2
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
%setup -q -a1 -a2

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
	   $RPM_BUILD_ROOT%{_datadir}/themes/{OSXDocker/Icons,news_pl/{Pics/ikony,script}} 

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/*.desktop
%{_datadir}/themes/news_pl/*.theme
%{_datadir}/themes/news_pl/Pics/*.png
%{_datadir}/themes/news_pl/Pics/ikony/*
%attr(755,root,root) %{_datadir}/themes/news_pl/script/*

%{_datadir}/themes/OSXDocker/*.*
%{_datadir}/themes/OSXDocker/Icons/*.png
