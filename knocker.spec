Summary:	Simple port scanner
Summary(pl):	Prosty skaner portów
Name:		knocker
Version:	0.7.1
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/knocker/%{name}-%{version}.tar.gz
# Source0-md5:	53d1a036071ceccb6500c0292feafacd
Source1:	http://www.mbsoftware.boo.pl/knocker/%{name}-polish-man-page.tar.gz
# Source1-md5:	a3ea62d930e98698885ef417ea653e8b
URL:		http://knocker.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Knocker is a simple, versatile, and easy-to-use TCP security port
scanner written in C

%description -l pl
Knocker jest prostym, uniwersalnym i ³atwym w u¿yciu skanerem portów.

%prep
%setup -q -a1

%build
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
cp -r pl/ $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%doc AUTHORS BUGS ChangeLog NEWS README TO-DO
%{_mandir}/man1/*
%{_mandir}/pl/man1/*
