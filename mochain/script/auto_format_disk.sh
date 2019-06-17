#!/bin/sh
# Auto format and mount first disk on /data

disk_tow=`cat /proc/partitions | grep ".*da$" | awk '{print $4}' | cut -c 1`db
# aliyun ECS disk is vda..vdb……
if [ -e "/dev/${disk_tow}" ]; then
fdisk /dev/${disk_tow} << EOF
n
p
1


wq
EOF

# format
mkfs.ext4 /dev/${disk_tow}1

# mount to /data
mkdir /data
mount /dev/${disk_tow}1 /data

# auto mount disk onboot
echo "/dev/${disk_tow}1	/data	ext4	defaults	0 0" >> /etc/fstab
fi

# chang sshd port
sed -i '18i\Port 7221' /etc/ssh/sshd_config
firewall-cmd --zone=public --add-port=7221/tcp --permanent
firewall-cmd --reload
systemctl restart sshd
