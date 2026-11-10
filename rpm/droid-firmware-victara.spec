Name:       droid-firmware-victara
Version:    1
Release:    1
Summary:    Firmware for Motorola Moto X 2014 (victara)
License:    Proprietary and LicenseRef-LICENSE.qcom
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2

%description
Wi-Fi NV calibration and Adreno 330 microcode for victara, plus early mount of
the modem firmware partition so remoteproc blobs load from /firmware/image.

%prep
%autosetup -n %{name}-%{version}

%build

%install
install -Dm644 firmware/wlan/prima/WCNSS_qcom_wlan_nv.bin %{buildroot}/lib/firmware/wlan/prima/WCNSS_qcom_wlan_nv.bin
install -Dm644 firmware/qcom/a330_pm4.fw %{buildroot}/lib/firmware/qcom/a330_pm4.fw
install -Dm644 firmware/qcom/a330_pfp.fw %{buildroot}/lib/firmware/qcom/a330_pfp.fw

install -Dm755 sparse/usr/bin/victara-firmware-mount %{buildroot}/usr/bin/victara-firmware-mount
install -Dm644 sparse/usr/lib/systemd/system/victara-firmware.service %{buildroot}/usr/lib/systemd/system/victara-firmware.service

mkdir -p %{buildroot}/usr/lib/systemd/system/sysinit.target.wants
ln -s ../victara-firmware.service %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/victara-firmware.service

mkdir -p %{buildroot}/firmware

%files
%license LICENSE.qcom NOTICE.qcom
/lib/firmware/wlan/prima/WCNSS_qcom_wlan_nv.bin
/lib/firmware/qcom/a330_pm4.fw
/lib/firmware/qcom/a330_pfp.fw
/usr/bin/victara-firmware-mount
/usr/lib/systemd/system/victara-firmware.service
/usr/lib/systemd/system/sysinit.target.wants/victara-firmware.service
%dir /firmware
