Summary:	Simple port scanner
Summary(pl):	Prosty skaner portów
Name:		knocker
Version:	0.7.1
Release:	2
License:	GPL
Group:		Networking/Utilities
URL:		http://knocker.sourceforge.net/
Source0:	http://dl.sourceforge.net/sourceforge/knocker/%{name}-%{version}.tar.gz
# Source0-md5:	53d1a036071ceccb6500c0292feafacd
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Knocker is a simple, versatile, and easy-to-use TCP security port
scanner written in C

%description -l pl
Knocker jest prostym, uniwersalnym i ³atwym w u¿yciu skanerem portów.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knocker
%doc ChangeLog AUTHORS BUGS TO-DO NEWS README
%{_mandir}/man1/*
