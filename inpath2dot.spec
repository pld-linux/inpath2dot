%include	/usr/lib/rpm/macros.perl
Summary:	Parses inpath-data to a format usuable by graphviz
Name:		inpath2dot
Version:	1.3
Release:	1
License:	GPL v2+
Group:		Networking/Daemons
Source0:	http://cord.de/tools/news/%{name}.pl
# Source0-md5:	cc81944660fcaf1d72447358ab7bfa71
URL:		http://cord.de/tools/news/
BuildRequires:	rpm-perlprov
Requires:	graphviz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -Tc -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
