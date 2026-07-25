%define upstream_name    Dist-Zilla-Plugin-GitObtain
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Obtain files from a git repository before building a distribution
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Dist-Zilla-Plugin-GitObtain
Source0:	https://cpan.metacpan.org/authors/id/D/DU/DUFF/Dist-Zilla-Plugin-GitObtain-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Role::BeforeBuild)
BuildRequires:	perl(Dist::Zilla::Role::Plugin)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Git::Wrapper)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

