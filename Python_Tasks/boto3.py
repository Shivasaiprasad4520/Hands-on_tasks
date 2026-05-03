### this script using Boto3 to list + start/stop EC2s by tag 

import boto3

# Create EC2 client
ec2 = boto3.client("ec2", region_name="ap-south-1")

# Tag filter values
TAG_KEY = "Environment"
TAG_VALUE = "Dev"


def get_instances():
    response = ec2.describe_instances(
        Filters=[
            {
                "Name": f"tag:{TAG_KEY}",
                "Values": [TAG_VALUE]
            }
        ]
    )

    instance_ids = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_ids.append(instance["InstanceId"])

    return instance_ids


def start_instances(instance_ids):
    if instance_ids:
        ec2.start_instances(InstanceIds=instance_ids)
        print("Started Instances:", instance_ids)
    else:
        print("No matching instances found.")


def stop_instances(instance_ids):
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print("Stopped Instances:", instance_ids)
    else:
        print("No matching instances found.")


def list_instances(instance_ids):
    if instance_ids:
        print("Matching EC2 Instances:")
        for i in instance_ids:
            print(i)
    else:
        print("No matching instances found.")


# Main menu
instances = get_instances()

print("1. List Instances")
print("2. Start Instances")
print("3. Stop Instances")

choice = input("Enter your choice: ")

if choice == "1":
    list_instances(instances)

elif choice == "2":
    start_instances(instances)

elif choice == "3":
    stop_instances(instances)

else:
    print("Invalid choice")
