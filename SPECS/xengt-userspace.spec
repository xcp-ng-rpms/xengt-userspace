%global package_speccommit 42d56d416826cc009dafdea7cd4884f8b80e4fdf
%define vendor_name Intel Corporation
%define driver_name xengt

Summary: %{vendor_name} %{driver_name} userspace
Name: %{driver_name}-userspace
Version: 4.0.0
Release: 1%{?xsrel}%{?dist}
Vendor: %{vendor_name}
License: GPLv2
Group: System Environment/Base
Source0: gvt-g-whitelist
Source1: i915.conf
BuildArch: noarch

%description
%{vendor_name} %{driver_name} Userspace components

%install
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}
install -m 644 %{SOURCE0} ${RPM_BUILD_ROOT}%{_sysconfdir}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/modprobe.d
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/modprobe.d/

%files
%defattr(-,root,root,-)
%{_sysconfdir}/gvt-g-whitelist
%{_sysconfdir}/modprobe.d/i915.conf

%changelog
