Name:		slab-geoexplorer
Version:	3.0
Release:	1%{?dist}
Summary:	This is a packaged of the GeoExplorer WAR file for use on SLab/UVa infrastructure.

Group:		GIS
License:	GPL
URL:		https://github.com/opengeo/suit://github.com/opengeo/GeoExplorer	
Source0:	%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXXXX)

Requires:	tomcat6

%description
This is a packaged of the GeoExplorer WAR file for use on SLab/UVa infrastructure.

%prep
%setup -q


%build


%install
install -m 0755 -d $RPM_BUILD_ROOT/var/lib/tomcat6/webapps
install -m 0755 geoexplorer.war $RPM_BUILD_ROOT/var/lib/tomcat6/webapps/geoexplorer.war

%post
echo "Restarting Tomcat."
service tomcat6 restart

%postun
echo "Cleaning up webapp directory."
rm -rf /var/lib/tomcat6/webapps/geoexplorer
echo "Restarting Tomcat."
service tomcat6 restart


%clean
[ \$RPM_BUILD_ROOT != '/' ] && rm -rf \$RPM_BUILD_ROOT


%files
/var/lib/tomcat6/webapps/geoexplorer.war


%changelog

