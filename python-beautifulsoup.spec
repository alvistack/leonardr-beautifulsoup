%global debug_package %{nil}

Name: python-beautifulsoup
Epoch: 100
Version: 4.11.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Screen-scraping library
License: MIT
URL: https://pypi.org/project/beautifulsoup4/#history
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Beautiful Soup is a library that makes it easy to scrape information
from web pages. It sits atop an HTML or XML parser, providing Pythonic
idioms for iterating, searching, and modifying the parse tree.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-beautifulsoup4
Summary: Screen-scraping library
Requires: python3
Requires: python3-soupsieve > 1.2
Provides: python3-beautifulsoup4 = %{epoch}:%{version}-%{release}
Provides: python3dist(beautifulsoup4) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-beautifulsoup4 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(beautifulsoup4) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-beautifulsoup4 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(beautifulsoup4) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-beautifulsoup4
Beautiful Soup is a library that makes it easy to scrape information
from web pages. It sits atop an HTML or XML parser, providing Pythonic
idioms for iterating, searching, and modifying the parse tree.

%files -n python%{python3_version_nodots}-beautifulsoup4
%license COPYING.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-beautifulsoup4
Summary: Screen-scraping library
Requires: python3
Requires: python3-soupsieve > 1.2
Provides: python3-beautifulsoup4 = %{epoch}:%{version}-%{release}
Provides: python3dist(beautifulsoup4) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-beautifulsoup4 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(beautifulsoup4) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-beautifulsoup4 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(beautifulsoup4) = %{epoch}:%{version}-%{release}

%description -n python3-beautifulsoup4
Beautiful Soup is a library that makes it easy to scrape information
from web pages. It sits atop an HTML or XML parser, providing Pythonic
idioms for iterating, searching, and modifying the parse tree.

%files -n python3-beautifulsoup4
%license COPYING.txt
%{python3_sitelib}/*
%endif

%changelog
