Summary:	Ramaze - Web framework
Name:		ruby-ramaze
Version:	2010.06.18
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/ramaze-%{version}.gem
# Source0-md5:	751c0884322ae932c525e7938da138b5
URL:		http://ramaze.net/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-rake
BuildRequires:	setup.rb >= 3.4.1
Requires:	ruby-builder
Requires:	ruby-innate
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ramaze is web framework for Ruby.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.md -o -print | xargs touch --reference %{SOURCE0}
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
