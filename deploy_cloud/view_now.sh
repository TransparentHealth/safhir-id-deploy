#!/usr/bin/env bash
cd ./deploy_cloud
ansible-playbook -i ./etc/ansible/hosts  ./deploy_target_group.yml --vault-id ~/ansibled.vault --extra-vars "cloud_provider=aws cloud_client=afbh vpc_env=prod vpc_base_region=us-east vpc_number=1 aws_region=us-east-1"  -v
echo "Now go to AWS Console in US-EAST-1 (N.Virginia)"
echo "Add new servers to PROD-WEB target group"
echo "Remove old servers from PROD-WEB Target Group and terminate"
