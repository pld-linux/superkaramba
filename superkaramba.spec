#
# TODO:
# summary, desc, cleanups,
#
Summary:	superkaramba
Summary(pl):	superkaramba
Name:		superkaramba
Version:	0.22b
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/netdragon/superkaramba-0.22b.tar.gz
URL:		http://karamba.sourceforge.net/
BuildRequires:	qt-devel > 3.0
BuildRequires:	kdelibs-devel > 3.0
BuildRequires:	python-devel > 2.2
BuildRequires:	python-libs > 2.2
BuildRequires:	python-modules > 2.2
BuildRequires:	libart_lgpl-devel
BuildRequires:	xmms-devel
BuildRequires:	libxml2-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q 

%build
cd src
moc karamba.h > karamba.moc
cd ..
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure2_13 \
	--with-pythondir=/usr/lib/python2.2 \
	--with-extra-includes=/usr/include/python2.2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
