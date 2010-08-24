%define upstream_name    Dist-Zilla-Plugin-GitObtain
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Obtain files from a git repository before building a distribution
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla::Role::BeforeBuild)
BuildRequires: perl(Dist::Zilla::Role::Plugin)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(Git::Wrapper)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module uses the Git::Wrapper manpage to obtain files from git
repositories before building a distribution.

You may specify the directory that git repositories will be placed into by
following the plugin name ('GitObtain') with a forward slash ('/'), then
the path to the particular directory. For instance, if your _dist.ini_ file
contained the following section:

  [GitObtain/alpha/beta/gamma]
    ...

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


