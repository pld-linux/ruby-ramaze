Summary:	Ramaze - Web framework
Name:		ruby-ramaze
Version:	2010.04
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	ramaze-20100612.tar.gz
# Source0-md5:	3c4f204649b91f2db3243cb5df4f243c
URL:		http://ramaze.net/
BuildRequires:	ruby-rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.4.1
Requires:	ruby-builder
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ramaze is web framework for Ruby.

%prep
%setup -q -n ramaze
cp %{_datadir}/setup.rb .

%build
#mv ramaze.rb lib

ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%attr(755,root,root) %{_bindir}/ramaze
%{ruby_rubylibdir}/ramaze*
%{ruby_rubylibdir}/vendor*
%{ruby_rubylibdir}/proto
