%define module  File-Lockf
%define version 0.20
%define release %mkrel 9

Summary: 	%{module} module for perl
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source0: 	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
Requires: 	perl perl-base 
BuildRequires:	perl-devel

%description
File-Lockf module for perl

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(444,root,root,755)
%doc COPYRIGHT README
%dir %{perl_vendorlib}/*/File
%{perl_vendorlib}/*/File/lockf.pm
%dir %{perl_vendorlib}/*/auto/File
%dir %{perl_vendorlib}/*/auto/File/lockf
%{perl_vendorlib}/*/auto/File/lockf/lockf.so
%{_mandir}/*/*

