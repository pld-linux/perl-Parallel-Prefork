#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Parallel
%define		pnam	Prefork
%include	/usr/lib/rpm/macros.perl
Summary:	Parallel::Prefork - A simple prefork server framework
Name:		perl-Parallel-Prefork
Version:	0.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Parallel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	128f8c03eddde44d3e95f092d6116e9a
URL:		http://search.cpan.org/dist/Parallel-Prefork/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::Accessor::Lite) >= 0.04
BuildRequires:	perl(Proc::Wait3) >= 0.03
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Test-Requires
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parallel::Prefork is much like Parallel::ForkManager, but supports
graceful shutdown and run-time reconfiguration.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Parallel/*.pm
%{perl_vendorlib}/Parallel/Prefork
%{_mandir}/man3/*
