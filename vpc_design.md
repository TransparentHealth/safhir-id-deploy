# VPC Design

PRODUCTION: 10.10.x.x
STAGING: 10.20.x.x

## VPC Structure

                 Internet
 +------------+---------------+----------+
 |            |               |          |
 |    ALB     |     ALB       |   ALB    | DMZ
 |            |               |          |
 +------------+---------------+----------+ 
 
 +------------+---------------+----------+
 |            |               |          |
 |    EC2     |     EC2       |   EC2    | APP
 |            |               |          |
 +------------+---------------+----------+ 

 +------------+---------------+----------+
 |            |               |          |
 |    RDS     |               |   RDS    | DB
 |            |               |          |
 +------------+---------------+----------+ 

 +------------+---------------+----------+
 |            |               |          |
 |            |    MGMT       |          |
 |            |               |          |
 +------------+---------------+----------+ 