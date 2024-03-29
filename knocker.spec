Summary:	Simple port scanner
Summary(pl.UTF-8):	Prosty skaner portów
Name:		knocker
Version:	0.7.1
Release:	3
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/knocker/%{name}-%{version}.tar.gz
# Source0-md5:	53d1a036071ceccb6500c0292feafacd
Source1:	%{name}.1.pl
URL:		http://knocker.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Knocker is a simple, versatile, and easy-to-use TCP security port
scanner written in C

%description -l pl.UTF-8
Knocker jest prostym, uniwersalnym i łatwym w użyciu skanerem portów.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/knocker.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%doc AUTHORS BUGS ChangeLog NEWS README TO-DO
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
