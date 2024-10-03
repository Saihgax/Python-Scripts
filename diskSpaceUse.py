'''
Write a function to analyze disk space usage on a server. 
Given a list of dictionaries with each dictionary containing filesystem, size, used, and available, 
calculate the total disk space used and the percentage used per filesystem.

'''


def disk_space_usage(filesystems):
    total_used = sum(fs['used'] for fs in filesystems)
    disk_stats = []

    for fs in filesystems:
        used_percentage = (fs["used"]/fs["size"])*100
        disk_stats.append({
            'filesystem': fs["filesystem"],
            'used_percentage': used_percentage
        })

    return total_used, disk_stats


filesystems = [
    {"filesystem": "/dev/sda1", "size": 100, "used": 50, "available": 50},
    {"filesystem": "/dev/sda2", "size": 200, "used": 100, "available": 100},
    {"filesystem": "/dev/sda3", "size": 300, "used": 150, "available": 150}
]

total_used, disk_stats = disk_space_usage(filesystems)
print(f"Total Disk Space Used: {total_used} GB", "\n")
print(f"Disk Stats: {disk_stats}")