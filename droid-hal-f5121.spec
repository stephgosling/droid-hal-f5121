%define device suzu
%define vendor sony

%define rpm_device f5121
%define rpm_vendor qualcomm

%define vendor_pretty Sony
%define device_pretty Xperia X

%define have_custom_img_boot 1
%define have_custom_img_recovery 1

%define droid_target_aarch64 1

%define device_variant -userdebug
%define lunch_prefix aosp_

%define makefstab_skip_entries /system none /sys/fs/pstore

%define straggler_files\
    /selinux_version\
    /service_contexts\
%{nil}

Requires: droid-system

%include rpm/dhd/droid-hal-device.inc

