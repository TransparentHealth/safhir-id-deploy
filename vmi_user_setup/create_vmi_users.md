# SAFHIR - VMI 
## Process to add CPCDS Patients file to VMI
    create_vmi_users.md 
    Author: @ekivemark
    Created: 2019-12-04.00:42

    safhir-id-deploy/vmi_user_setup/create_vmi_users.md


### Preparatory Environment setup 

```
# ssh to Azure SAFHIR Management Controller
ssh -I ~/.ssh/safhir-id-dev ubuntu@104.41.129.89

# If updates need to be applied:
sudo apt-get =y update
sudo apt-get =y upgrade

# Switch to deployment directory
deploy
cd /opt/django-projects/vmi
# activate virtual environment
source env/bin/activate
Source .env

# ROLE_TYPE should now be set to “vmi”
# VARIABLE_HOST should now be set to “10.1.0.4”
# All variables needed by vmi should now be set


```
### Run Management command

This command will fail if a user account is already present.
If replacing accounts do the following first:

	- Login in to vmi admin console (https://id-dev.safhir.io)
	- Delete Individual Identifiers for members
	- Delete User records for members to be replaced

```
python manage.py create_sample_vmi_users \
			-s 1001 \
			-u dmnd \
			-p du.  \ 
			-f /home/ubuntu/patients.csv  \ 
			-o /home/ubuntu/patient_list.csv 
			-i “Diamond Health” \
			-m /home/ubuntu/member_meta.csv \
			1
```

- s = start number
- u = username prefix
- p = password prefix
- f = absolute path to source file of CPCDS Patients
- o = absolute path to output file
- I = issuer/insurer name
- m = absolute path to meta output file
- number of records to create (used when creating users without a CPCDS input file

### Post Processing

Copy Meta file to API Management gateway to incorporate into Meta database.

### File formats


#### Input CSV File

This is the CPCDS Patient.csv file:

```
[‘Member id’, ‘Date of birth’, ‘Date of death’, ‘County’, ‘State’, ’Country’, ‘Zip code’, ‘Race code’, ‘Ethnicity’, ‘Gender code’, 'Name', 'Relationship to subscriber', 'Subscriber id']

```

#### Output CSV File

[“member”, “subject”, “first”, “last”, “userid”, “password”]

#### Meta CSV File

[“memberid”, “subject”]


