#
# TODO:
# summary, desc, cleanups,
#
Summary:	superkaramba
Summary(pl):	superkaramba
Name:		superkaramba
Version:	0.24
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/netdragon/%{name}-%{version}.tar.gz
URL:		http://netdragon.sourceforge.net/
BuildRequires:	kdelibs-devel > 3.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	libxml2-progs
BuildRequires:	python-devel > 2.2
BuildRequires:	python-libs > 2.2
BuildRequires:	python-modules > 2.2
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SuperKaramba is a tool that allows anyone to easily create and run
little interactive widgets on a KDE desktop.

%description -l pl
SuperKaramba to narzêdzie które pozwala na³atwe tworzenie i
uruchamianie ma³ych interaktywnych wigetów na pulpicie KDE.

%prep
%setup -q 

%build
cd src
moc karamba.h > karamba.moc
cd ..
#rm -f missing
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
make -f Makefile.cvs
LDFLAGS="-lpython2.2"; export LDFLAGS
%configure2_13 \
	--with-pythondir=/usr/lib/python2.2 \
	--with-extra-includes=/usr/include/python2.2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install src/karamba.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/*.desktop
