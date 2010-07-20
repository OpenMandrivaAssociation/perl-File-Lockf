%define upstream_name    File-Lockf
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary: 	%{upstream_name} module for perl
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0: 	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
File-Lockf module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
