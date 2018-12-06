# http://github.com/hashicorp/go-sockaddr

%global goipath         github.com/hashicorp/go-sockaddr
%global commit          af174a6fe6c9f9a049a638e1dae7bc4442c4d426


%gometa -i

Name:           golang-github-hashicorp-go-sockaddr
Version:        0
Release:        0.7%{?dist}
Summary:        IP Address/UNIX Socket convenience functions for Go
# Detected licences
# - *No copyright* MPL (v2.0) at 'LICENSE'
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/hashicorp/errwrap)
#BuildRequires: golang(github.com/mitchellh/cli)
BuildRequires: golang-github-mitchellh-cli-devel-temporary
BuildRequires: golang(github.com/mitchellh/go-wordwrap)
BuildRequires: golang(github.com/ryanuber/columnize)

#Requires:      golang(github.com/mitchellh/cli)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
# Depends on hasicorp/consul -> cyclic deps
#%%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.7.gitaf174a6
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.20161202gitaf174a6
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitaf174a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitaf174a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitaf174a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.2.gitaf174a6
- Remove cyclic dep
  related: #1410393

* Thu Jan 05 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.gitaf174a6
- First package for Fedora
  resolves: #1410393
